'''
Created on 25-Aug-2015

@author: ghanshyam
'''

import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("mobcam.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", 
			port=5000,
			debug=True)