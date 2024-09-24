# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...") #prints out the string in terminal
    print(__name__)                   #prints out _main_ in terminal
    return "No hablo queso!"

app.debug = True                      #opens debugger in terminal
app.run()
