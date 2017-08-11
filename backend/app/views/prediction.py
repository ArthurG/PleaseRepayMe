from flask import jsonify, request
from app import app
from app.prediction import pipeline


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        return jsonify({"Error": "Must contain thread_url"}), 400
    else:
        thread_url = request.args.get("thread_url", False)
        return jsonify(pipeline.make_prediction(thread_url))

