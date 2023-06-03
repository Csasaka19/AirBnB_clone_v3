#!/usr/bin/python3
"""Returns JSON status"""
from api.v1.views import app_views
from models import storage
from flask import request, jsonify


@app_views.route('/status')
def status():
    """
    function for status route that returns the status code OK
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
