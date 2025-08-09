from app import app, db, Usuario, Post

# Criar usuário
with app.app_context():
    usuario1 = Usuario(nome="Athos", email="athos@email.com")
    usuario2 = Usuario(nome="Maria", email="maria@email.com")
    db.session.add_all([usuario1, usuario2])
    db.session.commit()
    print("Usuários criados!")
with app.app_context():
    usuarios = Usuario.query.all()
    for u in usuarios:
        print(u.id, u.nome, u.email)