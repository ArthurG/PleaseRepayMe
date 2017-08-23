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
        return jsonify({"error": "Must contain thread_url"}), 400
    else:
        thread_url = request.args.get("thread_url", False)

        #Look in the cache for result
        result = False
        if app.config["REDIS_ON"]:
            result = redis.get(thread_url)

        if result: 
            #Cache hit
            logger.info('Predict endpoint cache hit', url=thread_url)
            print(pickle.loads(result))
            return jsonify(pickle.loads(result))
        else:
            answer, status_code = pipeline.make_prediction(thread_url)
            if (status_code == 200) and app.config["REDIS_ON"]: 
                #Cache the prediction
                redis.setex(thread_url, app.config["REDIS_DURATION"], pickle.dumps(answer)) # Cache expires in 2 days
                logger.info('Predict endpoint cached result', url=thread_url)

            return jsonify(answer), status_code

