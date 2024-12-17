from flask import Blueprint, jsonify, request
from app.models.ativos import Ativo
from app.models.controle import Controle
from app.models.conformidade import Conformidade
from app import db

conformidade_bp = Blueprint('conformidade', __name__)

@conformidade_bp.route('/status', methods=['GET'])
def get_conformidade_status():
    """
    Retorna o relatório de conformidade com opção de filtro por status.
    ---
    parameters:
      - name: status
        in: query
        type: string
        required: false
        description: Filtra os resultados pelo status de conformidade (Implementado ou Não Pendente)
    responses:
      200:
        description: Lista de conformidades com ativos e controles associados.
        schema:
          type: array
          items:
            type: object
            properties:
              ativo:
                type: string
                description: Nome do ativo
                example: "Servidor Principal"
              controle:
                type: string
                description: Descrição do controle
                example: "Backup Diário"
              status:
                type: string
                description: Status de conformidade (Implemetado ou Não Pendente)
                example: "Implementado"
    """
    status_filtro = request.args.get('status')  # Obtém o filtro de status da query string

    # Base da query
    query = db.session.query(
        Ativo.nome.label("ativo"),
        Controle.descricao.label("controle"),
        Conformidade.status.label("status")
    ).join(
        Conformidade, Ativo.id == Conformidade.ativo_id
    ).join(
        Controle, Controle.id == Conformidade.controle_id
    )

    # Aplica o filtro, se fornecido
    if status_filtro:
        query = query.filter(Conformidade.status == status_filtro)

    # Executa a query e converte os resultados
    resultado = [
        {
            "ativo": row.ativo,
            "controle": row.controle,
            "status": row.status
        }
        for row in query
    ]

    return jsonify(resultado), 200


conformidade_bp.route('/conformidade/status', methods=['GET'])
def relatorio_conformidade():
    """
    Retorna o relatório de conformidade com opção de filtro por status.
    ---
    parameters:
      - name: status
        in: query
        type: string
        required: false
        description: Filtro de status (Implementado, Pendente)
    responses:
      200:
        description: Relatório de conformidade
    """
    # Obtém o filtro de status da query string
    status_filtro = request.args.get('status')

    # Query base com joins
    query = db.session.query(
        Ativo.nome.label("ativo"),
        Controle.descricao.label("controle"),
        Conformidade.status.label("status")
    ).join(
        Conformidade, Ativo.id == Conformidade.ativo_id
    ).join(
        Controle, Controle.id == Conformidade.controle_id
    )

    # Aplica o filtro, se fornecido
    if status_filtro:
        query = query.filter(Conformidade.status == status_filtro)

    # Executa a query e converte o resultado
    resultado = [
        {
            "ativo": row.ativo,
            "controle": row.controle,
            "status": row.status
        }
        for row in query
    ]

    return jsonify(resultado), 200

@conformidade_bp.route('/conformidade', methods=['POST'])
def cadastrar_conformidade():
    dados = request.json

    ativo_id = dados.get("ativo_id")
    controle_id = dados.get("controle_id")
    status = dados.get("status", "Pendente")

    if not ativo_id or not controle_id:
        return jsonify({"erro": "Campos 'ativo_id' e 'controle_id' são obrigatórios"}), 400

    # Valida existência do ativo e controle
    ativo = Ativo.query.get(ativo_id)
    if not ativo:
        return jsonify({"erro": "Ativo não encontrado"}), 404

    controle = Controle.query.get(controle_id)
    if not controle:
        return jsonify({"erro": "Controle não encontrado"}), 404

    # Verifica duplicidade
    conformidade_existente = Conformidade.query.filter_by(ativo_id=ativo_id, controle_id=controle_id).first()
    if conformidade_existente:
        return jsonify({"erro": "Essa conformidade já existe"}), 400


@conformidade_bp.route('/conformidade/<int:ativo_id>/<int:controle_id>', methods=['DELETE'])
def remover_conformidade(ativo_id, controle_id):
    """
    Remove uma relação de conformidade entre ativo e controle.
    """
    conformidade = Conformidade.query.filter_by(ativo_id=ativo_id, controle_id=controle_id).first()

    if not conformidade:
        return jsonify({"erro": "Conformidade não encontrada"}), 404

    db.session.delete(conformidade)
    db.session.commit()

    return jsonify({"mensagem": "Conformidade removida com sucesso"}), 200

@conformidade_bp.route('/conformidade/<int:ativo_id>/<int:controle_id>', methods=['PUT'])
def atualizar_conformidade(ativo_id, controle_id):
    """
    Atualiza uma relação de conformidade existente entre ativo e controle.
    """
    dados = request.json
    conformidade = Conformidade.query.filter_by(ativo_id=ativo_id, controle_id=controle_id).first()

    if not conformidade:
        return jsonify({"erro": "Conformidade não encontrada"}), 404

    # Atualiza o status se fornecido
    conformidade.status = dados.get("status", conformidade.status)
    db.session.commit()

    return jsonify({"mensagem": "Conformidade atualizada com sucesso"}), 200
