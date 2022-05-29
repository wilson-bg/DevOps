from distutils.log import Log
import string
from flask import Blueprint,request
from src.connections.db_connection import DBConnection
from injector import inject
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.logica.logica import Logica


blacklists_api = Blueprint('blacklists_api', __name__)

# Permite agregar un email a la lista negra global de la organización.
@blacklists_api.route('', methods=['POST'])
@inject
@jwt_required()
def registrar_email(db_connection: DBConnection):
    email = request.json["email"]
    app_uuid = request.json["app_uuid"]
    blocked_reason = request.json["blocked_reason"]
    data, menssage, code = Logica.agregar_email(db_connection.db,email,app_uuid,blocked_reason,request.remote_addr) 
    return menssage, code

# Consulta email
@blacklists_api.route('/<email>', methods=['GET'])
@inject
@jwt_required()
def consultar_email(email:string,db_connection: DBConnection):
    data, menssage, code = Logica.consultar_email(db_connection.db,email)
    return menssage, code
    

# Consulta emails
@blacklists_api.route('/<email>/reports', methods=['GET'])
@inject
@jwt_required()
def consultar_lista_reportes(email:string,db_connection: DBConnection):
    data, menssage, code = Logica.consultar_lista_reportes(db_connection.db,email)    
    return menssage, code
