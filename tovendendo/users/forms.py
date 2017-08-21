from wtforms import form, fields, validators
from tovendendo.users.models import User
from werkzeug.security import check_password_hash
from tovendendo.db import db


class LoginForm(form.Form):
    email = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        email = self.get_email()

        if email is None:
            raise validators.ValidationError('Invalid email')

        if not check_password_hash(email.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()


class RegistrationForm(form.Form):
    name = fields.StringField()
    email = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])
    phone_number = fields.StringField()

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')
