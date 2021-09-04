from flask import Flask, render_template, request, session, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    #options stored locally as lists but can later be migrated to the database
    languages=["C#", "C++", "Python", "Java", "JavaScript", "Ruby"]
    locations=["San Jose", "Seattle", "Chicago", "Burbank", "Remote"]

    return render_template("index.html", languages=languages, locations=locations)

#The purpose of this method is to capture form data and enter into database
@app.route("/capture", methods=["POST"])
def form_capture():
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"]
    }
    #Want to capture the new id upon creation
    if Dojo.validate_dojo(request.form):
        new_id = Dojo.create_dojo(data)

        #Using new id to navigate to results page
        return redirect("/result/" + str(new_id))
    else:
        return redirect("/")

@app.route("/result/<int:id>")
def landing(id):
    data = {"id": id}
    dojo = Dojo.get_by_id(data)
    return render_template("landing.html", dojo=dojo)