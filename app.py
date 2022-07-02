from flask import Flask, render_template
from tweet import home_timeline
import os

app = Flask(__name__)


@app.route("/")
def hoge():
    tweets = home_timeline(use_dummy=True)
    return render_template("index.html", name=os.getenv("NAME"), tweets=tweets, len=len(tweets["text"]))


@app.route("/api")
def home():
    tweets = home_timeline()
    return render_template("index.html", name=os.getenv("NAME"), tweets=tweets, len=len(tweets["text"]))


if __name__ == "__main__":
    app.run(debug=True)
