from flask import Flask
from .injections.routes import injections
from .dashboard.routes import dashboard
from extensions import *


def create_app():
    app = Flask(__name__)
    #app.config.from_object('config.DevConfig')
    # Initialise extensions
    #mongo.init_app(app)
    with app.app_context():
        app.register_blueprint(injections, url_prefix="/injections")
        app.register_blueprint(dashboard, url_prefix="/dashboard")
    return app