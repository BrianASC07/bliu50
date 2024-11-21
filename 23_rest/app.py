# Halls Relief
#SoftDev
#K23 - APIs
#2024-11-20
#time spent: 1.0

from flask import Flask, render_template, url_for, session, request, redirect
import os, json
import urllib.request

app = Flask(__name__)

app.secret_key = os.urandom(32)

API_KEY = open('key_nasa.txt','r').read()
@app.route("/", methods=['GET', 'POST'])
def main():
    data = urllib.request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
    w = data.read()
    print(w)
    return render_template('main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()