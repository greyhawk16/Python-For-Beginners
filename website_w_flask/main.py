from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask(__name__, template_folder="templates")
base_url = '127.0.0.1'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")  # keyword: user's input
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)

    jobs = indeed + wwr
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run(base_url)
