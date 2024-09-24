# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # imports flash and creates an instance of flask

@app.route("/")                # assigns fxn to root
def hello_world():
    print(__name__)            # prints out main in the terminal 
    return "No hablo queso!"   #displays the text on the webpage

app.run()                      # runs app in localhost
                
