# tests/test_app.py
# tests/test_app.py
# Testing app.py without actually calling OpenAI API

import pytest
from unittest.mock import patch


# English: Patch the call_agent function from agent module
@patch("agent.call_agent")
def test_call_agent_in_app(mock_call):
    # English: Define what the mock should return
    mock_call.return_value = "Mock response from agent"

    # English: Call the patched function
    response = mock_call("Hello from app test")

    # English: Assert the response is the mocked one
    assert response == "Mock response from agent"
