from flask import Flask, render_template
from xata.client import XataClient

app = Flask(__name__)
xata = XataClient()

@app.route("/")
def hello_world():
  data = xata.data().query("community", {

    "columns": [
        "name",
        "photo",
        "role",
        "uname",
        "comment"
    ]
  })
  return render_template("index.html", items=data)
