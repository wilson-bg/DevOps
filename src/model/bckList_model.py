from ipaddress import ip_address
from sqlalchemy import Column, String, Integer, DateTime
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import datetime



# Modelo para la base de datos
class  BlackList(Base):
    __tablename__ = "blacklist"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    app_uuid = Column(String(256), nullable=False)
    blocked_reason = Column(String(512), nullable=False)
    ip_address = Column(String(24), nullable=False)
    date_create = Column(DateTime , default=datetime.now)


pydantic_parser = sqlalchemy_to_pydantic(BlackList)

def bck_convertir_arreglo(arreglo):
    return list(map(bck_convertir, arreglo))

def bck_convertir(fila):
    return pydantic_parser.from_orm(fila).dict()
    