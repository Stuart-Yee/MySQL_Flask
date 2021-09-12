from flask import Flask, render_template, session, flash, redirect, request
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def registration():
    movies = [
        "Star Wars",
        "American Pie",
        "The Usual Suspects",
        "Gone With the Wind",
        "Wizard of Oz",
        "The Good, The Bad, The Ugly",
        "American Pie",
        "The Avengers",
        "Austin Powers",
        "Indiana Jones and the Temple of Doom"
    ]
    return render_template("registration.html", movies=movies)

@app.route("/login", methods=["POST"])
def login():
    login_attempt = request.form
    if User.validate_login(login_attempt):
        user = User.find_by_email(login_attempt)
        session["user_id"] = user.id
        session["logged_in"] = True
        session["user_name"] = user.first_name + " " + user.last_name
        return redirect("/success")
    else:
        return redirect("/")


@app.route("/users/new", methods = ["POST"])
def create_user():
    data = {}
    for key in request.form:
        data[key] = request.form[key]
    if "subscribed" in data:
        data["subscribed"] = True
    else:
        data["subscribed"] = False
    if not "fav_movie" in data:
        data["fav_movie"] = None



    if User.validate_registration(data):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data["password"] = pw_hash
        new_id = User.register_user(data)
        session["user_id"] = new_id
        session["logged_in"] = True
        session["user_name"] = data["first_name"] + " " + data["last_name"]
        return redirect("/success")

    return redirect("/register")

@app.route("/success")
def success():
    if session["logged_in"] == True:
        return render_template("success.html")
    else:
        return redirect("/")

@app.route("/logout", methods=["POST"])
def logout():
    session["user_id"] = None
    session["user_name"] = None
    session["logged_in"] = False
    return redirect("/")
