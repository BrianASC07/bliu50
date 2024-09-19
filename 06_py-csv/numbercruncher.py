#<Brian> <Liu>
#<31>
#SoftDev
#K<06> -- <{csv/handling csvs/read csvs and converted its data into a dictionary>
#<2024>-<09>-<19>
#time spent: <>

#DISCO: we can use dict reader to read a csv file into a dictionary. then we can iterate through it to extract values
#QCC:
#How this script works: iterating through d

import csv
import random

with open("occupations.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile) #reads file
    percentages = []
    occupations = []
    for row in reader:
        percentages.append(float(row['Percentage']))
        occupations.append(row['Job Class'])
        #random choices return a list, [:-1] to remove last line, k = size of outputted list
    print(random.choices(occupations[:-1], weights = percentages[:-1], k = 1)[0]) 

#