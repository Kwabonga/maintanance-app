from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#Database
db= SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='abc'
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)
    

    #import blueprints
    from .views import views
    from .auth import auth 

   
   

    #Register them
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   
    
    
    from .models import User, Report

    create_database(app)
   
     #where the user must go if not logged in
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    #tells how we load a user
    @login_manager.user_loader 
    def load_user(id):
       return User.query.get(int(id))

    return app 

def create_database(app):
 if not path.exists('website/' + DB_NAME):
    with app.app_context():
       db.create_all()
    print('Created database')










  
