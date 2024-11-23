# In-memory storage for destinations
destinations = [
    {"id": 1, "name": "Paris", "description": "City of Light.", "location": "France", "price_per_night": 150.0},
    {"id": 2, "name": "Tokyo", "description": "Vibrant city.", "location": "Japan", "price_per_night": 200.0},
]

# Function to get all destinations
def get_all_destinations():
    """Return all destinations."""
    return destinations

# Function to delete a destination by its ID
def delete_destination(destination_id):
    """Delete a destination by its ID."""
    global destinations
    destination = next((d for d in destinations if d["id"] == destination_id), None)
    if destination:
        destinations = [d for d in destinations if d["id"] != destination_id]
        return True
    return False
