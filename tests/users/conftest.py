from tovendendo.users.models import User
import pytest


@pytest.fixture
def user(session):
    new_user = User(
        email='ana@testando.com',
        password='1234',
        phone_number='+358401234567')
    session.add(new_user)
    session.commit()

    yield new_user

    new_user.query.delete()


@pytest.fixture
def logged_user(user, client):
    data = dict(email=user.email, password=user.password)
    yield client.post('/admin/login/', data=data, follow_redirects=True)
    client.get('/admin/logout/', follow_redirects=True)
