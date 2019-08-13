# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:34:40 2019

@author: Frej Nielsen
"""

from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__, template_folder='./templates')



@app.route('/')
@app.route('/<int:station_id>')
def homepage(station_id=8600600):
    r = requests.get(
    f'http://xmlopen.rejseplanen.dk/bin/rest.exe/departureBoard?id={station_id}&format=json')
    data = r.json()
    departure = data['DepartureBoard']['Departure']        
    return render_template('index.html', data=departure)

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)