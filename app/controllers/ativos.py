from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify
from flask_cors import cross_origin
from app.models.ativos import Ativo
from app.schemas.ativo import AtivoSchema, NovoAtivoSchema, ListaAtivosSchema, AtivoPathParams
from app.schemas.error import RespostaErroSchema
from app import db

ativo_tag = Tag(name="Ativo", description="Operações com ativos")

# Inicializando o Blueprint
ativos_bp = APIBlueprint(
    'ativos_bp',
    __name__,
    url_prefix='/ativos',
    abp_tags=[ativo_tag]
)

# Endpoint para CORS preflight OPTIONS
@ativos_bp.route('/', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def handle_options():
    return "", 204  # Retorna uma resposta 204 sem conteúdo, permitindo o preflight request

# Endpoint para listar todos os ativos
@ativos_bp.get(
    '/',
    summary="Lista todos os ativos",
    responses={200: ListaAtivosSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def listar_ativos():
    ativos = Ativo.query.all()
    data = [AtivoSchema.model_validate(a, from_attributes=True) for a in ativos]
    return jsonify([d.dict() for d in data]), 200

@ativos_bp.get(
    '/<int:id>',  # Defina a URL com o parâmetro id capturado da URL
    summary="Consulta um ativo específico",
    description="Recupera as informações de um ativo específico pelo seu ID."
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def consultar_ativo(path: AtivoPathParams):
    """
    Consulta um ativo específico pelo ID.
    """
    try:
        # Buscar o ativo pelo ID
        ativo_id = path.id
        ativo = Ativo.query.get(ativo_id)
        
        # Se não encontrar o ativo
        if not ativo:
            return jsonify({"mensagem": "Ativo não encontrado"}), 404

        # Retornar o ativo encontrado
        return jsonify(AtivoSchema.model_validate(ativo, from_attributes=True).dict()), 200

    except Exception as e:
        return jsonify({"mensagem": "Erro ao consultar ativo", "erro": str(e)}), 400

        
# Endpoint para criar um novo ativo
@ativos_bp.post(
    '/',
    summary="Cria um novo ativo",
    responses={201: AtivoSchema, 400: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def criar_ativo(body: NovoAtivoSchema):
    try:
        novo = Ativo(
            nome=body.nome,
            tipo=body.tipo,
            responsavel=body.responsavel,
            status=body.status,
            observacoes=body.observacoes
        )
        db.session.add(novo)
        db.session.commit()

        return jsonify(AtivoSchema.model_validate(novo, from_attributes=True).dict()), 201

    except Exception as e:
        return jsonify({"mensagem": "Erro ao criar ativo", "erro": str(e)}), 400


@ativos_bp.put(
    '/<int:id>',
    summary="Atualiza um ativo existente",
    responses={200: AtivoSchema, 400: RespostaErroSchema, 404: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def atualizar_ativo(path: AtivoPathParams, body: NovoAtivoSchema):
    """
    Atualiza as informações de um ativo existente pelo ID.
    """
    try:
        ativo_id = path.id
        ativo = Ativo.query.get(ativo_id)

        if not ativo:
            return jsonify({"mensagem": "Ativo não encontrado"}), 404

        # Atualizando os campos
        ativo.nome = body.nome
        ativo.tipo = body.tipo
        ativo.responsavel = body.responsavel
        ativo.status = body.status
        ativo.observacoes = body.observacoes

        db.session.commit()

        return jsonify(AtivoSchema.model_validate(ativo, from_attributes=True).dict()), 200

    except Exception as e:
        return jsonify({"mensagem": "Erro ao atualizar ativo", "erro": str(e)}), 400
