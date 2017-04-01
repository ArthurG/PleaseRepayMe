from flask import render_template, jsonify, request
from flask_restful import Resource, reqparse
from app import app, models, db, api
import datetime

parser = reqparse.RequestParser()
parser.add_argument('transaction_id')
parser.add_argument('borrower_name')
parser.add_argument('thread_link')
parser.add_argument('lender_name')
parser.add_argument('lender_comment_url')
parser.add_argument('agree_comment_url')
parser.add_argument('date_requested', type=lambda x: datetime.datetime.fromtimestamp(x))
parser.add_argument('payment_prediction')
parser.add_argument('lender_comment_url')
parser.add_argument('payment_prediction')
parser.add_argument('result_thread')
parser.add_argument('status', type=lambda x: models.StatusType.fromstring(x))

class Transaction(Resource):
    def get(self, transaction_id):
        m = models.Transaction.query.filter_by(transaction_id=transaction_id).first_or_404()
        del m._sa_instance_state 
        return jsonify(m.__dict__)
    def post(self, transaction_id):
        m = models.Transaction.query.filter_by(transaction_id=transaction_id)
        update_vals = parser.parse_args()
        update_vals.pop("transaction_id", None)
        m.update(update_vals)
        db.session.commit()

        m2 = m.first()
        del m2._sa_instance_state 
        return jsonify(m2.__dict__)
    #Delete transaction not implemented

class TransactionList(Resource):
   def get(self):
       ans = models.Transaction.query.all()
       for m in ans:
           del m._sa_instance_state 
       return jsonify({"transactions": [item.__dict__ for item in ans]})
   def post(self):
       args = parser.parse_args()
       model = models.Transaction(**args)
       db.session.add(model)
       db.session.commit()

       m = models.Transaction.query.filter_by(transaction_id=model.transaction_id).first()
       del m._sa_instance_state
       return jsonify(m.__dict__)

  

api.add_resource(Transaction, '/transaction/<transaction_id>')
api.add_resource(TransactionList, '/transactions')
