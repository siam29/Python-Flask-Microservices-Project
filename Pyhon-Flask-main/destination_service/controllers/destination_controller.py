from models.destination_model import get_all_destinations, delete_destination

# Controller function: Get all destinations
def fetch_all_destinations():
    """Fetch all destinations."""
    return get_all_destinations()

# Controller function: Delete a destination
def remove_destination(destination_id):
    """Delete a destination by ID."""
    return delete_destination(destination_id)
