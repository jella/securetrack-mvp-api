from flask import Flask
from flask_openapi3 import OpenAPI,  Info, Tag
from pydantic import BaseModel
from app.controllers.ativos import ativo_tag, ativos_bp
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run('127.0.0.1','3001',debug=True)