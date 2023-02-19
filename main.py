from flask import Flask, render_template, request
from threading import Thread
import os
import json

dirname = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(dirname, 'data', 'messages.json')

if not os.path.exists(fp): # ensure file exists
	open(fp, 'w').close()
	

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/requests', methods=["GET", "POST"])
def requests():
	if request.method == "GET":
		data = ''
		with open(fp, 'r') as f:
			data = f.read() # already json

		response = app.response_class(
			response = data,
			status = 200,
			mimetype = 'application/json',
			content_type = 'json'
		)

		return response

	if request.method == "POST":
		post = json.loads(request.json)
		
		msg = post.get('message', None)
		if msg is None:
			return "No message attached.", 400
		
		author = post.get('author', None)
		time = post.get('time', None)

		data = {
			'content': msg,
			'author': author,
			'time': time
		}

		with open(fp, 'r') as f:
			file_data = ""
			file_data = f.read()
		
			if file_data == "":
				messages = { 'messages': [] }
			else:
				messages = json.loads(file_data)
		
			messages['messages'].append(data)

		with open(fp, 'w') as f:	
			json_data = json.dumps(messages)
			f.write(json_data)

		return "Message received.", 200

@app.route('/requests/clear', methods=["POST"])
def clear(): # todo : check if sent by localhost^
	if request.method != "POST": return
	open(fp, 'w').close()
	return "Sucessfully cleared", 200

def run():
	app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
	thread = Thread(target = run())
	thread.start()