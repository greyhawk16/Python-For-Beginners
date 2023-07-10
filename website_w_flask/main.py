from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")
base_url = '127.0.0.1'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    print('request.args: ', request.args)
    print('keyword:      ', request.args.get("keyword"))
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)


app.run(base_url)
