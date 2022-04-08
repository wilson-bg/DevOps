from flask import current_app
from flask_sqlalchemy import SQLAlchemy

# Instanciar la base de datos
db = SQLAlchemy(current_app)

class DBConnection():
   def __init__(self):
      self.db = db
      
