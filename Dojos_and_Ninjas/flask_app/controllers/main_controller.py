from flask import Flask, redirect
from flask_app import app

@app.route("/")
def main_route():
    return redirect("/dojos")