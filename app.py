from flask import Flask, render_template
from tweet import home_timeline
import os

app = Flask(__name__)


@app.route("/")
def hoge():
    return render_template("index.html", name=os.getenv("NAME"))


@app.route("/api")
def home():
    text = home_timeline()
    return f"""
<h1>Hello from Flask-Docker!</h1>

{"".join(text)}
"""


if __name__ == "__main__":
    app.run(debug=True)
