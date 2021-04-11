from flask import Flask
from os import environ
import logging
app = Flask(__name__)


if environ.get('PROFILE') == 'DEV':
    logging.info("Loading Dev Config")
    app.config.from_object('config.config.DevConfig')
elif environ.get('PROFILE') == 'PROD':
    logging.info("Loading Prod Config")
    app.config.from_object('config.config.ProdConfig')


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # Only for debugging while developing
    app.config.from_object('config.config.LocalConfig')
    app.run(host='0.0.0.0', debug=True, port=8080)
