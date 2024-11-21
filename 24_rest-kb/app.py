# Halls Relief
#SoftDev
#K23 - APIs
#2024-11-20
#time spent: 0.3

#Disco

#QCC


from flask import Flask, render_template
import json, os
import urllib.request

app = Flask(__name__)
app.secret_key = os.urandom(32)

#gets API key from text file
API_KEY = open('key.txt','r').read()

@app.route("/", methods=['GET', 'POST'])
def main():
    data = urllib.request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")     #returns object using the link with properties url, headers, and status
    d = json.loads(data.read())     #returns source code and converts it into a python dict
    desc = d.get("explanation")     #get values from dict 
    image = d.get("hdurl")
    return render_template('main.html', desc=desc, image=image)

if __name__ == "__main__":
    app.debug = True
    app.run()

#requests.get()
#requests.get().json()
#requests.urlopen()
#json.loads()
#json.dumps()
