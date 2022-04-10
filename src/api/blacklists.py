from email import message
import string
from flask import Blueprint, request
from src.connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from src.model.bckList_model import BckList, bck_convertir, bck_convertir_arreglo, pydantic_parser
from flask_jwt_extended import jwt_required, get_jwt_identity

blacklists_api = Blueprint('blacklists_api', __name__)


# Permite agregar un email a la lista negra global de la organización.
@blacklists_api.route('', methods=['POST'])
@inject
@jwt_required()
def registrar_email(db_connection: DBConnection):
    
    try:
        email = request.json["email"]
        app_uuid = request.json["app_uuid"]
        blocked_reason = request.json["blocked_reason"]
        
        if not email or not app_uuid or email is None or app_uuid is None:
            return {"message":"Oops, hubo un error ","state": "failed", "error": "El email y app_uuid son obligatorios"}, 400
        
        data = BckList(email = email, app_uuid = app_uuid , blocked_reason = blocked_reason)
        db_connection.db.session.add(data)
        db_connection.db.session.commit()    
        return {"state": "success", "data" : bck_convertir(data)}
    except Exception as e:
        print(e)
        return {"message":"Oops, hubo un error ","state": "failed", "error":str(e)}, 400



# Consulta email
@blacklists_api.route('/<email>', methods=['GET'])
@inject
@jwt_required()
def consultar_email(email:string,db_connection: DBConnection):
    try:
        result = db_connection.db.session.query(BckList).filter(BckList.email == email).all()
    except NoResultFound:
        return {"message": "Data not found"}, 404
    
    if len(result) == 0 :
        return {"message": "Data not found"}, 404
    else :
            return { "message": "Reported email" }
    



# Consulta emails
@blacklists_api.route('/<email>/reports', methods=['GET'])
@inject
@jwt_required()
def consultar_lista_reportes(email:string,db_connection: DBConnection):
    try:
        result = db_connection.db.session.query(BckList).filter(BckList.email == email).all()
    except NoResultFound:
        return {"message": "Data not found"}, 404
    
    if len(result) == 0 :
        return {"message": "Data not found"}, 404
    
    #return bck_convertir_arreglo(result),200    
    return { "data": bck_convertir_arreglo(result) }
