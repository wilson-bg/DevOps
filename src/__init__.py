from flask import Flask

def create_app(config_name):
    app = Flask(__name__)      
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Amazon1234@devops.cvxrgbkdey3q.us-east-1.rds.amazonaws.com/blacklists'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    return app
