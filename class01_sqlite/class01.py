# CREATING DATABSE 01
import sqlite3

database = sqlite3.connect("class01.db")
cursor_class01 = database.cursor()
#cursor_class01.execute(
#"CREATE TABLE pessoas (nome text, idade integer, email text)")
#cursor_class01.execute(
#    "INSERT INTO pessoas VALUES('Athos', 17, 'athos@gmail.com')"
#)
database.commit()