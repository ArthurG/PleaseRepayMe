from flask import jsonify, request
from app import app
from app.prediction import pipeline

from app import logger
from app import redis

import pickle


@app.route('/predict', methods=['GET'])
def predict():
    if not (request.args.get("thread_url", False)):
        logger.warning('Predict endpoint used with no thread_url')
        return jsonify({"Error": "Must contain thread_url"}), 400
    else:
        thread_url = request.args.get("thread_url", False)
        result = redis.get(thread_url)
        if result:
            logger.info('Predict endpoint cache hit', url=thread_url)
            print(pickle.loads(result))
            return jsonify(pickle.loads(result))
        else:
            answer = pipeline.make_prediction(thread_url)
            redis.setex(thread_url, 60*24*2, pickle.dumps(answer)) # Cache expires in 2 days
            logger.info('Predict endpoint cached result', url=thread_url)
            return jsonify(answer)

