import requests
from app import db
from app.blueprints.main.forms import TopCitiesSearchForm
from app.blueprints.main.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import bp as app


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
@app.route('/top-city-search', methods=['get', 'post'])
def top_cities_search():
    url = "https://mashvisor-api.p.rapidapi.com/trends/cities"
    form = TopCitiesSearchForm()
    try:
        if form.validate_on_submit():
            # state = form.state.data
            # querystring = {"state": f"{state}", "items": "5", "page": "1"}
            # headers = {
            #     "X-RapidAPI-Key": "6918db1dd3msh4eb7255e960164dp1d2d18jsn9991606b9200",
            #     "X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
            # }
            # response = requests.request(
            #     "GET", url, headers=headers, params=querystring).json()
            # cities = {}
            # cities['city1'] = response['content']['cities'][0]
            # cities['city2'] = response['content']['cities'][1]
            # cities['city3'] = response['content']['cities'][2]
            # cities['city4'] = response['content']['cities'][3]
            # cities['city5'] = response['content']['cities'][4]
            return render_template('top-cities.html', context=cities_context)
    except Exception:
        flash("Invalid input")
        form.state.data = ''
        return render_template('top-cities-search.html', form=form)
    return render_template('top-cities-search.html', form=form)
