# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
import csv
import random

app = Flask(__name__)           #create instance of class Flask



with open("occupations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile) #reads file
    percentages = []
    occupations = []
    for row in reader:
        percentages.append(float(row['Percentage']))
        occupations.append(row['Job Class'])
        #random choices return a list, [:-1] to remove last line, k = size of outputted list
def chooseRandomOcc():
    return random.choices(occupations[:-1], weights = percentages[:-1], k = 1)[0]

@app.route("/")                 #assign fxn to route
def hello_world():
    output = "Trio name:<br>Anastasia, Mark, Brian<br>Random Occupation: " + chooseRandomOcc() + "<br>"
    print("the __name__ of this module is... ")
    print(__name__)
    for i in range(len(occupations)):
        output += "<br>" + occupations[i] + " (" + str(percentages[i]) + "%)" 
    return output



if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
