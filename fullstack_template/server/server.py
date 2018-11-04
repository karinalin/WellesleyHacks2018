#server.py
import os
from stream import write_haiku
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/addURL", methods = ['POST', 'GET'])
def addURL():
    if request.method == 'POST':
        url = request.form['keyword']
        haiku = stream.write_haiku(url)
    return render_template('index.html', haiku = haiku)

if __name__ == "__main__":
    app.run()
