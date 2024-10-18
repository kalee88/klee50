'''
Kyle Lee
# K^3 (Vedant Kothari, Suhana Kumar, Kyle Lee)
# SoftDev
# Learn more about what Flask is
# 2024-09-21
# time spent: 0.75 hours

DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. I believe I have seen similar syntax in Java, where you call a function name (Flask in this case), and enter a parameter inside for what you want to run the function with. 
1. A point of reference I have for the meaning of '/' is new line, where we use '/n'. I've also seen it in the terminal, where we use it to travel to different directories. 
2. What is the use of Flask?
3. 
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
We found points of reference to deduce the meaning of each term. 
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
                                         # We see this in many typesetting langauges such as LaTeX and HTML. We also see it in the file system indicating a directory.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? 
def hello_world():                       # Additionally in the file system when you go into a specific path, each directory and file is seperated by a /
    print(__name__)                      # Q2: Where will this print to? http://127.0.0.1:5000/ or an IP adress
                                         # http://127.0.0.1:5000/ or an IP adress
                                         # Q3: What will it print? No Hablo Queso!
                                         # No Hablo Queso!
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? On the corresponding IP with
                                         # It seems to create a new text document that has No hablo queso! on it
app.run()                                # Q5: Where have you seen similar constructs in other languages? 
                                         # We have seen similar constructs when creating an html file and just writing in No hablo queso and running it. Maybe this program just puts No hablo queso into an empy HTML file
