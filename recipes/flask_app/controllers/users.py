from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users/new", methods=["POST"])
def new_user():
    #todo validate user, save user, login user, redirect to dashboard
    #todo if not valid, redirect back to login page
    return redirect("/")

@app.route("/users/login", methods=["POST"])
def login_user():
    #todo validate credentials and if valid redirect to /dashboard
    #todo if not valid, redirect back to index
    return redirect("/")
