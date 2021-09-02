from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def create_ninja():
    dojos = Dojo.get_all()
    for dojo in dojos:
        print(dojo.name)
        print(dojo.id)

    return render_template("new_ninja.html", dojos=dojos)

@app.route("/ninjas/save", methods=["POST"])
def save_ninja():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "nage": request.form["age"],
        "dojo_num": request.form["dojo_id"]
    }

    dojo = request.form["dojo_id"]

    Ninja.create_ninja(data)
    return redirect(f"/dojos/{dojo}")