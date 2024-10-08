# ASK (Alex, Sascha, Kyle)
# SoftDev
# Sep 30 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
It would give an error if you tried to access /my_foist_template through
localhost:5000/my_foist_template. 

Q1:
localhost:5000/my_foist_template

Q2:
model_templt.html is the template to render
foo = "foooo" tells jinja that foo is "foooo" and should be rendered as that
collection = coll tells jinja that while rendering the page  collection refers to 
to the list coll = [0,1,1,2,3,5,8]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template #Render_template allows you to use python code in html
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()