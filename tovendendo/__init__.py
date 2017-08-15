import os
from tovendendo.portal.views import portal
from tovendendo.db import db
from tovendendo.users.models import User, UserAdminView
from tovendendo.items.models import Item, Category, ItemView, images
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_uploads import configure_uploads

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'tovendendo.config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['UPLOADED_IMAGES_DEST'] = 'data/images'
app.config['UPLOADED_IMAGES_URL'] = '/data/images/'

configure_uploads(app, (images))

db.init_app(app)

admin = Admin(app, name='tovendendo', template_mode='bootstrap3')
admin.add_view(UserAdminView(User, db.session))
admin.add_view(ItemView(Item, db.session))
admin.add_view(ModelView(Category, db.session))

app.register_blueprint(portal)
