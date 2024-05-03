from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from .views import map_search_views
from sqlalchemy import MetaData

convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models 

    from .views import main_views, board_views, auth_views,map_search_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(board_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(map_search_views.bp)

    return app