"""
This module is used to create light weight web service using flask.
The web service running on a local host,on port 5000
The web service expose the following end points
    1. /convert/fahrenheit/
    2./convert/celsius/
    3./convert/kelvin/
    4./convert/rankine/
Each of the end points recieve a temperatuer and returns a json object
python : 2.7 must be used 

"""

from flask import Flask,render_template
from flask import jsonify
import inspect # this module helps to get the stack trace
app = Flask(__name__)

def convertor_function(x):
    """ This is a common function which accepts numerical values from the predefined functions and 
    calculates the other 3 temperature parameters using formulas"""
    C=K=F=R= 0
    x = int(x)
    caller_fuction_name = inspect.stack()[1][3]
    if caller_fuction_name == 'from_fahrenheit' :
        print "converting from fahrenheit"
        C = (float)(x - 32) * 5/9
        K = (float) (x+459.7) * 5/9
        R = x + 459.67
        return C,K,R
    elif caller_fuction_name == 'from_celsius' :
        print "converting from celsius"
        F = (float) (x *1.8) + 32
        K =  (float) (x) + 273.15
        R =  (float)(x + 273.15) * 1.8
        return F,K,R
    elif caller_fuction_name == 'from_kelvin' :
        print "converting from kelvin"
        F = (float)(x)*1.8 - 459.67
        C = (float)(x) - 273.15
        R = (float)(x) *1.8
        return F,C,R   
    elif caller_fuction_name == 'from_rankine' :
        print "converting from rankine"
        F = (float)(x) - 459.67
        C = (float)(x) - 491.67 *5/9
        K = (float)(x)*5/9
        return F,C,K
    
#defining routes here

@app.route("/")
def main():
    """ This is just a home page for this web service"""
    return "<h1>Welcome to the temperature convertor home page</h1>"

@app.route("/convert/fahrenheit/<page_id>")
def from_fahrenheit(page_id):
    celsius,kelvin,rankine = convertor_function(page_id)
    return jsonify("{'celsius' : %s,'kelvin' : %s,'rankine' : %s}"%(celsius,kelvin,rankine))


@app.route("/convert/celsius/<page_id>")
def from_celsius(page_id):
    fahrenheit,kelvin,rankine = convertor_function(page_id)
    return jsonify("{'fahrenheit' : %s,'kelvin' : %s,'rankine' : %s}"%(fahrenheit,kelvin,rankine))

@app.route("/convert/kelvin/<page_id>")
def from_kelvin(page_id):
    fahrenheit,celsius,rankine = convertor_function(page_id)
    return jsonify("{'fahrenheit' : %s,'celsius' : %s,'rankine' : %s}"%(fahrenheit,celsius,rankine))

@app.route("/convert/rankine/<page_id>")
def from_rankine(page_id):
    fahrenheit,celsius,kelvin = convertor_function(page_id)
    return jsonify("{'fahrenheit' : %s,'celsius' : %s,'kelvin' : %s}"%(fahrenheit,celsius,kelvin))



@app.route("/convert/rankine/")
@app.route("/convert/fahrenheit/")
@app.route("/convert/celsius/")
@app.route("/convert/kelvin/")
@app.route("/convert/")
@app.route("/convert/")
@app.route("/convert/")
@app.route("/convert/")
def nnot_valid():
    return "<ul> <li><h2> Please enter the metric followed by the temperature</li></h2>\
     <h3><li>Please read the docstring of the module for further information on the usage</li></h3> </ul>"


if __name__ == "__main__":
    app.run()