from flask import jsonify
from app import app


@app.route('/statistics', methods=['GET'])
def statistics():
    ##Do something with database
    return jsonify({"precision": 0.9585, "accuracy": 0.34243, "recall": 0.32135})


