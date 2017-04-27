from flask import jsonify, request
from app import app
from app.prediction import pipeline


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        return jsonify({"Error": "Must contain thread_url"}), 400

    thread_url = request.args.get("thread_url", False)
    usernameStr = pipeline.get_user_from_thread_url(thread_url)
    #prediction = pipeline.predict(usernameStr)
    return jsonify({"user": usernameStr, "prediction": "1.0"})


