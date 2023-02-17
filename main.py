from flask import Flask, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
	return "Hello world!"

def run():
	app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
	thread = Thread(target = run())
	thread.start()