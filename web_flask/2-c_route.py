#!/usr/bin/python3
""" Starts a Flask web application listeniing on 0.0.0.0:5000"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def get_c_text(text):
    return "C " + str(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
