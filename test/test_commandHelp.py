from fastapi.testclient import TestClient
from .mocks.mock_help_command import mocks
from .. import main

client = TestClient(main.app)

def test_command_help():
    command_body = mocks['help']
    response = client.post(
        '/api/help',
        data = command_body
    )
    assert response.status_code == 200
    assert response.json() == {
        "text":"/task <owner>:<description> || /task list"
        }
