# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. If you click http://127.0.0.1:5000/ while holding control it will redirect you to a page which states "No hablo queso!"
1. 
2. 
3. 
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
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