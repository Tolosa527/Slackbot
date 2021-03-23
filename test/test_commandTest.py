from fastapi.testclient import TestClient
from .mocks.mock_help_command import mocks
from .. import main

client = TestClient(main.app)

def test_commnad_test():
    response = client.post(
        '/api/test',
    )
    assert response.status_code == 200
    assert response.json() == {
        "text":"Everything OK!",
        }
