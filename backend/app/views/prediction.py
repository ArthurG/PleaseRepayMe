from flask import jsonify, request
from app import app
from app.prediction import pipeline


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        return jsonify({"Error": "Must contain thread_url"}), 400

    thread_url = request.args.get("thread_url", False)
    usernameStr = pipeline.get_user_from_thread_url(thread_url)
    predictive_data = pipeline.get_predictive_data(usernameStr)
    predictions = pipeline.predict_user_repayment2(predictive_data) 
    return jsonify({"user": usernameStr, 
                    "prediction": [str(predictions[1][0][0]), str(predictions[1][0][1]), str(predictions[1][0][2])],
                    "guess": str(predictions[0][0]),
                    "num_borrow": predictive_data["num_borrow"], 
                    "num_req": predictive_data["num_req"]})


