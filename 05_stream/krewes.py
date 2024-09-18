#Kyle Lee
#K^3 (Kyle, Suhana, Vedant)
#SoftDev
#K6 -- Reading Files
#2024-09-18
#time spent: .75

import random
with open("krewes.txt", "r") as file:
    f = file.read()
tuples = f.split("@@@")
devos = []
for tuple in tuples:
    info = tuple.split("$$$")
    if len(info) == 3:
        period, devo, ducky = info
        devos.append({'period': period, 'devo': devo, 'ducky': ducky})
if devos:
    random_devo = random.choice(devos)
    print(f"Devo: {random_devo['devo']}, Period: {random_devo['period']}, Ducky: {random_devo['ducky']}")
else:
        print("No devos found.")