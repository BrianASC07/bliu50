#<Brian> <Liu>
#<31>
#SoftDev
#K<08> -- <{building the cradle>
#<2024>-<09>-<23>
#time spent: <0.5 hrs>

'''
DISCO:
<note any discoveries you made here... no matter how small!>
#Flask is used to create the website
#runs locally
#running the script from thonny doesnt work
#print() always prints out _main_
QCC:
0. what is 'name' and where does it come from/what is it used for?
1. what does app.route() do? why does the website break when its removed?
2. does app.run() run all the functions? where is hello_world() called in the code?
3. why does print(_name_) print out _main_?
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
#We looked through the script and tried running the program to see what happens
#We then commented out/changed certain lines/variables to see what would happen to the page

from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? A: similar to creating a class/object in Java

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? A: '/' might mean the root directory
def hello_world():
    print(hi)                      # Q2: Where will this print to? Q3: What will it print? A: it outputs _main_ in the terminal when the website is created
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? A: it appears the text when I run the webpage

app.run()                                # Q5: Where have you seen similar constructs in other languages? A: Similar to accessing a method in an object in java