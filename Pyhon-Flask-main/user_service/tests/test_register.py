import pytest
import json
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from user_service.app import app  # Import the Flask app
from user_service.models.models import users  # Import the global users list

@pytest.fixture
def client():
    """Fixture to set up the test client for the Flask app."""
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)

def clear_users():
    """Reset the users list and clear the users.json file before each test."""
    global users
    users.clear()  # Clear the in-memory list

    # Clear the users.json file
    users_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models", "users.json"))
    if os.path.exists(users_file_path):
        with open(users_file_path, "w") as file:
            json.dump([], file)

def test_register_success(client):
    """Test successful user registration."""
    # Prepare the payload
    payload = {
        
    }
    

    # Send a POST request to the /register endpoint
    response = client.post('/users/register', data=json.dumps(payload), content_type='application/json')

    # Check the response status code
    assert response.status_code == 201

    # Parse the response JSON
    data = response.get_json()

    # Assert the message in the response
    assert "message" in data
    assert data["message"] == "User registered successfully"





def test_register_duplicate_email(client):
    """Test registration with a duplicate email."""
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123",
        "role": "User"
    }

    # First registration
    client.post('/users/register', data=json.dumps(payload), content_type='application/json')

    # Attempt duplicate registration
    response = client.post('/users/register', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 409
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Email already exists"

def test_register_missing_fields(client):
    """Test registration with missing required fields."""
    payload = {"email": "missingfields@example.com"}  # Missing other fields
    response = client.post('/users/register', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Missing required fields"
