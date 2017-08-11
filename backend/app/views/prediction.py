from flask import jsonify, request
from app import app
from app.prediction import pipeline

from app import logger


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        logger.warning('Predict endpoint used with no thread_url')
        return jsonify({"Error": "Must contain thread_url"}), 400
    else:
        thread_url = request.args.get("thread_url", False)
        return jsonify(pipeline.make_prediction(thread_url))

