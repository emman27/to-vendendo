import pytest
from tovendendo import app as _app


@pytest.fixture
def app():
    _app.config.from_object('tovendendo.config.TestConfig')
    return _app
