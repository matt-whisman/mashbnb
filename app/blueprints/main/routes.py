import requests
from app import db
from app.blueprints.main.forms import StateSearchForm, CityStateSearchForm
from app.blueprints.main.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from config import Config

from . import bp as app

rapid_key = Config.RAPIDAPI_KEY


@app.route('/')
def home():
    return render_template('index.html')


cities = {
    "status": "success",
    "content": {
        "input": {
            "page": "1",
            "items": "5",
            "state": "CA"
        },
        "total_page_results": 5,
        "cities": [
            {
                "city": "Oakland",
                "state": "CA",
                "occupancy": 67.27373939,
                "total_listing": 10308,
                "occ_listing": 693457.70566304
            },
            {
                "city": "Los Angeles",
                "state": "CA",
                "occupancy": 68.45154043,
                "total_listing": 9652,
                "occ_listing": 660694.2681821
            },
            {
                "city": "San Francisco",
                "state": "CA",
                "occupancy": 72.52560682,
                "total_listing": 8109,
                "occ_listing": 588110.14568716
            },
            {
                "city": "San Diego",
                "state": "CA",
                "occupancy": 58.76988824,
                "total_listing": 6440,
                "occ_listing": 378478.0802334
            },
            {
                "city": "Long Beach",
                "state": "CA",
                "occupancy": 66.036248,
                "total_listing": 4264,
                "occ_listing": 281578.561472
            },
        ]
    }
}

cities_context = {
    "city1": {
        "city": "Oakland",
        "state": "CA",
        "occupancy": 67.27373939,
        "total_listing": 10308,
        "occ_listing": 693457.70566304
    },
    "city2": {
        "city": "Los Angeles",
        "state": "CA",
        "occupancy": 68.45154043,
        "total_listing": 9652,
        "occ_listing": 660694.2681821
    },
    "city3": {
        "city": "San Francisco",
        "state": "CA",
        "occupancy": 72.52560682,
        "total_listing": 8109,
        "occ_listing": 588110.14568716
    },
    "city4": {
        "city": "San Diego",
        "state": "CA",
        "occupancy": 58.76988824,
        "total_listing": 6440,
        "occ_listing": 378478.0802334
    },
    "city5": {
        "city": "Long Beach",
        "state": "CA",
        "occupancy": 66.036248,
        "total_listing": 4264,
        "occ_listing": 281578.561472
    }
}


@login_required
@app.route('/top-cities-search', methods=['get', 'post'])
def top_cities_search():
    url = "https://mashvisor-api.p.rapidapi.com/trends/cities"
    form = StateSearchForm()
    try:
        if form.validate_on_submit():
            state = form.state.data.upper()
            querystring = {"state": f"{state}", "items": "5", "page": "1"}
            headers = {
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring).json()
            cities = {}
            cities['city1'] = response['content']['cities'][0]
            cities['city2'] = response['content']['cities'][1]
            cities['city3'] = response['content']['cities'][2]
            cities['city4'] = response['content']['cities'][3]
            cities['city5'] = response['content']['cities'][4]
            return render_template('top-cities.html', context=cities)
    except Exception:
        flash("Invalid input")
        form.state.data = ''
        return render_template('top-cities-search.html', form=form)
    return render_template('top-cities-search.html', form=form)


rates_response = {
    "status": "success",
    "content": {
        "retnal_rates": {
            "studio_value": 2972,
            "one_room_value": 3292,
            "two_room_value": 4055,
            "three_room_value": 5710,
            "four_room_value": 5914
        },
        "sample_count": 213,
        "detailed": [  # 5 items 0-4
            {
                "state": "CA",
                "city": "Los Angeles",
                "neighborhood": None,
                "zipcode": "90291",
                "beds": "0",
                "count": 73,
                "min": 1452,
                "max": 4490,
                "avg": 3019.3150684931506,
                "median": 2972,
                "adjusted_rental_income": 3376.250000000001,
                "median_night_rate": 125,
                "median_occupancy": 81
            },
        ]
    }
}

rates_context = {
    "city": "Los Angeles",
    "state": "CA",
    "studio": 2972,
    "one_room": 3292,
    "two_room": 4055,
    "three_room": 5710,
    "four_room": 5914,
    "sample_count": 213
}


@login_required
@app.route('/rates-search', methods=['get', 'post'])
def rates_search():
    url = "https://mashvisor-api.p.rapidapi.com/rental-rates"
    form = CityStateSearchForm()
    try:
        if form.validate_on_submit():
            state = form.state.data.upper()
            city = form.city.data.title()
            querystring = {"source": "airbnb", "state": f"{state}",
                           "city": f"{city}"}
            headers = {
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring).json()
            print(response)
            rates = {}
            rates['city'] = city
            rates['state'] = state
            # there is a misspellin in the api, rental_rates is actually 'retnal_rates'
            rates['studio'] = response['content']['retnal_rates']['studio_value']
            rates['one_room'] = response['content']['retnal_rates']['one_room_value']
            rates['two_room'] = response['content']['retnal_rates']['two_room_value']
            rates['three_room'] = response['content']['retnal_rates']['three_room_value']
            rates['four_room'] = response['content']['retnal_rates']['four_room_value']
            rates['sample_count'] = response['content']['sample_count']
            flash(rates)
            return render_template('rates.html', context=rates)
    except Exception:
        flash("Invalid input")
        form.state.data = ''
        return render_template('rates-search.html', form=form)
    return render_template('rates-search.html', form=form)


summary = {
    "status": "success",
    "content": {
        "active_neighborhoods": 17,
        "investment_properties": 1475,
        "airbnb_listings": 780,
        "traditional_listings": 1490,
        "avg_property_price": 821075.718,
        "avg_price_per_sqft": 619.45463533,
        "avg_days_on_market": 218.4112,
        "avg_occupancy": 55.3341,
        "avg_nightly_price": 150.6636,
        "avg_airbnb_ROI": 0.3576789552493784,
        "avg_airbnb_rental": 3297.268772468138,
        "avg_traditional_ROI": -0.45838680145165633,
        "avg_traditional_rental": 2678.689869765255
    }
}

summary_context = summary['content']


@login_required
@app.route('/city-summary-search', methods=['get', 'post'])
def city_summary_search():
    url = "https://mashvisor-api.p.rapidapi.com/trends/summary/"
    form = CityStateSearchForm()
    try:
        if form.validate_on_submit():
            state = form.state.data.upper()
            city = form.city.data.title()
            city_url = city.replace(' ', '%20')
            url += f"{state}/{city_url}"
            headers = {
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers).json()
            print(response)
            city_summary = {}
            city_summary = response['content']
            city_summary['city'] = city
            city_summary['state'] = state
            return render_template('city-summary.html', context=city_summary)
    except Exception:
        flash("Invalid input")
        form.state.data = ''
        return render_template('city-summary-search.html', form=form)
    return render_template('city-summary-search.html', form=form)
