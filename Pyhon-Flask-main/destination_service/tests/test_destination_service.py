import pytest
import json
#from destination_service.app import app  # Adjust import path for app

import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from destination_service.app import app  # Adjust import path for app





@pytest.fixture
def client():
    """Fixture to set up the test client for the Flask app."""
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_all_destinations(client):
    """Test the GET /destinations/ endpoint."""
    response = client.get('/destinations/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_delete_destination_as_admin(client):
    """Test DELETE /destinations/<id> as an admin."""
    headers = {"Role": "Admin"}
    response = client.delete('/destinations/1', headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "message" in data
    assert data["message"] == "Destination deleted successfully"

def test_delete_destination_as_non_admin(client):
    headers = {"Role": "User"}  # Non-admin role
    response = client.delete('/destinations/1', headers=headers)
    assert response.status_code == 403
    data = json.loads(response.data)
    assert "error" in data
    assert data["error"] == "Unauthorized access"


def test_delete_destination_missing_headers(client):
    response = client.delete('/destinations/1')  # No headers
    assert response.status_code == 403
    data = json.loads(response.data)
    assert "error" in data
    assert data["error"] == "Unauthorized access"


def test_delete_nonexistent_destination(client):
    headers = {"Role": "Admin"}
    response = client.delete('/destinations/999', headers=headers)  # ID does not exist
    assert response.status_code == 404
    data = json.loads(response.data)
    assert "error" in data
    assert data["error"] == "Destination not found"
