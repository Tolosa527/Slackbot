from fastapi.testclient import TestClient
from .mocks.mock_help_command import mocks
from .. import main

client = TestClient(main.app)
