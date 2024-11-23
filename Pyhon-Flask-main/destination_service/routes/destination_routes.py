from flask import Blueprint, jsonify, request
from controllers.destination_controller import fetch_all_destinations, remove_destination

# Create a Blueprint for the destination routes
destination_routes = Blueprint('destination_routes', __name__)

# Route: Get all destinations
@destination_routes.route('/', methods=['GET'])
def get_destinations():
    """
    Get all destinations
    ---
    tags:
      - Destinations
    responses:
      200:
        description: A list of destinations
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: Paris
              description:
                type: string
                example: City of Light.
              location:
                type: string
                example: France
              price_per_night:
                type: number
                example: 150.0
    """
    destinations = fetch_all_destinations()
    return jsonify(destinations), 200

# Route: Delete a destination (Admin-only)
@destination_routes.route('/<int:destination_id>', methods=['DELETE'])
def delete_destination_route(destination_id):
    """
    Delete a destination (Admin-only)
    ---
    tags:
      - Destinations
    parameters:
      - name: destination_id
        in: path
        type: integer
        required: true
        description: The ID of the destination to delete
      - name: Role
        in: header
        type: string
        required: true
        description: The role of the user (must be Admin)
    responses:
      200:
        description: Destination deleted successfully
      403:
        description: Unauthorized access
      404:
        description: Destination not found
    """
    admin_role = request.headers.get('Role')
    if admin_role != 'Admin':
        return jsonify({"error": "Unauthorized access"}), 403

    if remove_destination(destination_id):
        return jsonify({"message": "Destination deleted successfully"}), 200
    return jsonify({"error": "Destination not found"}), 404
