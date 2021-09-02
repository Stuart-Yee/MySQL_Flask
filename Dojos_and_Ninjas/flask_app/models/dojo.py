from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at=["created_at"]
        self.updated_at=["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo)) #note to self, cls([args]) instantiates an object
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojo_name)s, NOW(), NOW());"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"],
                "dojo_id" : row["dojo_id"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo