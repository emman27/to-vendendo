from tovendendo.db import db
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType
import flask_login as login


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

    #def __unicode__(self):
    #    return self.email

    def __repr__(self):
        return self.email
