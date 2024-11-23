import pytest
import json
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to set up the test client for the Flask app."""
    app.testing = True
    with app.test_client() as client:
        yield client


def test_validate_token_not_found(client, monkeypatch):
    """Test validation with a token not found in tokens.json."""
    # Mock the decode_jwt function to return a valid payload
    monkeypatch.setattr("models.jwt_handler.decode_jwt", lambda token: {
        "email": "john@example.com",
        "role": "User",
        "exp": 1732303375,
        "iat": 1732302975
    })

    # Mock the get_token_details function to return None (token not found)
    monkeypatch.setattr("models.token_storage.get_token_details", lambda token: None)

    # Prepare the payload
    payload = {
        "token": "nonexistent.jwt.token"
    }

    # Send a POST request to /auth/validate
    response = client.post('/auth/validate', data=json.dumps(payload), content_type='application/json')

    # Assert the response
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] == "Token not found"
