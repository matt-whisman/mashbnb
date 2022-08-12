response = {
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

city_summary = {}
city_summary = response['content']
city_summary['city'] = 'Miami Beach'
city_summary['state'] = 'FL'



