# -*- coding: utf-8 -*-
from flask import Flask,render_template

from trafiklab.sl import sites, departures

app = Flask(__name__)



@app.route('/')
def hello_world():
    x=departures(9521)
    return render_template("index.html",departures=x)

#hack för att hitta sitid
@app.route('/sites')
def sitessearch():

    sitelist = sites(("Sodertalje hamn"))

    return str(sitelist)


if __name__ == '__main__':
    app.run(debug=True)