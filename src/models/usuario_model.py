from src import db
from passlib.hash import pbkdf2_sha256 as cripto


#Define a classe Usuario, que representa uma tabela no banco de dados
class Usuario(db.Model):
    __tablename__ = 'tb_usuario'


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)


    #construtor da classea
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone


    #Método para gerar o hash da senha e armazená-la no atributo 'senha'
    def gen_senha(self, senha):
        self.senha = cripto.hash(senha)

    #Método para verificar se a senha fornecida corresponde ao hash armazenado
    def ver_senha(self, senha):
        return cripto.verify(senha, self.senha)
