from flask import Blueprint, request, jsonify
from app import db
from app.models.ativos import Ativo

ativos_bp = Blueprint('ativos', __name__)

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