from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Tähän tulee paikka, jossa voi laitta luovia ideoita ja muut voi toteuttaa niitä "
