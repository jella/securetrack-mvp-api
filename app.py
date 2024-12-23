from flask import Flask, redirect
from flask_openapi3 import OpenAPI,  Info, Tag
from pydantic import BaseModel
from app.controllers.ativos import ativo_tag, ativos_bp
from app import create_app
from app.controllers.ativos import  ativos_bp
from app.controllers.controles import  controles_bp
from app.controllers.conformidades import  conformidade_bp

app = create_app()



app.register_api(ativos_bp)
app.register_api(controles_bp)
app.register_api(conformidade_bp)

@app.route("/")
def index():
    return redirect("/openapi/swagger")

if __name__ == "__main__":
    app.run('127.0.0.1', '3001',debug=True)