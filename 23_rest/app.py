# Halls Relief
#SoftDev
#K20 - Foundation CSS Tutorial
#2024-11-13
#time spent: 1.5

from flask import Flask, render_template, url_for, session, request, redirect
import os, json
import urllib.request

app = Flask(__name__)

app.secret_key = os.urandom(32)

API_KEY = "Rn8ocxR2ed7XDx4l35PektxNByKYhG3beJv96YLe"
@app.route("/", methods=['GET', 'POST'])
def main():
    data = urllib.request.urlopen(f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0")
    w = data.read()
    print(w)
    return render_template('main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()