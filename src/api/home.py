#from flask import current_app,request
#from flask_restful import Resource
#from flask_jwt_extended import create_access_token
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src.connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from src.model.bckList_model import BlackList, pydantic_parser
from flask_jwt_extended import jwt_required, get_jwt_identity
#import socket
import uuid

home_api = Blueprint('home_api', __name__)

#class VistaHome(Resource):
#    def get(self):                       
#        return {"state": "success", "running host": socket.gethostname(), "dn:":socket.getfqdn()}, 200

# Consulta de 

@home_api.route('/', methods=['GET'])
@inject
def home(db_connection: DBConnection):
    uid = uuid.uuid4().hex
    token_de_acceso = create_access_token(identity = 4)
    return {"uuid": str(uid), "token": token_de_acceso}
    #return {"state": "success", "running host": socket.gethostname(), "dn:":socket.getfqdn()}, 200
