from flask_restful import Resource
from marshmallow import ValidationError
from src.schemas import usuario_schema
from flask import request, jsonify, make_response
from src.services import usuario_services
from src import api
from src.models.usuario_model import Usuario

#POST, GET, PUT, DELETE

#Define um recurso RESTful para lidar com múltiplos usuários (lista de usuários)
class UsuarioList(Resource):

    #Método GET para listar todos os usuários
    def get(self):
        # Chama o serviço para buscar todos os usuários do banco
        usuarios = usuario_services.listar_usuario()

        #Se a lista de usuários estiver vazia (não encontrou nenhum)
        if not usuarios:
            return make_response(jsonify({"mensagem": "Não existe usuários"}))
        
        schema = usuario_schema.UsuarioSchema(many=True)

        return make_response(jsonify(schema.dump(usuarios)), 200)
    
    def post(self):
        schema = usuario_schema.UsuarioSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        if usuario_services.listar_usuario_email(dados('email')):
            return make_response(jsonify({'message':'Email já cadastrado!'}), 400)
        
        try:
            #criaçao de um novo usuario no banco
            novo_usuario = Usuario(
                nome = dados['nome'],
                email = dados['email'],
                senha = dados['senha'],
                telefone = dados['telefone']
            )
            resultado = usuario_services.cadastrar_usuario(novo_usuario)
            return make_response(jsonify(schema.dump(resultado)), 201)
        

        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(UsuarioList, '/usuario')