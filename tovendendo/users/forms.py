from wtforms import form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired, Email, ValidationError
from wtforms.fields.html5 import EmailField, TelField

from tovendendo.db import db
from tovendendo.users.models import User


class LoginForm(form.Form):
    email = EmailField(validators=[
                        InputRequired(),
                        Email('This field requires a valid email address')])
    password = PasswordField(validators=[InputRequired()])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()


class RegistrationForm(form.Form):
    name = StringField()
    email = EmailField(validators=[
                        InputRequired(),
                        Email('This field requires a valid email address')])
    password = PasswordField(validators=[InputRequired()])
    phone_number = TelField()

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise ValidationError('Email already used')

    def validate_phone_number(self, field):
        if db.session.query(User).filter_by(phone_number=self.phone_number.data).count() > 0:
            raise ValidationError('Phone number already used')
