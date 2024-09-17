#<Brian> <Liu>
#<45>
#SoftDev
#K<05> -- <{bitstream/python file handling/practiced handling files in python and parsing string>
#<2024>-<09>-<17>
#time spent: <>

import random
#import and read file and store contents into variable text
file = open('krewes.txt')
text = file.read()

#split text to create an array 
text = text.split("@@@")
#remove last element cuz empty line
text.pop(len(text) - 1)

#for each devo in the text array, split on $, create a dict, and add it to array    
krewes = []
for devos in text:
    infoArray = devos.split("$$$")
    devoInfo = {"pd": int(infoArray[0]), "devo": infoArray[1], "ducky": infoArray[2]}
    krewes.append(devoInfo)

#random choose one from krewes array
randomDevo = krewes[random.randint(0,len(krewes) - 1)]
print(str(randomDevo.get("pd")) + " " + randomDevo.get("devo") + " " + randomDevo.get("ducky"))