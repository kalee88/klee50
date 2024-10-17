# K^3 : Kyle Lee, Suhana Kumar, Vedent Kothari
# SoftDev
# Oct 16th 2024
# DEMO
# basics of /static folder

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating


app = Flask(__name__)    #create Flask object
@app.route("/")
def htmlrender():
    
    return render_template( 'index.html')

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()