from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import requests
from config import *

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup')
def setup():
    return render_template('setup.html')

@app.route('/shutter_up', methods=['POST'])
def shutter_up():
    print("up")
    return jsonify(data="up")

@app.route('/shutter_down', methods=['POST'])
def shutter_down():
    print("down")
    return jsonify(data="down")

@app.route('/train', methods=['POST'])
def train():
    json_data = request.json
    print (json_data)
    if json_data["data"] == "train":
        res = requests.post(url_pre + '/shutter_down')
    elif json_data["data"] == "no_train":
        res = requests.post(url_pre + '/shutter_up')
    return jsonify(data="ok")

@app.route('/setup/shutter/up',methods = ['POST', 'GET'])
def manual_shutter_up():
    res = requests.post(url_pre + '/shutter_up')
    return redirect(url_for('setup'))

@app.route('/setup/shutter/down',methods = ['POST', 'GET'])
def manual_shutter_down():
    res = requests.post(url_pre + '/shutter_down')
    return redirect(url_for('setup'))


if __name__ == '__main__':
   app.run(port = port, debug = True, use_reloader = False)
