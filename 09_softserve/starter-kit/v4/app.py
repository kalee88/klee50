# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
# Same debugger pin as v3
from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
'''
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 142-081-659
'''
