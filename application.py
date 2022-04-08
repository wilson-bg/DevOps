from flask import Flask
from src.model.init import instantiate_db
from flask_injector import FlaskInjector
from src.model.model import Base

# Instancia de la aplicación en Flask
app = Flask(__name__)
#app = create_app('default')

app.config.from_object('config.default_settings.Config')
app.config.from_envvar('APPLICATION_SETTINGS', True)
app.config.from_envvar('APPLICATION_SECRETS', True)


with app.app_context():
    from src.connections.db_connection import db
    db.Model = Base

from src.dependencies import configure

from src.api.test import test_api
app.register_blueprint(test_api, url_prefix='/test')

#@app.route('/ping')
#def ping():
#    return 'pong'

# Agregamos el inyector de dependencias 
FlaskInjector(app=app, modules=[configure])


# Punto de arranque: gunicorn
def gunicorn():
    # Iniciar la base de datos si no existe
    with app.app_context():
        instantiate_db(db=db)

    # Retornar el objeto de la aplicacion
    return app

# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    # Iniciar la base de datos si no existe
    with app.app_context():
        instantiate_db(db=db)

    app.run(
        host="0.0.0.0", port=5000, debug=True
    )