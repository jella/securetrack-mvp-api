from flask import Blueprint, jsonify
from app.models.conformidade import Conformidade

conformidade_bp = Blueprint('conformidade', __name__)

@conformidade_bp.route('/status', methods=['GET'])
def get_conformidade_status():
    conformidades = Conformidade.query.all()
    conformidades_data = [{
        'id': conformidade.id,
        'ativo_id': conformidade.ativo_id,
        'controle_id': conformidade.controle_id,
        'status': conformidade.status,
        'data_hora_alteracao': conformidade.data_hora_alteracao
    } for conformidade in conformidades]
    return jsonify(conformidades_data), 200