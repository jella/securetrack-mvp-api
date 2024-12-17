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
        description: Filtra os resultados pelo status de conformidade (Conforme ou Não Conforme)
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
        description: Filtro de status (Conforme, Não Conforme)
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

conformidade_bp.route('/conformidade', methods=['POST'])
def cadastrar_conformidade():
    """
    Cadastra uma nova relação de conformidade entre um ativo e um controle.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            ativo_id:
              type: integer
            controle_id:
              type: integer
            status:
              type: string
              enum: ["Implementado", "Pendente"]
              example: "Implementado"
    responses:
      201:
        description: Conformidade cadastrada com sucesso
    """
    dados = request.json

    # Valida os dados recebidos

    ativo_id = dados.get("ativo_id")
    controle_id = dados.get("controle_id")
    status = dados.get("status", "Pendente")  # Padrão: Pendente
    
    if not ativo_id or not controle_id:
        return jsonify({"erro": "Campos 'ativo_id' e 'controle_id' são obrigatórios"}), 400

    # Cria e salva a conformidade
    nova_conformidade = Conformidade(ativo_id=ativo_id, controle_id=controle_id, status=status)
    db.session.add(nova_conformidade)
    db.session.commit()

    return jsonify({"mensagem": "Conformidade cadastrada com sucesso"}), 201
