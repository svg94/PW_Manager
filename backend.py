from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
from pymongo import MongoClient
import json

reader = SimpleMFRC522()
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/DBPasswords"
DOMAIN = "192.168.100.40"
MONGO_PORT = 27017

def readPW():
	text = ""
	try:
		id, text = reader.read()
	finally:
		GPIO.cleanup()
	return text


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/auth', methods=['GET'])
def auth():
	print("Hello", file=sys.stdout)
	output = readPW()
	if("Hi" in output):
		print("Access")
		return db()
	else :
		print("No")
		return  "Access denied."
#@app.route('/db', methods=['GET'])
def db():
	documents ={}
	client = MongoClient()
	db = client.DBPasswords
	pws = db.passwords
	result = pws.find_one()
	return "Account bei: "+result["name"]+" <br>password: "+result["pw"]

	



