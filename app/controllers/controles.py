from flask import  request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag, APIBlueprint
from app.models.controle import Controle
from app import db
from app.models.controle import Controle
from app.schemas.controles import *
from app.schemas.error import *


controles_bp = APIBlueprint('controles', __name__,url_prefix='/controles')

controle_tag = Tag(name="Controles", description="Gerenciamento de controles da organização.")

@controles_bp.post('/', tags=[controle_tag], responses={"201": ControleSchema, "400": RespostaErroSchema})
def create_controle(form: NovoControleSchema):
    data = request.get_json()
    novo_controle = Controle(
        descricao=data['descricao'],
        categoria=data['categoria'],
        codigo=data['codigo'],
        anotacoes=data.get('anotacoes', None)
    )
    db.session.add(novo_controle)
    db.session.commit()
    return jsonify({'message': 'Controle criado com sucesso!'}), 201

@controles_bp.get('/', tags=[controle_tag],  responses={"200": NovoControleSchema, "404": RespostaErroSchema})
def list_controles(query: ControleSchema):
    controles = Controle.query.all()
    controles_data = [{
        'id': controle.id,
        'descricao': controle.descricao,
        'categoria': controle.categoria,
        'codigo': controle.codigo,
        'anotacoes': controle.anotacoes,
        'data_hora_alteracao': controle.data_hora_alteracao
    } for controle in controles]
    return jsonify(controles_data), 200


@controles_bp.delete('/<int:id>', tags=[controle_tag],responses={"200": {"description": "Controle removido com sucesso"}, "404": RespostaErroSchema})
def delete_controle(id):
    """
    Remove um controle pelo ID.
    """
    controle = Controle.query.get(id)  # Busca o controle pelo ID
    if not controle:
        return jsonify({'error': 'Controle não encontrado'}), 404

    db.session.delete(controle)  # Remove o controle
    db.session.commit()  # Salva as alterações no banco de dados

    return jsonify({'message': 'Controle removido com sucesso!'}), 200
