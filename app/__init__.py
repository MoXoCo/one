from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    db_path = 'db.sqlite'

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///{}'.format(db_path)

    app.secret_key = 'a random string'

    db.init_app(app)
    db.app = app

    from .api import api as api_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(api_blueprint)
    app.register_blueprint(main_blueprint)

    return app