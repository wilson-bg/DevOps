from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src.connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from src.model.bckList_model import BlackList, pydantic_parser
from flask_jwt_extended import jwt_required, get_jwt_identity
import socket
import uuid
from src.logger_nr import logger

home_api = Blueprint('home_api', __name__)
health_api = Blueprint('health_api', __name__)



'''@home_api.route('/', methods=['GET'])
@inject
def home():
    uid = uuid.uuid4().hex
    token_de_acceso = create_access_token(identity = 4)
    logger.info(f"[INFO] Token Create => uid: {uid}")
    return {"uuid": str(uid), "token": token_de_acceso}'''




@health_api.route('/ping', methods=['GET'])
@inject
def home_ping():
    uid = uuid.uuid4().hex
    token_de_acceso = create_access_token(identity = 4)
    logger.info(f"[INFO] Ping => uid: {uid}")
    return {"uuid": str(uid),"state": "success", "running host": socket.gethostname(), "dn:":socket.getfqdn(),"token": token_de_acceso}, 200