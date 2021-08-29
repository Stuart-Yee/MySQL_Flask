from flask import Flask, render_template, request, redirect
from user import User
from datetime import datetime

app=Flask(__name__)



@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    users = User.get_all()
    for user in users:
        print(user.created_at)
        print(type(user.created_at))
    return render_template("index.html", users=users)

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/new/create", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
        }
    User.add_user(data)

    return redirect("/users")

if __name__=="__main__":
    app.run(debug=True)

