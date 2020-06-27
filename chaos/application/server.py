import datetime
import os 
from flask import Flask, jsonify, request
from chaos.infrastructure.config.config import config
import pandas as pd

from chaos.domain.customer import Customer
import chaos.settings.base as base
from os.path import splitext, basename
import logging
base.enable_logging(log_filename=f'{splitext(basename(__file__))[0]}.log', logging_level=logging.DEBUG)

import joblib

app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]
        
@app.route("/score", methods=["POST"])
def score():
    try:
        client_marketing_data = request.get_json()["marketing"]
        prediction = Customer(marketing=client_marketing_data).predict_subscription()
        message =  "ok" 
        answer = prediction

    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
        message = "exception raised"
    response = {"answer": answer, "message": message}
    return jsonify(response)

if __name__ == "__main__":
    logging.info('--------------------')
    logging.info('Starting API ...')    
    print("starting API at", datetime.datetime.now())
    app.run(debug=True, host=HOST, port=PORT)
logging.info('... Closed API')
logging.info('--------------------')