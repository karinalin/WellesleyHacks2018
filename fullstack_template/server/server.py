#server.py
import os
from stream import write_haiku
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/addURL/", methods = ['POST', 'GET'])
def addURL():
	if request.method == 'POST':
		url = request.form["keyword"]
		haiku_lines = write_haiku(url)
	return render_template('index.html', haiku_lines = haiku_lines, url=url)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, use_reloader=True, host='0.0.0.0', port=port)
