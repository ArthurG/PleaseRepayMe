import redis
from app import app

redis = redis.StrictRedis(host=app.config["REDIS_HOST"], 
                          port=app.config["REDIS_PORT"], 
                          db=app.config["REDIS_DB"])
