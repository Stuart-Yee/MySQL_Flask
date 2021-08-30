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
    id = User.add_user(data)
    return redirect(f"/users/{id}")

@app.route("/users/<int:id>")
def show_user(id):
    data = {"id": id}
    user = User.get_by_id(data)
    return render_template("show_user.html", user=user)

@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {"id": id}
    User.delete_by_id(data)
    return redirect("/users")

@app.route("/users/<int:id>/edit", methods=["GET", "POST"])
def edit_user(id):
    if request.method == "GET":
        data = {"id": id}
        user = User.get_by_id(data)
        return render_template("edit_user.html", user=user)
    elif request.method == "POST":
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"],
            "id" : id
        }
        User.edit_user(data)

        return redirect(f"/users/{id}")
    else:
        return redirect("/")