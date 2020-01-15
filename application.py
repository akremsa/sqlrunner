import os

from flask import Flask
from config import app_config

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return 'Hello, World!'

flask_env = os.getenv('FLASK_ENV')   
app.config.from_object(app_config[flask_env])
app.run()

