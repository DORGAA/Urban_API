from flask import Flask
app = Flask(__name__)


def logger(message):
    app.logger.info(message)
