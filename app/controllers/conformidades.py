from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify, request
from flask_cors import cross_origin
from app.models.conformidade import Conformidade
from app.schemas.conformidade import ConformidadeSchema, NovoConformidadeSchema, ListaConformidadesSchema
from app.schemas.error import RespostaErroSchema
from app import db

conformidade_tag = Tag(name="Conformidade", description="Operações com conformidades")

conformidade_bp = APIBlueprint(
    'conformidade_bp',  # Nome único
    __name__,
    url_prefix='/conformidades',
    abp_tags=[conformidade_tag]
)


@conformidade_bp.route('/', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def handle_options():
    return "", 204  # Retorna uma resposta 204 sem conteúdo, permitindo o preflight request


@conformidade_bp.route('/status/', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def handle_options_status():
    return "", 204  # Retorna uma resposta 204 sem conteúdo, permitindo o preflight request

# Endpoint para listar todas as conformidades
@conformidade_bp.get(
    '/',
    summary="Lista todas as conformidades",
    responses={200: ListaConformidadesSchema}  # Usando ListaConformidadesSchema
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def listar_conformidades():
    conformidades = Conformidade.query.all()
    data = [ConformidadeSchema.from_orm(c).dict() for c in conformidades]
    return jsonify(data), 200

# Endpoint para criar uma nova conformidade
@conformidade_bp.post(
    '/',
    summary="Cria uma nova conformidade",
    responses={201: ConformidadeSchema, 400: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def criar_conformidade(body: NovoConformidadeSchema):
    try:
        nova_conformidade = Conformidade(
            ativo_id=body.ativo_id,
            controle_id=body.controle_id,
            status=body.status,
        )
        db.session.add(nova_conformidade)
        db.session.commit()
        return jsonify(ConformidadeSchema.from_orm(nova_conformidade).dict()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400




@conformidade_bp.get(
    '/status/',
    summary="Lista conformidades filtradas por status",
    responses={200: ListaConformidadesSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def listar_conformidades_por_status(query: StatusQueryParams):
 
    if status and status.lower() != "todos":
        conformidades = Conformidade.query.filter_by(status=status).all()
    else:
        conformidades = Conformidade.query.all()

    data = [ConformidadeSchema.from_orm(c).dict() for c in conformidades]
    return jsonify(data), 200