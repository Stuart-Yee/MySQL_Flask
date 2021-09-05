from flask import Flask, render_template, redirect, session, flash, request, get_flashed_messages
from flask_app import app
from flask_app.models.email import Email

@app.route("/")
def index():
    print("getting those flashed messages...")
    messages = get_flashed_messages()
    for m in messages:
        print(m, "from controller")
    return render_template("index.html")

@app.route("/email/save", methods=["POST"])
def save_email():
    if not Email.validate_email(request.form):
        print("Email fail!")
        # messages = get_flashed_messages(category_filter=["email"])
        # for m in messages:
            #print(m, "from controller after save_email")
        return redirect("/")
    else:
        session["heyo"] = "hiya!"
        data ={"id": Email.create_email(request.form)}
        email = Email.get_email_by_id(data).email
        flash(email, "success")
        return redirect("/success")

@app.route("/success")
def success():
    emails = Email.get_all()
    return render_template("success.html", emails=emails)