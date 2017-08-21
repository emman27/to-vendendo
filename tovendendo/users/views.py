import flask_login as login
from flask import url_for, redirect, request, flash
from flask_admin import helpers, expose
import flask_admin as admin
from werkzeug.security import generate_password_hash
from tovendendo.users.forms import LoginForm, RegistrationForm
from tovendendo.users.models import User
from tovendendo.db import db

# TODO move to appropriate folder (admin?)


class AuthenticationView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(AuthenticationView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user:
                login.login_user(user)
            else:
                flash('Invalid credentials')

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        # TODO remove HTML code
        link = '<p>Don\'t have an account? <a href="' \
            + url_for('.register_view') + '">Click here to register</a></p>'

        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AuthenticationView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))

        link = '<p>Already have an account? <a href="' \
            + url_for('.login_view') + '">Click here to log in</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AuthenticationView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
