#!/usr/bin/python3
"""first endpoint (route) will be to return the status of the API"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, Blueprint
from os import getenv
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(error):
    """json 404 page"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown(exception=None):
    """This method closes the storage to end session"""
    storage.close()


if __name__ == "__main__":
    port = getenv('HBNB_API_PORT', default=5000)
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    app.run(host, int(port), threaded=True)
