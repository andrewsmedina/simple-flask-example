from flask import Flask

import os


app = Flask(__name__)


@app.route("/")
def index():
    return "\o/"


if __name__ == "__main__":
    app.run(port=8888, host="0.0.0.0")
