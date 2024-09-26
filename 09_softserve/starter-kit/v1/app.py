# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
'''
127.0.0.1 - - [24/Sep/2024 11:29:23] "GET / HTTP/1.1" 200 -
'''
