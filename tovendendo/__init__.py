import os
from tovendendo.portal.views import portal
from tovendendo.db import db
from tovendendo.users.models import User, UserAdminView
from tovendendo.users.views import AuthenticationView
from tovendendo.items.models import Item, Category, images
from tovendendo.items.views import ItemView, CategoryView
from flask import Flask
from flask_admin import Admin
from flask_uploads import configure_uploads
import flask_login as login


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'tovendendo.config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['UPLOADED_IMAGES_DEST'] = 'data/images'
app.config['UPLOADED_IMAGES_URL'] = '/data/images/'

configure_uploads(app, (images))

db.init_app(app)


def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


init_login()

admin = Admin(app, name='tovendendo', index_view=AuthenticationView(), template_mode='bootstrap3')
admin.add_view(UserAdminView(User, db.session))
admin.add_view(ItemView(Item, db.session))
admin.add_view(CategoryView(Category, db.session))

app.register_blueprint(portal)
