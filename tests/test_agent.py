# tests/test_agent.py
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src folder to Python path so tests can import project modules
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

# Now import the function under test from the agent module
from agent import call_agent


def test_call_agent_response_type_and_content():
    """
    Test that call_agent returns a string and returns the expected
    content when the agent.invoke method is mocked.
    This avoids any real network/API calls.
    """
    query = "Hello"

    # Patch the 'invoke' method on the agent object inside the agent module.
    # We patch 'agent.agent.invoke' because, after sys.path manipulation, agent is imported as a module.
    with patch("agent.agent.invoke") as mock_invoke:
        # Create a fake message object with the attributes the real code expects
        fake_message = MagicMock()
        fake_message.type = "ai"
        fake_message.content = "Mocked response"

        # Make the mocked invoke return a dict similar to the real agent.invoke result
        mock_invoke.return_value = {"messages": [fake_message]}

        # Call the function under test
        response = call_agent(query)

        # Assertions: response should be a string and match the mocked content
        assert isinstance(response, str)
        assert response == "Mocked response"
