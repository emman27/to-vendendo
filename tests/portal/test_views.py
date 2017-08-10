def test_access_home_page(client):
    assert client.get('/').status_code == 200


def test_access_about_page(client):
    assert client.get('/about').status_code == 200


def test_access_how_it_works_page(client):
    assert client.get('/howitworks').status_code == 200


def test_access_contact_page(client):
    assert client.get('/contact').status_code == 200
    assert 'form' in str(client.get('/contact').data)
