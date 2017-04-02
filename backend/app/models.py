from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

from app import db, bcrypt
import enum


class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

class StatusType(enum.IntEnum):
   looking_lender  = 0
   wait_confirm  = 1
   wait_repay = 2
   resolve_repaid = 3
   resolve_defaulted  = 4
   def __str__(self):
       return str(self.value)
   def __repr__(self):
       return str(self.value)
   @classmethod
   def fromstring(cls, i):
       return getattr(cls, i, None)

class Transaction(db.Model):

    ''' A transaction on the /r/borrow subreddit '''

    __tablename__ = 'transaction'

    transaction_id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String)
    lender_name = db.Column(db.String)
    date_requested = db.Column(db.DateTime)
    repayment_probability = db.Column(db.Float)
    original_thread_url = db.Column(db.String)
    lender_comment_url = db.Column(db.String)
    agree_comment_url = db.Column(db.String)
    settle_thread_url = db.Column(db.String)
    status = db.Column(db.Enum(StatusType))

    def add_lender(self, lender_name, lender_comment_url):
        self.lender_name = lender_name
        self.lender_comment_url = lender_comment_url
        self.status = StatusType.confirm
   
    def add_agreement(self, agree_comment_url):
        self.agree_comment_url = agree_comment_url
        self.status = StatusType.repayment

    def finish_transaction(self, is_repaid, result_thread):
        self.result_thread = result_thread
        if is_repaid:
            self.status = StatusType.repaid
        else:
            self.status = StatusType.defaulted
