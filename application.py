import os
import pymysql
from flask import Flask, abort, request, jsonify
from sqlalchemy import create_engine, text
from config import app_config
from http import HTTPStatus
from pprint import pprint

app = Flask(__name__)
flask_env = os.getenv('FLASK_ENV')
cfg = app_config[flask_env]
pprint(vars(cfg))
app.config.from_object(cfg)
engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(cfg.DB_USERNAME,cfg.DB_PASSWORD,cfg.DB_HOST,cfg.DB_PORT,cfg.DB_NAME),echo=True)
conn = engine.connect()
app.run()

@app.route('/health', methods=['GET'])
def health():
   return 'OK!'

@app.route('/runsql', methods=['POST'])
def run_sql():
        if not request.json:
                abort(400)

        if not 'query' in request.json or request.json['query'] == "":
                return "query field not found", HTTPStatus.BAD_REQUEST

        res = conn.execute(request.json['query']).fetchall()

        resp = []
        for r in res:
                d = { "id": r[0], "data": r[1]}
                resp.append(d)
                
        return jsonify(resp, HTTPStatus.OK)

        


