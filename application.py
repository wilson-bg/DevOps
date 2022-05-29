import newrelic.agent
newrelic.agent.initialize()

import logging
from flask import Flask, render_template, jsonify
from src import create_app
from flask_jwt_extended import JWTManager
from src.model.init import instantiate_db
from flask_injector import FlaskInjector
from src.model.model import Base


# Flask Web Application
application = create_app('default')
application.config.from_object('config.default_settings.Config')
application.config.from_envvar('APPLICATION_SETTINGS', True)
application.config.from_envvar('APPLICATION_SECRETS', True)

with application.app_context():
    from src.connections.db_connection import db
    from src.logger_nr import logger
    db.Model = Base

from src.dependencies import configure
from src.api import blacklists_api,health_api,home_api
application.register_blueprint(home_api, url_prefix='/')
application.register_blueprint(health_api, url_prefix='/health')
application.register_blueprint(blacklists_api, url_prefix='/blacklists')
FlaskInjector(app=application, modules=[configure])
jwt = JWTManager(application)


# Navigation
@application.route("/")
def index():
    return render_template("index.html", title="Blacklists Application")

# Punto de arranque: servidor de desarrollo
print(__name__)
if __name__ == "__main__":
    logger.info(f"[INFO] Start App")
    # Iniciar la base de datos si no existe
    with application.app_context():
        instantiate_db(db=db)

    application.run(host="0.0.0.0", port=5000, debug=True )