from flask import Flask, render_template, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

def run():
	app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
	thread = Thread(target = run())
	thread.start()