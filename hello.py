import config
from flask import request
from flask import Flask
import logging

app = Flask(__name__)

 
# add filemode="w" to overwrite
logging.basicConfig(filename="requests.log", level=logging.INFO)

@app.route('/', methods=['GET','POST'])
def hello_world():
    logging.info(request)
    return config.CHECK_RESPONSE
