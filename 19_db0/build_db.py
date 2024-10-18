#Brian liu Team 45
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

#QCC: what is integer primary key? how does it differ from just using int? why can't I have more than one integer primary key

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
c.execute("CREATE TABLE students (name TEXT, age int, id int)")
with open("students.csv", newline='') as studentscsv:
    reader = csv.DictReader(studentscsv) #reads file
    for row in reader:
        command = "(" + row["name"] + ", " + str(row["age"]) + ", " + str(row["id"]) + ")"
        c.execute("INSERT INTO students VALUES " + command)

c.execute("CREATE TABLE courses (st TEXT, mark int, id int)")
with open("courses.csv", newline='') as coursescsv:
    reader = csv.DictReader(coursescsv) #reads file
    for row in reader:
        command = "(" + row["st"] + ", " + str(row["mark"]) + ", " + str(row["id"]) + ")"
        c.execute("INSERT INTO courses VALUES " + command)
        
#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
