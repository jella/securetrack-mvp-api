from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify
from flask_cors import cross_origin
from app.models.responsavel import Responsavel
from app.schemas.responsavel import ResponsavelSchema, NovoResponsavelSchema, ListaResponsavelSchema, ResponsavelPathParams
from app.schemas.error import RespostaErroSchema
from app import db

responsavel_tag = Tag(name="Responsavel", description="Op")

# erações com responsaveisInicializando o Blueprint
responsaveis_bp = APIBlueprint(
    'responsaveis_bp',
    __name__,
    url_prefix='/responsaveis',
    abp_tags=[responsavel_tag]
)

# Endpoint para CORS preflight OPTIONS
@responsaveis_bp.route('/', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def handle_options():
    return "", 204  # Retorna uma resposta 204 sem conteúdo, permitindo o preflight request

# Endpoint para listar todos os responsaveis
@responsaveis_bp.get(
    '/',
    summary="Lista todos os responsaveis",
    responses={200: ListaResponsavelSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def listar_responsaveis():
    responsaveis = Responsavel.query.all()
    data = [ResponsavelSchema.model_validate(a, from_attributes=True) for a in responsaveis]
    return jsonify([d.dict() for d in data]), 200

@responsaveis_bp.get(
    '/<int:id>',  # Defina a URL com o parâmetro id capturado da URL
    summary="Consulta um responsavel específico",
    description="Recupera as informações de um responsavel específico pelo seu ID."
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def consultar_responsavel(path: ResponsavelPathParams):
    """
    Consulta um responsavel específico pelo ID.
    """
    try:
        # Buscar o responsavel pelo ID
        responsavel_id = path.id
        responsavel = responsavel.query.get(responsavel_id)
        
        # Se não encontrar o responsavel
        if not responsavel:
            return jsonify({"mensagem": "responsavel não encontrado"}), 404

        # Retornar o responsavel encontrado
        return jsonify(responsaveischema.model_validate(responsavel, from_attributes=True).dict()), 200

    except Exception as e:
        return jsonify({"mensagem": "Erro ao consultar responsavel", "erro": str(e)}), 400

        
# Endpoint para criar um novo responsavel
@responsaveis_bp.post(
    '/',
    summary="Cria um novo responsavel",
    responses={201: ResponsavelSchema, 400: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def criar_responsavel(body: NovoResponsavelSchema):
    try:
        novo = Responsavel(
            nome=body.nome,
            status=body.status,
            email=body.email
        )
        db.session.add(novo)
        db.session.commit()

        return jsonify(ResponsavelSchema.model_validate(novo, from_attributes=True).dict()), 201

    except Exception as e:
        return jsonify({"mensagem": "Erro ao criar responsavel", "erro": str(e)}), 400


# Endpoint para deletar um responsavel específico
@responsaveis_bp.delete(
    '/<int:id>',  # Parametro 'id' na URL
    summary="Deleta um responsavel específico",
    description="Remove um responsavel específico do banco de dados pelo ID.",
    responses={
        200: ResponsavelSchema,  # Resposta 200 com o responsavel deletado ou uma confirmação
        404: RespostaErroSchema,  # Resposta 404 caso o responsavel não seja encontrado
        400: RespostaErroSchema   # Resposta 400 para erros gerais
    }
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def deletar_responsavel(path: ResponsavelPathParams):  # Aqui passamos o parâmetro `id` diretamente
    """
    Deleta um responsavel específico pelo ID.
    """
    try:
        # Buscar o responsavel pelo ID
        responsavel_id = path.id
        responsavel = Responsavel.query.get(responsavel_id)  # Usando o id para buscar no banco de dados

        # Se não encontrar o responsavel, retorna um erro 404
        if not responsavel:
            return jsonify({"mensagem": "responsavel não encontrado"}), 404

        # Deleta o responsavel
        db.session.delete(responsavel)
        db.session.commit()

        # Retorna a confirmação com o objeto deletado
        return jsonify({"mensagem": f"responsavel {path.id} deletado com sucesso!"}), 200
  
    except Exception as e:
        return jsonify({"mensagem": "Erro ao deletar responsavel", "erro": str(e)}), 400