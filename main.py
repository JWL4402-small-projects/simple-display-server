from flask import Flask, render_template, request
from threading import Thread
import json

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/requests', methods=["GET", "POST"])
def requests():
	if request.method == "GET":
		msg = ''
		response = app.response_class(
			response = json.dumps(msg),
			status = 200,
			mimetype = 'application/json',
			content_type = 'json'
		)
		return response

def run():
	app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
	thread = Thread(target = run())
	thread.start()