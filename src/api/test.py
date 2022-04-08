from flask import Blueprint, request
from src.connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from src.model.bckList_model import BckList, pydantic_parser

test_api = Blueprint('test_api', __name__)

# Consulta de 
@test_api.route('/', methods=['GET'])
@inject
def dar_test(db_connection: DBConnection):
    try:
        result = db_connection.db.session.query(BckList).all()[0]
    except NoResultFound:
        return {"message": "Data not found"}, 404
    return pydantic_parser.from_orm(result).dict()



