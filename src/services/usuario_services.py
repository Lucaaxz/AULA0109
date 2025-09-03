from ..models import usuario_model
from src import db
from ..schemas import usuario_schema

#Função para cadastrar um novo usuário no banco de dados
def cadastrar_usuario(usuario):
    #Cria uma nova instância do modelo Usuario com os dados fornecidos
    usuario_db = usuario_model.Usuario(
        nome = usuario.nome,
        email = usuario.email,  
        telefone = usuario.telefone
    )
    
    #Chama o método para criptografar a senha antes de salvar
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    
    db.session.commit()
    
    #Retorna o objeto usuário cadastrado (com id e outros dados atualizados)
    return usuario_db


#Função para listar todos os usuários cadastrados
def listar_usuario():
    #Executa uma consulta para obter todos os registros da tabela de usuários
    usuarios = usuario_model.Usuario.query.all()
    return usuarios


def listar_usuario_id():
    ...

def excluir_usuario():
    ...

def editar_usuario():
    ...

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()
