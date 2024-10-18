'''
Kyle Lee, Vedant Kothari, Suhana Kumar
Team Name: K^3
K18 - Serving Looks
2024-10-16
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating


app = Flask(__name__)    #create Flask object
@app.route("/")
def htmlrender():
    
    return render_template( 'index.html')

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
