from tovendendo.users.forms import LoginForm, RegistrationForm
from werkzeug.datastructures import MultiDict
import pytest


def test_allows_login_with_valid_data(user):
    data = MultiDict({'email': 'user@email.com', 'password': 'pas'})
    form = LoginForm(data)

    assert form.validate()


@pytest.mark.parametrize('email,password', [
    ('', ''),
    (None, None)
])
def test_login_when_form_is_invalid(email, password):
    form = LoginForm(email=email, password=password)

    assert not form.validate()


def test_allows_registration_with_valid_data(session):
    data = MultiDict({
                    'name': 'Harry Poter',
                    'email': 'harry@poter.com',
                    'password': '4321',
                    'phone_number': '43112345'})
    form = RegistrationForm(data)

    assert form.validate()


@pytest.mark.parametrize('name,email,password,phone_number', [
    ('', '', '', ''),
    (None, None, None, None)
])
def test_registration_when_form_is_invalid(name, email, password, phone_number, session):
    data = MultiDict({
                    'name': 'Myname',
                    'email': email,
                    'password': password,
                    'phone_number': '0987654'})
    form = RegistrationForm(data)

    assert not form.validate()


def test_denied_registration_with_already_registered_email(user, session):
    data = MultiDict({
                    'name': 'Harry Poter',
                    'email': user.email,
                    'password': '4321',
                    'phone_number': user.phone_number})
    form = RegistrationForm(data)

    assert not form.validate()


def test_denied_registration_with_already_registered_phone_number(user, session):
    data = MultiDict({
                    'name': 'Harry Poter',
                    'email': 'user@email.com',
                    'password': '4321',
                    'phone_number': user.phone_number})
    form = RegistrationForm(data)

    assert not form.validate()
