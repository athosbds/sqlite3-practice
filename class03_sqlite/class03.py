# DELETING RECORDS 03
import sqlite3
try:
    database = sqlite3.connect("class01.db")
    cursor = database.cursor()
    cursor.execute("DELETE from pessoas WHERE idade = 17")
    database.commit()
    database.close()
    print("Dados Removidos.")
except sqlite3.Error as error:
    print(f'Erro ao Excluir: {error}')