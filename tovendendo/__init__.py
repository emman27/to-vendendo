import os
from tovendendo.portal.views import portal
from tovendendo.db import db
from tovendendo.users.models import User, UserAdminView
from tovendendo.items.models import Item, Category, ItemView
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'tovendendo.config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

admin = Admin(app, name='tovendendo', template_mode='bootstrap3')
admin.add_view(UserAdminView(User, db.session))
admin.add_view(ItemView(Item, db.session))
admin.add_view(ModelView(Category, db.session))

app.register_blueprint(portal)
