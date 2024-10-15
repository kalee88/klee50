#Kyle Lee
#K^3 (Kyle, Suhana, Vedant)
#SoftDev
#K6 -- Reading Files
#2024-09-18
#time spent: .75

import os
from flask import render_template
from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    if 'username' in session:
        return redirect("/response.html")
    return render_template( 'login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    method1 = request.method
    if request.method == 'POST':
        username = request.form['username']
        requesttype = "POST"
    else:
        username = request.args.get('username')
        requesttype = "GET"
    
    return render_template( 'response.html', username=username, request = requesttype )

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template( 'logout.html')


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()