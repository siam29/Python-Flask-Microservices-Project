from flask import Blueprint, request, jsonify
from models import decode_jwt, get_token_details

# Create the Blueprint for authentication routes
auth_routes = Blueprint('auth_routes', __name__)

# Route: Validate and display token details
@auth_routes.route('/validate', methods=['POST'])
def validate():
    """
    Validate a JWT token and display details
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpYW1AZXhhbXBsZS5jb20iLCJleHAiOjE3MzIzMDMyODJ9.BWSnxob88974pN0Lh8vclrCvK0l0X0XB5oCE0KqcYk"
    responses:
      200:
        description: Token is valid
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Token is valid"
            user_details:
              type: object
              properties:
                email:
                  type: string
                  example: "john@example.com"
                role:
                  type: string
                  example: "User"
                exp:
                  type: integer
                  example: 1732303375
                iat:
                  type: integer
                  example: 1732302975
      401:
        description: Invalid or expired token
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Invalid or expired token"
      404:
        description: Token not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Token not found"
    """
    data = request.get_json()
    print("Request Body:", data)  # Log the incoming request body
    
    if not data or "token" not in data:
        print("Missing token in request!")  # Log missing token error
        return jsonify({"error": "Missing token"}), 400

    token = data["token"]
    print(f"Received Token: {token}")  # Log the received token

    # Decode the token
    payload = decode_jwt(token)
    if not payload:
        print("Invalid or expired token!")  # Log invalid token
        return jsonify({"error": "Invalid or expired token"}), 401

    # Check token in tokens.json
    token_details = get_token_details(token)
    if not token_details:
        print("Token not found in tokens.json!")  # Log token not found
        return jsonify({"error": "Token not found"}), 404  # Fix: Return 404 for missing token

    print("Token is valid and found in tokens.json:", token_details)  # Log valid token

    return jsonify({
        "message": "Token is valid",
        "user_details": {
            "email": token_details["email"],
            "role": payload.get("role", "Unknown"),
            "exp": payload.get("exp"),
            "iat": payload.get("iat")
        }
    }), 200

