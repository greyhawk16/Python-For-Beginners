from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", name='DDG')


@app.route('/hello')
def hello():
    return "hello?"


app.run('127.0.0.1', debug=True)
