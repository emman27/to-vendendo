from tovendendo.db import db
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from wtforms.fields import PasswordField, TextField


class User(db.Model, login.UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), info={'label': 'Name'})
    email = db.Column(EmailType, unique=True, nullable=False, info={'label': 'Email'})
    phone_number = db.Column(PhoneNumberType(), info={'label': 'Phone Number'})
    password = db.Column(PasswordType(schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ]), nullable=False, info={'label': 'Password'})

    def __unicode__(self):
        return self.email

    def __repr__(self):
        return '%r' % (self.email)


class UserAdminView(ModelView):
    column_searchable_list = ('name', 'email')
    column_exclude_list = ('password')

    def is_accessible(self):
        return login.current_user.is_authenticated

    def scaffold_form(self):
        form_class = super(UserAdminView, self).scaffold_form()
        form_class.password = PasswordField('Password')
        form_class.phone_number = TextField('Phone Number')
        form_class.email = TextField('Email')
        return form_class
