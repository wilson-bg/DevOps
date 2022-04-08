from sqlalchemy.exc import IntegrityError
from src.model.bckList_model import BckList
import uuid

def instantiate_db(db) -> None:
    """
    Permite instanciar la base de datos
    Dado a que con gunicorn instanciamos varios workers,
    estos al iniciar intentaran volver a crear la base de datos.
    Lo anterior causara un error que vamos a suprimir

    :param db: Conexion a la base de datos
    """
    try:
        db.create_all()
        #data = BckList(email = "1@1.1", app_uuid = uuid.uuid4(), blocked_reason = "*****")
        #db.session.add(data)
        #db.session.commit()
        
    except IntegrityError as e:
        pass
