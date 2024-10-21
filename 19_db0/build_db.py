#K^3 : Kyle Lee, Suhana Kumar, Vedent Kothari
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tableCourse = "<table><tr><th>code</th><th>mark</th><th>id</th></tr>"
tableName = "<table><tr><th>name</th><th>age</th><th>id</th></tr>"
with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tableCourse += "<tr>"
        tableCourse += "<td>" + row['code'] + "</td>"
        tableCourse += "<td>" + row['mark'] + "</td>"
        tableCourse += "<td>" + row['id'] + "</td>"
        tableCourse += "</tr>"
with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tableName += "<tr>"
        tableName += "<td>" + row['name'] + "</td>"
        tableName += "<td>" + row['age'] + "</td>"
        tableName += "<td>" + row['id'] + "</td>"
        tableName += "</tr>"
        
        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
