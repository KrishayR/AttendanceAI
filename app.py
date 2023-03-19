from flask import Flask, render_template
from flask import request, jsonify
import requests
from bs4 import BeautifulSoup
from flask import Response, stream_with_context
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import pandas as pd
from flask import Blueprint, render_template
from replit import db, Database
from passlib.hash import sha256_crypt

app = Flask(__name__)

people = "Stephen Curry","Elon Musk","Jeff Bezos","Shah Rukh Khan","LeBron James","Barack Obama"



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500

@app.route('/data-stream')
def data_stream():
    def generate():
        with open('data.csv', 'r') as f:
            while True:
                data = f.read()
                print(data)
                if not data:
                    break
                yield data
    return Response(stream_with_context(generate()))

db = Database(db_url="https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzkyODc5NTYsImlhdCI6MTY3OTE3NjM1NiwiZGF0YWJhc2VfaWQiOiI5NTdhNzJkMi0wMmI5LTQ5YjYtOTU0Zi1kNGIxMjYwMjQzZmUiLCJ1c2VyIjoiTmVhbFBhdGFsYXkxIiwic2x1ZyI6IkF0dGVuZGFuY2VBSSJ9.imGXj1BiYGOX9mi2yYmrcnugIOKTgYCGGB8a1KJk4X1_DwfHL9SUyoxuQQrbe07cNojzkdvx9-x1WGvZSkA5DA")

@app.route("/")
def home():
    return render_template("index.html")

#test

@app.route("/signin")
def login():
  loggedIn = request.cookies.get("loggedIn")
  if loggedIn == "true":
    return redirect("/dashboard") 
  else:
    return render_template("signin.html")

@app.route("/signup")
def signup():
  loggedIn = request.cookies.get("loggedIn")
  if loggedIn == "true":
    return redirect("/dashboard")
  else:
    return render_template("getstarted.html")

@app.route("/loginsubmit", methods=["GET", "POST"])
def loginsubmit():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    if username in db.keys():
      if sha256_crypt.verify(password, db[username]) == True:
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie("loggedIn", "true")
        resp.set_cookie("username", username)
        return resp
      else:
        return render_template("error.html", error="Incorrect Password, please try again.")
    else:
      return render_template("error.html", error="Account does not exist, please sign up.")

@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
  if request.method == "POST":
    newusername = request.form.get("newusername")
    newpassword = sha256_crypt.encrypt((request.form.get("newpassword")))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    allchars = letters + cap_letters + numbers + ['_']
    print(newusername)
    for i in newusername:
      if i not in allchars:
        return "Username can only contain alphanumeric characters and underscores."
    if newusername in db.keys():
      return "Username taken."
    if newusername == "":
      return "Please enter a username."
    if newpassword == "":
      return "Please enter a password."
    db[newusername] = newpassword
    db[newusername+"stat"] = "user"
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie("loggedIn", "true")
    resp.set_cookie("username", newusername)
    return resp

@app.route("/logout")
def logout():
  resp = make_response(render_template('readcookie.html'))
  resp.set_cookie("loggedIn", "false")
  resp.set_cookie("username", "None")
  return resp

#iojasjdjkaskjdass

@app.route("/dashboard")
def dashboard():
    username = request.cookies.get("username")
    loggedIn = request.cookies.get("loggedIn")
    #55
    data = pd.read_csv("data.csv")
    first_names = [name.split()[0] for name in data.loc[:,"studentname"]]
    students = [(id, name, date, attendance) for id, name, date, attendance in zip(data.loc[:,"studentid"], data.loc[:,"studentname"], data.loc[:,"date"], data.loc[:,"attendance"])]
    #
    if loggedIn == "false":
        return render_template("index.html")
    else:
        return render_template("dashboard.html", username=username, students=students)
    
        

    

@app.route("/getstarted")
def getstarted():
    return render_template("getstarted.html")

@app.route("/index")
def index():
    return render_template("index.html")


#jasjnkdjnasjndjnasdjnkajknsd

if __name__ == "__main__":
    app.run(debug=True)