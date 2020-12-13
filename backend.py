from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
reader = SimpleMFRC522()

def readPW():
	text = ""
	try:
		id, text = reader.read()
	finally:
		GPIO.cleanup()
	return text
#	text = ""
#	try:
#		id, text = reader.read()
#	finally:
#		GPIO.cleanup()
#	return text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/auth', methods=['GET'])
def auth():
	print("Hello", file=sys.stdout)
	output = readPW()
	if("Hi" in output):
		print("Access")
		return "Access granted."
	else :
		print("No")
		return  "Access denied."


