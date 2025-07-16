import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
#cursor.execute('''
    #CREATE TABLE IF NOT EXISTS alunos (
       # id INTEGER PRIMARY KEY AUTOINCREMENT,
       # nome TEXT NOT NULL,
       # idade INTEGER,
       # nota REAL
    #)
#''')
while True:
    print("\n--- MENU ---")
    print("[1] Adicionar aluno")
    print("[2] Ver todos os alunos")
    print("[3] Atualizar nota de um aluno")
    print("[4] Remover aluno")
    print("[5] Sair")
    choose = input("Escolha uma opção: ")
    if choose == "1":
        name = str(input('Nome: '))
        age = int(input('Idade: '))
        grade = float(input('Nota: '))
        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
    elif choose == "2":
        for row in cursor.execute('select * from alunos'):
            print(row)
    elif choose == "3":
        try:
            id_student = int(input('ID ALuno'))
            new_grade = float(input('Nota: '))
            cursor.execute("UPDATE alunos SET nota = ? WHERE id = ?", (new_grade, id_student))
            conn.commit()
            if cursor.rowcount == 0:
                print('Nenhum Aluno com esse ID')
            else:
                print('Atualizado com Sucesso.')
        except ValueError:
            print('Entrada Errada')
    elif choose == "4":
        try:
            id_student = int(input('ID aluno: '))
            cursor.execute("DELETE FROM alunos WHERE id= ?", id_student)
            conn.commit()
            if cursor.rowcount == 0:
                print('\nNenhum Aluno Com Esse ID')
            else:
                print('\nAluno Removido')
        except ValueError:
            print('ID Inválido')
        
    elif choose == "5":
        break
    else:
        print("Opção inválida!")
conn.close()