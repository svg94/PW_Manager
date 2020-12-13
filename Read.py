#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id, text = reader.read()
	print(id)
	if "Hi" in text:
		print("Access granted.")
finally:
	GPIO.cleanup()

def read():
	id, text = reader.read()
	return text

