#Kyle Lee
#50_Ls (Kyle, Kevin)
#SoftDev
#K7 -- Reading csv Files
#2024-09-18
#time spent: .75

import random
import csv
def Program(): 
    with open('occupations.csv', "r") as file: #Don't have to close
        csvFile = csv.reader(file)
        info = {}
        count = 0
        rando_number = random.randint(0,998) #Get a random number in scale with job percentages such that there are no decimals 
        total = 0
        for lines in csvFile:
            if not(count == 0):
                if (total > rando_number): #If we gone above the desired value from this step, this means that we reached our desired job
                    print(lines[0])
                    return(lines[0])
                else:
                    total += (float(lines[1])*10)
                info.update({lines[0]:float(lines[1])}) #Add to dictionary
            count = count + 1
        info.popitem()
Program()
