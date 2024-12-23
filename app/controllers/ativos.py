from flask import Blueprint, request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag, APIBlueprint
from app import db
from app.models.ativos import Ativo
from app.schemas.ativo import *
from app.schemas.error import *



# Tags para a documentação
ativo_tag = Tag(name="Ativos", description="Gerenciamento de ativos da organização.")

ativos_bp = APIBlueprint('ativos', __name__, url_prefix='/ativos')

@ativos_bp.post('/', tags=[ativo_tag], responses={"200": NovoAtivoSchema, "409": RespostaErroSchema, "400": RespostaErroSchema})
def create_ativo(form: NovoAtivoSchema):
    """
      Cria um novo ativo na organização.
    """
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
    return jsonify({'message': 'Ativo criado com sucesso!','error':201}), 201

@ativos_bp.get('/', tags=[ativo_tag], responses={"200": NovoAtivoSchema, "404": RespostaErroSchema})
def list_ativos(query: AtivoSchema):
    """
    Lista todos os ativos cadastrados.
    """
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

@ativos_bp.get('/<int:id>', tags=[ativo_tag])
def get_ativo(id):
    """
    Retorna os detalhes de um ativo pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do ativo a ser retornado.
    responses:
      200:
        description: Detalhes do ativo.
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID do ativo.
                nome:
                  type: string
                  description: Nome do ativo.
                tipo:
                  type: string
                  description: Tipo do ativo.
                responsavel:
                  type: string
                  description: Nome do responsável pelo ativo.
                observacoes:
                  type: string
                  description: Observações adicionais sobre o ativo.
                status:
                  type: string
                  description: Status do ativo.
                data_hora_alteracao:
                  type: string
                  format: date-time
                  description: Data e hora da última alteração no ativo.
      404:
        description: Ativo não encontrado.
    """
    ativo = Ativo.query.get(id)
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

@ativos_bp.delete('/<int:id>', tags=[ativo_tag])
def delete_ativo(query: AtivoSchema):
    """
    Remove um ativo pelo ID.
    """
    ativo = Ativo.query.get(id)
    if not ativo:
        return jsonify({'error': 'Ativo não encontrado'}), 404

    db.session.delete(ativo)
    db.session.commit()

    return jsonify({'message': 'Ativo removido com sucesso'}), 200