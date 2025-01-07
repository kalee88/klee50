# Team JK - Jessica Yu, Kyle Lee
#SoftDev
#K23
#2024-11-21
#time spent : 1


import urllib.request
import json
from flask import Flask, render_template
app = Flask(__name__)
app.run(port=5001)

@app.route("/")
def main():
    with open("key_nasa.txt", "r") as file:
        key = file.read()
    request = requests.get(key).json()
    with urllib.request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={key}:") as response:
        html = response.read()
        data = json.loads(html)
    return render_template("main.html",text=request['explanation'],img1 = request['url'], img2 = request['hdurl'])

if __name__ == "__main__":
    app.debug = True
    app.run()
