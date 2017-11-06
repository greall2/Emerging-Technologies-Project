from flask import Flask, render_template

import flask as fl

app = fl.Flask(__name__)



@app.route("/")
def route():
	return "Hello World"

if __name__ == "__main__":
	app.run()