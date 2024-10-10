# Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import csv, random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"



def readerocc():
    with open("data/occupations.csv", "r") as file: #Don't have to close
        csvFile = csv.reader(file)
        info = {}
        count = 0
        rando_number = random.randint(0,998)
        total = 0
        x = ""
        for lines in csvFile:
            if not(count == 0):
                info.update({lines[0]:float(lines[1])}) #Add to dictionary
            count = count + 1
        info.popitem()
        return info
def linkjobs(f):
    with open(f, "r") as file: #Don't have to close
        csvFile = csv.reader(file)
        data = []
        for lines in csvFile:
            if lines[2] == "Link":
                continue
            data.append(lines[2])
        return data
def randomoccupation():
    occupations = readerocc()
    x = ""
    rando_number = random.randint(0,998)
    total = 0
    count = 0
    listoccupations = []
    for z in occupations:
        listoccupations.append(z)
    for i in occupations.values():
        if (total > rando_number):
            x = listoccupations[count]
        else:
            total += i*10
            count+=1
    return x

@app.route("/wdywtbwygp")
def test_tmplt():
    #starts the table
    occupations = readerocc()
    occupationlink = linkjobs("data/occupations.csv")
    listoccupations = []
    percentoccupations = []
    linkoccupations = []
    tableoccupations = []
    tableoccupations.append("<table>")
    rando = randomoccupation()
    count = 0
    for z in occupations:
        listoccupations.append("<tr> <td>" + z + "</td>")
        count+=1
    for i in occupations.values():
        percentoccupations.append("<td>" + str(i) + "</td>")
    for m in occupationlink:
        linkoccupations.append("<td>" + m + "</td> </tr>")
    for x in range(count):
        tableoccupations.append(listoccupations[x])
        tableoccupations.append(percentoccupations[x])
        tableoccupations.append(linkoccupations[x])
    tableoccupations.append("</table>")    
    return render_template('tablified.html', foo="randomTableOccupations", oogada= "Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK", boogada=rando, collection=tableoccupations)


if __name__ == "__main__":
    app.debug = True
    app.run()
