from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models.recipe import Recipe

@app.route("/dashboard")
def dashboard():
    if session["logged_in"]:
        recipes = Recipe.get_all()
        return render_template("dashboard.html", recipes = recipes)
    else:
        return redirect("/")

@app.route("/recipes/new", methods=["POST", "GET"])
def create_recipe():
    if session["logged_in"] == False | session["logged_in"] == None:
        return redirect("/")
    if request.method == "GET":
        return render_template("save_recipe.html")
    elif request.method == "POST":
        if not Recipe.validate_recipe(request.form):
            return redirect("/recipes/new")
        else:
            new_id = Recipe.create_recipe(redirect.form)
            return redirect(f"/recipes/{new_id}")
    else:
        return "I'm sorry, that request method isn't allowed."


@app.route("/recipes/<int:recipe_id>")
def show_recipe():
    #todo show recipe
    pass
    return render_template("show_recipe.html")

@app.route("/recipes/edit/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe():
    # todo if session["user_id"] != # todo get recipe user id
        #return redirect("/logout")
    if request.method == "GET":
        # todo get recipe from id and pass into edit page
        return("save_recipe.html")
    elif request.method == "POST":
        # todo save recipe in database
        return redirect(f"/recipes/{recipe_id}")
    else:
        return "I'm sorry, that request method isn't allowed"

@app.route("/recipes/delete/<int:recipe_id>", methods=["POST"])
def delete_recipe():
    # todo if session["user_id"] != # todo get recipe user id
        #return redirect("/logout")
    # todo delete method for recipe
    return redirect("/dashboard")