from flask import render_template, jsonify
from app import app
import random


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404
