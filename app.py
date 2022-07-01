from flask import Flask
from tweet import home_timeline

app = Flask(__name__)


@app.route("/api")
def home():
    text = home_timeline()
    return f"""
<h1>Hello from Flask-Docker!</h1>

{"".join(text)}
"""


if __name__ == "__main__":
    app.run(debug=True)
