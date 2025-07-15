# UPDATE DATA 05
import sqlite3
database = sqlite3.connect("class01.db")
cursor_database = database.cursor()
cursor_database.execute("UPDATE pessoas SET nome = 'Barbosa' WHERE idade = 28")
database.commit()