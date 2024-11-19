'''
Wen Zhang, Kyle Lee, Danny Huang, Tracy Ye
Made-in-Nigeria
SoftDev
P00 - Move Slowly and Fix Things
Time Spent:
Target Ship Date: 2024-11-011
'''

# import necessary

import sqlite3
import csv
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash


import database

# flask hosting base

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/", methods=['GET', 'POST'])
def root():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template("main.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        if session.pop('signup_success', None):
            flash("Account created successfully! Please log in.")
        elif request.method == "POST":
            username = request.form['username']
            password = request.form['pw']
            user = database.viewAccount(username)
            
            if len(user) > 0:
                stored_password = user[0][0]
                if password == stored_password:
                    session['username'] = username
                    return redirect(url_for('dashboard'))
                else:
                    flash("Incorrect password. Please try again.")
            else:
                flash("No account found with that username. Please sign up.")
        
        return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pw']
        if database.accountExists(username):
            flash("Username already exists. Please choose a different username.")
        else:
            database.addAccount(username, password)
            session['signup_success'] = True
            return redirect(url_for('login'))
    
    return render_template("signup.html")

@app.route("/user", methods=['GET', 'POST'])
def dashboard():
    if 'username' in session:
        user = database.viewAccount(session['username'])
        return render_template("dashboard.html", uname=session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/edit", methods=['GET', 'POST'])
def edit_page():
    if 'username' in session:
        entry = database.get_entry(session['username'], session['blogTitle'], session['entryID'])
        if request.method =="POST":
            database.edit_entry(session['username'], session['blogTitle'], session['entryID'], request.form['entryTitle'], request.form['entryContent'])
            return redirect(url_for('view'))
        print("_________________________")
        print(entry)
        return render_template("edit_page.html", entry = entry)
    else:
        return redirect(url_for('login'))

@app.route("/create", methods=['GET', 'POST'])
def create_page():
    if 'username' in session:
        if request.method =="POST":
            database.addBlog(session['username'], request.form['blog_title'])
            flash(f"Blog {request.form['blog_title']} Created Successfully.")
            return redirect(url_for('view'))
        return render_template("create_page.html", uname = session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/view", methods=['GET', 'POST'])
def view():
    if 'username' in session:
        blogs = database.get_blog()
        owners = []
        blogtitles = []
        for (owner, blogtitle) in blogs:
            owners.append(owner)
            blogtitles.append(blogtitle)
        return render_template("view.html", owners=owners, blogtitles=blogtitles, blogs = blogs, user = session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/view/<owner>/<blogtitle>", methods=['GET', 'POST'])
def viewBlog(owner, blogtitle):
    if 'username' in session:
        session['author'] = owner
        session['blogTitle'] = blogtitle
        entries = database.get_entries(owner,blogtitle)
        edit = False
        if session['author'] == session['username']:
            edit = True
        if request.method == "POST":
            session['entryID'] = request.form.get('entryID')
            return redirect(url_for('edit_page'))
        return render_template("viewBlog.html", owner=owner, blogtitle=blogtitle, entries=entries, edit = edit)
    else:
        return redirect(url_for('login'))

@app.route("/addEntry", methods=['GET', 'POST'])
def add():
    if 'username' in session:
        if request.method =="POST":
            database.addentry(session['username'], session['blogTitle'], request.form['entryTitle'], request.form['entryContent'])
            flash("New Entry Added Successfully.")
            return redirect(url_for('view'))
        return render_template("add.html", uname = session['username'], blogtitle = session['blogTitle'])
    else:
        return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
