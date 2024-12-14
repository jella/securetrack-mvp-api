from flask import Blueprint, request, jsonify
from app import db
from app.models.controle import Controle

controles_bp = Blueprint('controles', __name__)

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