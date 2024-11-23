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

def test_validate_token_success(client, monkeypatch):
    """Test successful token validation."""
    # Mock the decode_jwt function to return a payload
    monkeypatch.setattr("routes.decode_jwt", lambda token: {
        "email": "john@example.com",
        "role": "User",
        "exp": 1732303375,
        "iat": 1732302975
    })

    # Mock the get_token_details function to return token details
    monkeypatch.setattr("routes.get_token_details", lambda token: {
        "token": token,
        "email": "john@example.com",
        "role": "User"
    })

    # Prepare the payload
    payload = {
        "token": "mocked.jwt.token"
    }

    # Send a POST request to /auth/validate
    response = client.post('/auth/validate', data=json.dumps(payload), content_type='application/json')

    # Assert the response
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Token is valid"
    assert data["user_details"]["email"] == "john@example.com"
    assert data["user_details"]["role"] == "User"

def test_validate_token_invalid(client, monkeypatch):
    """Test validation with an invalid token."""
    # Mock the decode_jwt function to return None (invalid token)
    monkeypatch.setattr("routes.decode_jwt", lambda token: None)

    # Prepare the payload
    payload = {
        "token": "invalid.jwt.token"
    }

    # Send a POST request to /auth/validate
    response = client.post('/auth/validate', data=json.dumps(payload), content_type='application/json')

    # Assert the response
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "Invalid or expired token"


def test_validate_token_not_found(client, monkeypatch):
    """Test validation with a token not found in tokens.json."""
    # Mock the decode_jwt function to return a valid payload
    monkeypatch.setattr("routes.decode_jwt", lambda token: {
        "email": "john@example.com",
        "role": "User",
        "exp": 1732303375,
        "iat": 1732302975
    })



    # Mock the get_token_details function to return None (token not found)
    monkeypatch.setattr("routes.get_token_details", lambda token: None)

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
    

def test_validate_missing_token(client):
    """Test validation with a missing token in the request body."""
    # Prepare an empty payload
    payload = {}

    # Send a POST request to /auth/validate
    response = client.post('/auth/validate', data=json.dumps(payload), content_type='application/json')

    # Assert the response
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Missing token"
