#!/usr/bin/env python3
from flask import Flask, jsonify
import RPi.GPIO as gpio

app = Flask(__name__)
pin = 4
app.status = 0
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

@app.route("/")
def hello():
        app.status = gpio.input(pin)
        return jsonify(action='get', status=bool(app.status))

@app.route("/on")
def turnon():
        app.status = 1
        gpio.output(pin, app.status)

@app.route("/off")
def turnoff():
        app.status = 0
        gpio.output(pin, app.status)
        return jsonify(action='off', status=bool(app.status))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)