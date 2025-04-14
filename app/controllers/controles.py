from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify, request
from flask_cors import cross_origin
from app.models.controles import Controle
from app.schemas.controles import ControleSchema, NovoControleSchema, ListaControlesSchema
from app.schemas.error import RespostaErroSchema
from app import db

controle_tag = Tag(name="Controle", descr1iption="Operações com controles")

controles_bp = APIBlueprint(
    'controles_bp',  # Nome único
    __name__,
    url_prefix='/controles',
    abp_tags=[controle_tag]
)


@controles_bp.route('/', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:8000",supports_credentials=True)
def handle_options():
    return "", 204  # Retorna uma resposta 204 sem conteúdo, permitindo o preflight request

# Endpoint para listar todos os controles
@controles_bp.get(
    '/',
    summary="Lista todos os controles",
    responses={200: ListaControlesSchema}  # Agora usando ListaControlesSchema
)
@cross_origin(origins="http://localhost:8000",supports_credentials=True)
def listar_controles():
    controles = Controle.query.all()
    data = [ControleSchema.from_orm(c).dict() for c in controles]
    return jsonify(data), 200

# Endpoint para criar um novo controle
@controles_bp.post(
    '/',
    summary="Cria um novo controle",
    responses={201: ControleSchema, 400: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def criar_controle(body: NovoControleSchema):
    try:
        # Criação de um novo controle
        novo_controle = Controle(
            descricao=body.descricao,
            categoria=body.categoria,
            codigo=body.codigo,
            anotacoes=body.anotacoes
        )
        db.session.add(novo_controle)
        db.session.commit()

        # Retorno do controle criado
        return jsonify(ControleSchema.from_orm(novo_controle).dict()), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Endpoint para excluir um controle
@controles_bp.route('/<int:id>', methods=["DELETE"], strict_slashes=False)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def delete_controle(id: int):
    controle = Controle.query.get(id)
    if not controle:
        return jsonify({"erro": "Controle não encontrado"}), 404
    db.session.delete(controle)
    db.session.commit()
    return jsonify({"mensagem": "Controle removido com sucesso!"}), 200
