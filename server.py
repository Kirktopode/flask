#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, jsonify
from dateutil.parser import parse
from datetime import datetime

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

@app.route('/')
def homepage():
    print("index")
    """Displays thot hormeparger."""
    return render_template('index.html')
    
@app.route('/api/time/<string:time_string>/', methods=['GET', 'POST'])
def time(time_string):
    """Simple API my hoes and dreas.
    """
    print("time")
    stamp = {
       "error":"Invalid Date", 
    }
    try:
      date = datetime.fromtimestamp(parse(time_string.replace("_"," ").replace("+"," ")).timestamp())
      datestring = date.strftime("%a, %d %b %Y %H:%M:%S GMT")
      timestamp = date.timestamp()
      stamp = {
         "unix": int(timestamp * 1000),
         "utc": datestring,
      }
    except Exception as e:
      print(str(e))
      stamp = stamp
    return jsonify(stamp)

if __name__ == '__main__':
    app.run()