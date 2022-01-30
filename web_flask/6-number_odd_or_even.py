#!/usr/bin/python3
""" Starts a Flask web application listeniing on 0.0.0.0:5000"""


from flask import Flask, render_template
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


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python_text(text):
    return "Python " + str(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def check_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
