from datetime import date, datetime

from sqlalchemy import false, true
import string
from src.model.bckList_model import BlackList, bck_convertir, bck_convertir_arreglo, pydantic_parser
from sqlalchemy.exc import NoResultFound
from src.logger_nr import logger

class Logica():
    
    def agregar_email(db,email:string,app_uuid:string,blocked_reason:string,remote_addr:string):
        try:
            
            if len(blocked_reason)>255:
                return None, {"message":"Oops, hubo un error ","state": "failed", "error": "El campo blocked_reason supera el máximo permitido de 255 caracteres"},400
            
            if not email or not app_uuid or email is None or app_uuid is None:
                logger.info(f"[INFO] error not data =>  email:{email} app_uuid:{app_uuid}")
                return None, {"message":"Oops, hubo un error ","state": "failed", "error": "El email y app_uuid son obligatorios"},400
            
            data = BlackList(email = email, app_uuid = app_uuid , blocked_reason = blocked_reason, ip_address = remote_addr)
            db.session.add(data)
            db.session.commit()
            logger.info(f"[INFO] add email {email}")
            return  data, {"state": "success", "data" : bck_convertir(data)} ,200
        
        except Exception as e:
            error = str(e)
            logger.info(f"[INFO] Add email error {error}")
            return data, {"message":"Oops, hubo un error ","state": "failed", "error":error} ,400
    
        
    def consultar_email(db,email:string):
        try:            
            result = db.session.query(BlackList).filter(BlackList.email == email).all()
            logger.info(f"[INFO] get email {email}")
        except NoResultFound:
            logger.info(f"[INFO] email {email} not found")
            return None, {"message": "Data not found"}, 404
        
        if len(result) == 0 :
            logger.info(f"[INFO] email not found {email}")
            return  None, {"message": "Data not found"}, 404
        else :
            logger.info(f"[INFO] email {email} found")
            return  result, { "message": "Reported email", "result" : bck_convertir_arreglo(result)  }, 200
        
        
        
    def consultar_lista_reportes(db,email:string):
        try:
            result = db.session.query(BlackList).filter(BlackList.email == email).all()
            logger.info(f"[INFO] get email {email}")
        except NoResultFound:
            logger.info(f"[INFO] email {email} not found")
            return None, {"message": "Data not found"}, 404
        
        if len(result) == 0 :
            logger.info(f"[INFO] email not found {email}")
            return None, {"message": "Data not found"}, 404
        
        logger.info(f"[INFO] email {email} found")
        return result,  { "data": bck_convertir_arreglo(result) }, 200