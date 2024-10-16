# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

# DEMO
# basics of /static folder
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return render_template( 'index.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
