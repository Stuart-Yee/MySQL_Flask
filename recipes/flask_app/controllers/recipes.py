from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app

@app.route("/dashboard")
def dashboard():
    #todo if logged in, pull in all recipes and render html
    #todo if not logged in, redirect to /
    return render_template("dashboard.html")