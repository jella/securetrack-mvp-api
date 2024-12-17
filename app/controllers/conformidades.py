from flask import request, jsonify
from flask_openapi3 import APIBlueprint, Tag
from app.models.ativos import Ativo
from app.models.controle import Controle
from app.models.conformidade import Conformidade

from app import db

conformidade_bp = APIBlueprint('conformidade', __name__, url_prefix='/conformidades')

conformidade_tag = Tag(name="Conformidade", description="Gerenciamento de conformidades entre ativos e controles.")

@conformidade_bp.get('/status', tags=[conformidade_tag])
def get_conformidade_status():
    status_filtro = request.args.get('status')
    query = db.session.query(
        Ativo.nome.label("ativo"),
        Controle.descricao.label("controle"),
        Conformidade.status.label("status")
    ).join(Conformidade, Ativo.id == Conformidade.ativo_id).join(Controle, Controle.id == Conformidade.controle_id)
    if status_filtro:
        query = query.filter(Conformidade.status == status_filtro)
    resultado = [{"ativo": row.ativo, "controle": row.controle, "status": row.status} for row in query]
    return jsonify(resultado), 200

@conformidade_bp.post('/', tags=[conformidade_tag])
def cadastrar_conformidade():
    """
    Cadastra uma nova conformidade.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [ativo_id, controle_id]
            properties:
              ativo_id: {type: integer}
              controle_id: {type: integer}
              status: {type: string, default: Pendente}
    responses:
      201:
        description: Conformidade criada.
      400:
        description: Erro ao cadastrar conformidade.
    """
    dados = request.json
    ativo = Ativo.query.get(dados["ativo_id"])
    controle = Controle.query.get(dados["controle_id"])
    if not ativo or not controle:
        return jsonify({"erro": "Ativo ou controle não encontrado"}), 404
    conformidade_existente = Conformidade.query.filter_by(ativo_id=ativo.id, controle_id=controle.id).first()
    if conformidade_existente:
        return jsonify({"erro": "Conformidade já existe"}), 400
    nova_conformidade = Conformidade(ativo_id=ativo.id, controle_id=controle.id, status=dados.get("status", "Pendente"))
    db.session.add(nova_conformidade)
    db.session.commit()
    return jsonify({"mensagem": "Conformidade cadastrada com sucesso!"}), 201

@conformidade_bp.delete('/<int:ativo_id>/<int:controle_id>', tags=[conformidade_tag])
def remover_conformidade(ativo_id, controle_id):
    """
    Remove uma conformidade existente.
    ---
    parameters:
      - in: path
        name: ativo_id
        schema: {type: integer}
      - in: path
        name: controle_id
        schema: {type: integer}
    responses:
      200:
        description: Conformidade removida.
      404:
        description: Conformidade não encontrada.
    """
    conformidade = Conformidade.query.filter_by(ativo_id=ativo_id, controle_id=controle_id).first()
    if not conformidade:
        return jsonify({"erro": "Conformidade não encontrada"}), 404
    db.session.delete(conformidade)
    db.session.commit()
    return jsonify({"mensagem": "Conformidade removida com sucesso!"}), 200
