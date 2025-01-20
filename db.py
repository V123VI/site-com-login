from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Inicializa o aplicativo Flask

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

  
    
   
    def mostrartudo():
        usuarios = Usuario.query.all()
        for u in usuarios:
            print(f'ID do usuario:{u.id} || nome: {u.nome} || Email: {u.email} || Senha: {u.senha}')

  
    def criar_usuario(nome, email, senha):
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        print(f'O usuario com o nome: { nome} foi criado com o email {email}.')

    def deletar_usuario(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            print('usuario deletado')
        else: 
            print('usuario nao encontrado ou erro na hora de deletar')



          

    
