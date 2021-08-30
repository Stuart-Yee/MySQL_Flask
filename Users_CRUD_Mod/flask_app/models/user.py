# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# burger.py

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW())"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query ="SELECT * FROM users WHERE %(id)s = id;"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result[0]

    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        connectToMySQL('users_schema').query_db(query, data)

