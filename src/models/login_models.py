from src import db


#Define a classe Login, que representa uma tabela no banco de dados
class Login(db.Model):

    #Define o nome da tabela no banco como 'tb_login'
    __tablename__ = 'tb_login'

    #Define a coluna 'id' como um inteiro, chave primária e auto-incrementável
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #Define a coluna 'email' como uma string de até 120 caracteres, não pode ser nula
    email = db.Column(db.String(120), nullable=False)
    
    #Define a coluna 'senha' (senha em português) como uma string de até 120 caracteres, não pode ser nula
    senha = db.Column(db.String(120), nullable=False)
