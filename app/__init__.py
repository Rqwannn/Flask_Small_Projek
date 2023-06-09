from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    Migrate(app, db)

    from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint

    # Registri the Blueprint/Views 

    app.register_blueprint(main_blueprint)

    # Registri the Auth/Backend Logic 

    app.register_blueprint(auth_blueprint)

    return app