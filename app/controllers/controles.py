from flask import  request, jsonify
from flask_openapi3 import APIBlueprint, Tag
from app.models.controle import Controle
from app import db

controles_bp = APIBlueprint('controles', __name__,url_prefix='/controles')

controle_tag = Tag(name="Controles", description="Gerenciamento de controles da organização.")

@controles_bp.route('/', methods=['POST'])
def create_controle():
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

@controles_bp.route('/', methods=['GET'])
def list_controles():
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


@controles_bp.route('/<int:id>', methods=['DELETE'])
def delete_controle(id):
    """
    Remove um controle pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do controle a ser removido
    responses:
      200:
        description: Controle removido com sucesso
      404:
        description: Controle não encontrado
    """
    controle = Controle.query.get(id)  # Busca o controle pelo ID
    if not controle:
        return jsonify({'error': 'Controle não encontrado'}), 404

    db.session.delete(controle)  # Remove o controle
    db.session.commit()  # Salva as alterações no banco de dados

    return jsonify({'message': 'Controle removido com sucesso!'}), 200
