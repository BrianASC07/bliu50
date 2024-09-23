# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # imports flash and creates an instance of flask

@app.route("/")                # assigns fxn to root
def hello_world():
    print(__name__)            # prints ut  
    return "No hablo queso!"   

app.run()                      # runs app in localhost
                
