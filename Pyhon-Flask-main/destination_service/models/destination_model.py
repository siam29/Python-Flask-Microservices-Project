# In-memory storage for destinations
destinations = [
    {"id": 1, "name": "Paris", "description": "City of Light.", "location": "France", "price_per_night": 150.0},
    {"id": 2, "name": "Tokyo", "description": "Vibrant city.", "location": "Japan", "price_per_night": 200.0},
    {"id": 3, "name": "New York", "description": "The Big Apple.", "location": "USA", "price_per_night": 250.0},
    {"id": 4, "name": "London", "description": "Historic city with modern vibes.", "location": "United Kingdom", "price_per_night": 180.0},
    {"id": 5, "name": "Sydney", "description": "Harbor city.", "location": "Australia", "price_per_night": 220.0},
    {"id": 6, "name": "Rome", "description": "The Eternal City.", "location": "Italy", "price_per_night": 140.0},
    {"id": 7, "name": "Bangkok", "description": "City of Angels.", "location": "Thailand", "price_per_night": 100.0},
    {"id": 8, "name": "Dubai", "description": "City of Gold.", "location": "UAE", "price_per_night": 300.0},
    {"id": 9, "name": "Cape Town", "description": "Mother City.", "location": "South Africa", "price_per_night": 120.0},
    {"id": 10, "name": "Rio de Janeiro", "description": "Marvelous City.", "location": "Brazil", "price_per_night": 130.0},
    {"id": 11, "name": "Istanbul", "description": "Where East meets West.", "location": "Turkey", "price_per_night": 110.0},
    {"id": 12, "name": "Barcelona", "description": "City of Gaudi.", "location": "Spain", "price_per_night": 170.0},
    {"id": 13, "name": "Moscow", "description": "The heart of Russia.", "location": "Russia", "price_per_night": 190.0},
    {"id": 14, "name": "Mumbai", "description": "City of Dreams.", "location": "India", "price_per_night": 80.0},
    {"id": 15, "name": "Singapore", "description": "Garden City.", "location": "Singapore", "price_per_night": 210.0}
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

# Example Usage
if __name__ == "__main__":
    print("All destinations:", get_all_destinations())
    print("Deleting destination with ID 3...")
    if delete_destination(3):
        print("Destination deleted successfully.")
    else:
        print("Destination not found.")
    print("Updated destinations:", get_all_destinations())
