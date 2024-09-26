'''
Sascha Gordon-Zolov, Kyle Lee, John (JAKS)
SoftDev
K09 -- Softserve -- Using Flask import to create a list with a randomly changing occupation
2024-09-24
time spent: 2 hours
'''

from flask import Flask # imports the flask command
import csv
import random

def randomSelec():
    def finalPage():
    page = "<h1>Sascha Gordon-Zolov, Kyle Lee, John (JAKS)</h1><br><h3>Occupations:<\h3><br>"
    with open("occupations.csv", "r") as file:
        next(file)
        f = csv.reader(file)
        dic = {}
        for i in f:
            dic.update({i[0]: float(i[1])})
        total = dic["Total"]
        key = dic.keys()
        for k in key:
            num = dic[k]
            if (num / total) > random.random(): #random.random generates a float in (0, 1)
                thing = k
            else:
                total -= num #Used for weighted probability; subtracts the probability from the total if the occupation is not chosen
    for stuff in dic.keys():
        page = page + stuff + "<br>"
    return page + "<br><h4>Random Occupation: " + thing + "</h4><br>"

app.run()