import pytest
from tovendendo import app as _app
from tovendendo.db import db as _db


@pytest.fixture(scope='session')
def app(request):
    _app.config.from_object('tovendendo.config.TestConfig')

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    return _app


@pytest.fixture(scope='session')
def db(app, request):
    _db.app = app
    _db.drop_all()
    _db.create_all()
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
