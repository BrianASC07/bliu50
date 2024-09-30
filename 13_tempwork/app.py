#Team name: 45
# Members: Tahmin, Brian, Jady


from flask import Flask, render_template
import csv
import random


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

with open("data/occupations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile) #reads file
    percentages = []
    occupations = []
    for row in reader:
        percentages.append(float(row['Percentage']))
        occupations.append(row['Job Class'])
        #random choices return a list, [:-1] to remove last line, k = size of outputted list
        
def chooseRandomOcc():
    return random.choices(occupations[:-1], weights = percentages[:-1], k = 1)[0]
@app.route("/wdywtbwygp")
def test_tmplt():
    return render_template( 'tablified.html', foo="OCCUPATIONS", randocc=chooseRandomOcc(), per=percentages,occ=occupations)
