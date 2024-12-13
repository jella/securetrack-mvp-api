from flask import Blueprint, jsonify, request
from app.services.ativos import AtivosService


bp = Blueprint()