#!/usr/bin/python
from flask import Flask
from flask import render_template
import time
import requests
import random
from random import randint
import json
import subprocess



networks = subprocess.check_output('sudo iwlist wlan0 scanning | grep ESSID',shell=True)
networks = networks.decode('ascii')
networks = networks.replace('\r','')
ssid = networks.split('\n')
ssid = ssid[4:]

app = Flask(__name__)

apikey = "6e5185f9ae58143d2c4fefc5a4d8d706"
base = "http://api.openweathermap.org/data/2.5/weather?"
city = 'Toronto'

complete = base+'appid='+apikey+'&q='+city

result = requests.get(complete)

acc = result.json()

y = acc['main']
temp = str(round(int(y['temp']) - 273.15))


if any("Redacted" in s for s in ssid):
    stat = "Online"
else:
    stat = "Offline"


@app.route('/', methods= ['GET'])
def index():

    return  render_template('index.html', temprature=(temp), status1=(stat))


if __name__ == '__main__':
  app.run(host ='0.0.0.0', port=8080, debug=True)
