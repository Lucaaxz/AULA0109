from src import ma
from src.models import usuario_model
from marshmallow import fields


#Define o schema para serialização e desserialização da classe Usuario
class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario

        #Define explicitamente os campos que serão incluídos na serialização/desserialização
        fields = ('id', 'nome', 'email', 'senha', 'telefone')

    #Define que esses campos são obrigatórios para validação na desserialização (ex: no POST)
    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    telefone = fields.String(required=True)
