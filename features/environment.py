from app.main import app
from fastapi.testclient import TestClient


def before_all(context):
    context.client = TestClient(app)
