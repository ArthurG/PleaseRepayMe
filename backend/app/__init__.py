from flask import Flask
from flask_restful import Api
from flask_cors import CORS 

app = Flask(__name__)
#api = Api(app)
CORS(app)

# Setup the app with the config.py file
app.config.from_object('app.config')

# Setup the logger
from app.logger_setup import logger

#Import Redis
from app.redis_setup import redis

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

# Import the views
from app.views import main, prediction

