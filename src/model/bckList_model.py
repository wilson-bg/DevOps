from sqlalchemy import Column, String, Integer
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

# Modelo para la base de datos
class  BckList(Base):
    __tablename__ = "bck_list"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    app_uuid = Column(String(256), nullable=False)
    blocked_reason = Column(String(512), nullable=False)

pydantic_parser = sqlalchemy_to_pydantic(BckList)

def bck_convertir_arreglo(arreglo):
    return list(map(bck_convertir, arreglo))

def bck_convertir(fila):
    return pydantic_parser.from_orm(fila).dict()
    