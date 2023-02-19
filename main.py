from flask import Flask, render_template, request
from threading import Thread
import json

app = Flask(__name__)
json_data = {
	'messages': []
}

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/requests', methods=["GET", "POST"])
def requests():
	if request.method == "GET":
		response = app.response_class(
			response = json.dumps(json_data),
			status = 200,
			mimetype = 'application/json',
			content_type = 'json'
		)
		return response

	if request.method == "POST":
		print(request)
		data = json.loads(request.json)
		if not data['message']:
			return "No message attached.", 400

		message = data['message']
		json_data['messages'].append(message)

		return "Message received.", 200


def run():
	app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
	thread = Thread(target = run())
	thread.start()