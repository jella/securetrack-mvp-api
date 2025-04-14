from flask_openapi3 import APIBlueprint, Tag
from flask import request, jsonify
from flask_cors import cross_origin
from app.models.ativos import Ativo
from app.schemas.ativo import AtivoSchema, NovoAtivoSchema, ListaAtivosSchema, AtivoPathParams
from app.schemas.error import RespostaErroSchema
from app import db
import requests

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

@ativos_bp.get(
    '/<int:id>/ipinfo',
    summary="Consulta informações de IP do ativo",
    description="Faz uma chamada externa ao IPinfo para buscar informações do IP do ativo."
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def consultar_ipinfo_ativo(path: AtivoPathParams):
    """
    Consulta informações de IP de um ativo usando IPinfo.
    """
    try:
        ativo = Ativo.query.get(path.id)

        if not ativo:
            return jsonify({"mensagem": "Ativo não encontrado"}), 404

        # Vamos supor que o IP está armazenado no campo 'observacoes'
        # Ex: observacoes="IP: 8.8.8.8"
        import re
        match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', ativo.observacoes or "")
        if not match:
            return jsonify({"mensagem": "IP não encontrado nas observações do ativo."}), 400
        
        ip = match.group(1)

        # Fazendo a requisição à API do IPinfo
        response = requests.get(f"https://ipinfo.io/{ip}/json")

        if response.status_code != 200:
            return jsonify({"mensagem": "Erro ao consultar IPinfo", "status": response.status_code}), 500

        ipinfo_data = response.json()

        return jsonify({
            "ip": ip,
            "dados_ipinfo": ipinfo_data
        }), 200

    except Exception as e:
        return jsonify({"mensagem": "Erro na consulta do IP", "erro": str(e)}), 400

@ativos_bp.get('/ipinfo/manual')
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def consultar_ipinfo_manual():
    try:
        ip = request.args.get('ip')
        if not ip:
            return jsonify({"mensagem": "IP não informado"}), 400

        print(f"🔍 Consultando IP: {ip}")
        response = requests.get(f"https://ipinfo.io/{ip}/json")

        print("📦 Resposta IPinfo:", response.text)

        if response.status_code != 200:
            return jsonify({"mensagem": "Erro ao consultar IPinfo"}), response.status_code

        return jsonify({
            "ip": ip,
            "dados_ipinfo": response.json()
        }), 200

    except Exception as e:
        print("💥 Erro interno:", str(e))
        return jsonify({"mensagem": "Erro na consulta do IP", "erro": str(e)}), 500
    

    

@ativos_bp.delete(
    '/<int:id>/',
    summary="Remove um ativo pelo ID",
    responses={204: None, 404: RespostaErroSchema, 400: RespostaErroSchema}
)
@cross_origin(origins="http://localhost:8000", supports_credentials=True)
def deletar_ativo(path: AtivoPathParams):
    """
    Remove um ativo do banco de dados com base no ID fornecido.
    """
    try:
        ativo_id = path.id
        ativo = Ativo.query.get(ativo_id)

        print("Path recebido:", path)
        print("ID recebido:", getattr(path, 'id', 'Sem ID'))

        if not ativo:
            return jsonify({"mensagem": "Ativo não encontrado"}), 404
     
        db.session.delete(ativo)
        db.session.commit()

        return '', 204

    except Exception as e:
        return jsonify({"mensagem": "Erro ao deletar ativo", "erro": str(e)}), 400


