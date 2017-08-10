from tovendendo.db import db
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField, TextField


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(EmailType, unique=True)
    phone_number = db.Column(PhoneNumberType())
    _password = db.Column(PasswordType())

    def __repr__(self):
        return '%r' % (self.email)


class UserAdminView(ModelView):
    column_searchable_list = ('name', 'email')
    column_exclude_list = ('_password')

    def scaffold_form(self):
        form_class = super(UserAdminView, self).scaffold_form()
        form_class.password = PasswordField('Password')
        form_class.phone_number = TextField('Phone Number')
        form_class.email = TextField('Email')
        return form_class
