"""
Initialisation module. It initialise Flask server and Redis client
"""
from flask import Flask
from redis import Redis

# initialise Flask
app = Flask(__name__)
# initialise Redis
redis = Redis(host="redis", port=6379)
from app import routes