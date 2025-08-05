# INSERTING VALUES THROUGH VARIABLES 04
import sqlite3
name = "Athos"
age = "28"
email = "athosyu@gmail.com"

database = sqlite3.connect("class01.db")
cursor_database = database.cursor()
cursor_database.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
cursor_database.execute("INSERT INTO pessoas VALUES('"+name+"', "+str(age)+", '"+email+"')")
database.commit()