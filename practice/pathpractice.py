from pathlib import Path
import os

server = open("server.py", "w+")
server.write(
"from flask_app import app\nfrom flask_app import #controllers go here\nif __name__==\"__main__\":\n\tapp.run(debug=True)"
)
server.close()
print("Current path:", Path.cwd())
Path("flask_app").mkdir()
os.chdir("flask_app")
Path("config").mkdir()
Path("controllers").mkdir()
Path("models").mkdir()
Path("static").mkdir()
Path("templates").mkdir()
module_file = open("__init__.py", "w+")
module_file.write(
"from flask import Flask\napp = Flask(__name__)\napp.secret_key = \"YOUR SECRET KEY\""
)

os.chdir("config")
mysql = open("mysqlconnection.py", "w+")
mysql.write(
"# a cursor is the object we use to interact with the database\nimport pymysql.cursors\n# this class will give us an instance of a connection to our database\nclass MySQLConnection:\n\tdef __init__(self, db):\n\t\t# change the user and password as needed\n\t\tconnection = pymysql.connect(host='localhost',\nuser='root',\npassword='root',\ndb=db,\ncharset='utf8mb4',\ncursorclass=pymysql.cursors.DictCursor,\nautocommit=True)\n\t\t# establish the connection to the database\n\t\tself.connection = connection\n\t# the method to query the database\n\t def query_db(self, query, data=None):\n\t\twith self.connection.cursor() as cursor:\n\t\t\ttry:\n\t\t\t\tquery = cursor.mogrify(query, data)\n\t\t\t\tprint(\"Running Query:\", query)\n\t\t\t\texecutable = cursor.execute(query, data)\n\t\t\t\tif query.lower().find(\"insert\") >= 0:\n\t\t\t\t\t# INSERT queries will return the ID NUMBER of the row inserted\n\t\t\t\t\tself.connection.commit()\n\t\t\t\t\treturn cursor.lastrowid\n\t\t\t\telif query.lower().find(\"select\") >= 0:\n\t\t\t\t\t# SELECT queries will return the data from the database as a LIST OF DICTIONARIES\n\t\t\t\t\tresult = cursor.fetchall()\n\t\t\t\t\treturn result\n\t\t\t\telse:\n\t\t\t\t\t# UPDATE and DELETE queries will return nothing\n\t\t\t\t\tself.connection.commit()\n\t\t\texcept Exception as e:\n\t\t\t\t# if the query fails the method will return FALSE\n\t\t\t\tprint(\"Something went wrong\", e)\n\t\t\t\treturn False\n\t\t\tfinally:\n\t\t\t\t# close the connection\n\t\t\t\tself.connection.close()\n\t\t\t\t# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection\ndef connectToMySQL(db):\n\treturn MySQLConnection(db)")
mysql.close()

module_file.close()