from app import db, app

class User(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome = db.Column(db.String())
    username = db.Column(db.String())
    senha = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, nome, username, senha, email):
        self.id = id
        self.nome = nome
        self.username = username
        self.senha = senha
        self.email = email
    
class Estudante(db.Model):
    id = db.Column(db.String(), primary_key=True)
    escolaridade = db.Column(db.String())
    cursos = db.Column(db.String())
    certificados = db.Column(db.String())

    def __init__(self, id, escolaridade, cursos, certificados):
        self.id = id
        self.escolaridade = escolaridade
        self.cursos = cursos
        self.certificados = certificados

class Recrutador(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome_empresa = db.Column(db.String())
    cnpj_empresa = db.Column(db.String())
    cargo = db.Column(db.String())
    areas_interesse = db.Column(db.String())

    def __init__(self, id, nome_empresa, cnpj_empresa, cargo, areas_interesse):
        self.id = id 
        self.nome_empresa = nome_empresa
        self.cnpj_empresa = cnpj_empresa
        self.cargo = cargo
        self.areas_interesse = areas_interesse

class Certificado(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome = db.Column(db.String())
    carga_horaria = db.Column(db.String())
    provedor = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, id, nome, carga_horaria, provedor, link):
        self.id = id 
        self.nome = nome 
        self.carga_horaria = carga_horaria
        self.provedor = provedor 
        self.link = link
    
with app.app_context():
    db.create_all()  # Cria as tabelas definidas nos modelos
