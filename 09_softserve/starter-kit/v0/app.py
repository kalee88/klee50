# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                
'''
__main__
127.0.0.1 - - [24/Sep/2024 11:28:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 11:28:59] "GET /favicon.ico HTTP/1.1" 404 -
'''
