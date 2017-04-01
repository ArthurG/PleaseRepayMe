from flask import render_template, jsonify
from app import app, models, db


@app.route('/transaction')
def transaction_all():
    return jsonify(models.Transaction.query.all())

@app.route('/transaction/', methods=['POST'])
def add_transaction():
    return render_template('map.html', title='Map')

@app.route('/transaction/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    return render_template('map.html', title='Map')

@app.route('/transaction/<transaction_id>', methods=['POST'])
def update_transaction(transaction_id):
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})

#Delete transaction not implemented
