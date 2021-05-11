# TODO(everyone): 웹서버의 healthz가 response code 200 확인
import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_healthCheck(app, client):
    res = client.get("/healthz")
    assert res.status_code == 200
