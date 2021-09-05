from flask import Flask, flash, session, get_flashed_messages
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:

    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # return a list of all emails fromt eh database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("emails_to_validate").query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    #created one email
    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL("emails_to_validate").query_db(query, data)

    @classmethod
    def get_email_by_id(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL("emails_to_validate").query_db(query, data)
        email = cls(results[0])
        return email

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            print("writing error to flash")
            flash("Invalid email, please try again", "email")
            # messages = get_flashed_messages(category_filter=["email"])
            #for m in messages:
                # print(m)
            is_valid = False
        return is_valid