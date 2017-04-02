from flask import jsonify, request
from app import app


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        return jsonify({"Error": "Must contain thread_url"}), 400
    return jsonify({"user": "arthur", "prediction": 0.95855})


