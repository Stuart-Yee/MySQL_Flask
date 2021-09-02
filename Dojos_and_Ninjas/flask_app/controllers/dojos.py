from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()

    return render_template("dojo.html", dojos=dojos)

@app.route("/dojos/new", methods=["POST"])
def create_dojo():
    data = {"dojo_name" : request.form["dojo"]}
    row = Dojo.save(data)
    print(row)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {"dojo_id" : id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_dojo.html", dojo=dojo)