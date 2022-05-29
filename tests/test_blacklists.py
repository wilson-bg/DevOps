from ipaddress import ip_address
import unittest
import uuid
from faker import Faker
from src import create_app
from src.model.model import Base
from src.model.bckList_model import BlackList
from flask_sqlalchemy import SQLAlchemy
from src.logica.logica import Logica

def setup_context():
    app = create_app('default')
    app_context = app.app_context()
    app_context.push()
    db = SQLAlchemy()
    db.init_app(app)
    return db
                              
class BlackListTestCase(unittest.TestCase):
   
    def setUp(self):
        self.db = setup_context()
        self.data_factory = Faker()
        data = BlackList(email = self.data_factory.email(), app_uuid = uuid.uuid4(), blocked_reason = "spam", ip_address=self.data_factory.ipv4())
        self.db.session.add(data)
        self.db.session.commit()
        self.email = data.email

    def test_add_email(self):
        ''' => Prueba para añadir un nuevo email'''
        data = BlackList(email = self.data_factory.email(), app_uuid = uuid.uuid4(), blocked_reason = self.data_factory.text(100), ip_address=self.data_factory.ipv4())                
        data, menssage, code = Logica.agregar_email(self.db,data.email,data.app_uuid,data.blocked_reason,data.ip_address)         
        self.assertIsNotNone(data)
        self.assertEqual(code,200)
        self.assertGreater(data.id,0) 
        print("Id:", data.id, data.email,data.ip_address)
        
    
    def test_get_email(self):
        ''' =>  Obtener email'''
        data, menssage, code = Logica.consultar_email(self.db,self.email)        
        self.assertIsNotNone(data)
        self.assertEqual(code,200)
        self.assertEqual(self.email, data[0].email)
        print("Q:",self.email,"R:",data[0].email)