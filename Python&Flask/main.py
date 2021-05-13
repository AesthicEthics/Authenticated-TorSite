#Currently a random number generated as I am developing the C code for ESP8266s 
from flask import Flask
from flask import render_template
import time
import requests
import random
from random import randint
import json

app = Flask(__name__)

apikey = "redacted"
base = "http://api.openweathermap.org/data/2.5/weather?"
city = 'Toronto'

complete = base+'appid='+apikey+'&q='+city

result = requests.get(complete)

acc = result.json()

y = acc['main']
temp = str(round(int(y['temp']) - 273.15))

c = random.randint(0,10)

d = (c)/(2.0)

if d.is_integer() == True:
    stat = "Online"
else:
    stat = "Offline"



@app.route('/', methods= ['GET'])
def index():

    return  render_template('index.html', temprature=(temp), status1=(stat))


if __name__ == '__main__':
  app.run(host ='0.0.0.0', port=8080, debug=True)
