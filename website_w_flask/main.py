from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
base_url = '127.0.0.1'


@app.route("/")
def home():
    return render_template("home.html", name='DDG')


@app.route("/search")
def hello():
    return render_template("search.html")


app.run(base_url, debug=True)
