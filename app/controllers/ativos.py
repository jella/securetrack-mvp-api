from flask import Blueprint, request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag , APIBlueprint 
from app import db
from app.models.ativos import Ativo

ativos_bp = APIBlueprint ('ativos', __name__,url_prefix='/ativos')
# Tags para a documentação
ativo_tag = Tag(name="Ativos", description="Gerenciamento de ativos da organização.")

@ativos_bp.route('/', methods=['POST'])
def create_ativo():
    
    data = request.get_json()
    novo_ativo = Ativo(
        nome=data['nome'],
        tipo=data['tipo'],
        responsavel=data['responsavel'],
        observacoes=data.get('observacoes', None),
        status=data['status']
    )
    db.session.add(novo_ativo)
    db.session.commit()
    return jsonify({'message': 'Ativo criado com sucesso!'}), 201

@ativos_bp.route('/', methods=['GET'])
def list_ativos():
    ativos = Ativo.query.all()
    ativos_data = [{
        'id': ativo.id,
        'nome': ativo.nome,
        'tipo': ativo.tipo,
        'responsavel': ativo.responsavel,
        'observacoes': ativo.observacoes,
        'status': ativo.status,
        'data_hora_alteracao': ativo.data_hora_alteracao
    } for ativo in ativos]
    return jsonify(ativos_data), 200

@ativos_bp.route('/<int:id>', methods=['GET'])
def get_ativo(id):
    """
    Retorna os detalhes de um ativo pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do ativo a ser retornado
    responses:
      200:
        description: Detalhes do ativo
      404:
        description: Ativo não encontrado
    """
    ativo = Ativo.query.get(id)  # Busca o ativo pelo ID
    if not ativo:
        return jsonify({'error': 'Ativo não encontrado'}), 404

    ativo_data = {
        'id': ativo.id,
        'nome': ativo.nome,
        'tipo': ativo.tipo,
        'responsavel': ativo.responsavel,
        'observacoes': ativo.observacoes,
        'status': ativo.status,
        'data_hora_alteracao': ativo.data_hora_alteracao
    }
    return jsonify(ativo_data), 200


@ativos_bp.route('/<int:id>', methods=['DELETE'])
def delete_ativo(id):
    """
    Remove um ativo pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do ativo a ser removido
    responses:
      200:
        description: Ativo removido com sucesso
      404:
        description: Ativo não encontrado
    """
    ativo = Ativo.query.get(id)  # Busca o ativo pelo ID
    if not ativo:
        return jsonify({'error': 'Ativo não encontrado'}), 404

    db.session.delete(ativo)  # Remove o ativo
    db.session.commit()  # Confirma a transação

    return jsonify({'message': 'Ativo removido com sucesso'}), 200
