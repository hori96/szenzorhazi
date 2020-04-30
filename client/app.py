from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import requests
from config import *

app = Flask(__name__)

@app.route('/shutter_down', methods=['POST'])
def shutter_down():
    print("down")
    return jsonify(data="down")

@app.route('/shutter_up', methods=['POST'])
def shutter_up():
    print("up")
    return jsonify(data="up")

@app.route('/temperature',methods = ['GET'])
def temperature():
    x = "10"
    return jsonify(temperature=x), 200


if __name__ == '__main__':
   app.run(host=host, port = port, debug = True, use_reloader = False)
