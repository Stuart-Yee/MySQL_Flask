from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        # id, name, location, language, comment, created_at and updated_at
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        dojo = cls(results[0])
        return dojo