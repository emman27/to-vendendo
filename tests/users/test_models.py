from tovendendo.users.models import User


def test_show_user_name():
    assert repr(User(email='ana@ana.com')) == 'ana@ana.com'
