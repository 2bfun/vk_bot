import config
import requests
import logging
from flask import Flask

app = Flask(__name__)

 
# add filemode="w" to overwrite
logging.basicConfig(filename="requests.log", level=logging.INFO)

@app.route('/')
def hello_world(r):
    logging.info(r)
    return config.CHECK_RESPONSE
