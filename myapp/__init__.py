from flask import Flask
from .api.routes import api
from .site.routes import site
from .admin.routes import admin
from .models import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/chus/Documentos/Portafolio/flask/hola/filestorage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['IMAGE_UPLOADS'] = '/home/chus/Documentos/Portafolio/flask/hola/myapp/static/images'
    

    app.register_blueprint(api)
    app.register_blueprint(site)
    app.register_blueprint(admin)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        return app

    #db.init_app(app)

    

    
