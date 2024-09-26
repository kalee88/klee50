# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()
'''
about to print __name__...
__main__
127.0.0.1 - - [24/Sep/2024 11:31:07] "GET / HTTP/1.1" 200 -
'''
