import pytest


def test_admin_index_show_login_form_when_user_is_not_logged(client, user, request):
    request.form = {}
    response = client.get('/admin', follow_redirects=True)

    email_input = '<input id="email" name="email" type="email" value="">'
    password_input = '<input id="password" name="password" type="password" value="">'

    assert response.status_code == 200
    assert email_input in str(response.data)
    assert password_input in str(response.data)
    assert 'Click here to register' in str(response.data)


def test_admin_index_show_logout_menu_when_user_is_logged(client, user, request):
    data = dict(email=user.email, password=user.password)
    client.post('/admin/login/', data=data, follow_redirects=True)

    request.form = {}
    response = client.get('/admin', follow_redirects=True)

    assert response.status_code == 200
    assert 'Log out' in str(response.data)


def test_login_sucessful(client, user):
    data = dict(email=user.email, password=user.password)
    response = client.post('/admin/login/', data=data, follow_redirects=True)

    assert response.status_code == 200


def test_login_not_sucessful(client):
    response = client.post('/admin/login/', data={}, follow_redirects=True)

    assert response.status_code == 200
    assert 'This field is required' in str(response.data)


def test_login_not_sucessful_with_invalid_user(client, user):
    data = dict(email='email@doesnot.exists', password='d3scubr4')
    response = client.post('/admin/login/', data=data, follow_redirects=True)

    assert response.status_code == 200
    assert 'Invalid credentials' in str(response.data)


def test_logout_sucessful(client, user):
    data = dict(email=user.email, password=user.password)
    client.post('/admin/login/', data=data, follow_redirects=True)
    response = client.get('/admin/logout/', follow_redirects=True)

    email_input = '<input id="email" name="email" type="email" value="">'
    password_input = '<input id="password" name="password" type="password" value="">'

    assert response.status_code == 200
    assert email_input in str(response.data)
    assert password_input in str(response.data)
    assert 'Click here to register' in str(response.data)


def test_logout_with_not_logged_user(client):
    response = client.get('/admin/logout/', follow_redirects=True)

    assert response.status_code == 200


def test_register(client):
    response = client.get('/admin/register/', follow_redirects=True)

    name_input = '<input id="name" name="name" type="text" value="">'
    email_input = '<input id="email" name="email" type="email" value="">'
    password_input = '<input id="password" name="password" type="password" value="">'
    phone_number_input = '<input id="phone_number" name="phone_number" type="tel" value="">'

    assert response.status_code == 200
    assert name_input in str(response.data)
    assert email_input in str(response.data)
    assert password_input in str(response.data)
    assert phone_number_input in str(response.data)
    assert 'Click here to log in' in str(response.data)


@pytest.mark.parametrize('view', ['item', 'user', 'category'])
def test_access_views_logged(client, view, user):
    data = dict(email=user.email, password=user.password)
    client.post('/admin/login/', data=data, follow_redirects=True)

    assert client.get('/admin/' + view, follow_redirects=True).status_code == 200


@pytest.mark.parametrize('view', ['item', 'user', 'category'])
def test_try_access_views_without_login(client, view):
    assert client.get('/admin/' + view, follow_redirects=True).status_code == 403
