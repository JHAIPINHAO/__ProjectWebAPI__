from flask import Flask
from api import api1

app = Flask(__name__)
app.register_blueprint(api1)


@app.route("/")
def index():
    return "<h1>Hello! 某某某!</h1>"