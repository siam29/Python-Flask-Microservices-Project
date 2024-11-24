from flask import Blueprint, request, jsonify
from models.models import register_user, authenticate_user, generate_jwt, decode_jwt, get_user_profile, get_token

# Create the Blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

# Route: Register a user
@user_routes.route('/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - User Management
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: John Doe
            email:
              type: string
              example: john@example.com
            password:
              type: string
              example: password123
            role:
              type: string
              example: User
    responses:
      201:
        description: User registered successfully
      409:
        description: Email already exists
      400:
        description: Missing required fields
    """
    
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "password", "role")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = register_user(data["name"], data["email"], data["password"], data["role"])
        if not user:
            return jsonify({"error": "Email already exists"}), 409
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Error registering user: {e}")  # Debug log
        return jsonify({"error": "Internal server error"}), 500

# Route: Login a user
@user_routes.route('/login', methods=['POST'])
def login():
    """
    Login a user
    ---
    tags:
      - User Management
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: john@example.com
            password:
              type: string
              example: password123
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            message:
              type: string
            token:
              type: string
      401:
        description: Invalid email or password
      400:
        description: Missing required fields
    """
    data = request.get_json()
    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = authenticate_user(data["email"], data["password"])
        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        # Include the role in the JWT
        token = generate_jwt(data["email"], user["role"])
        return jsonify({"message": "Login successful", "token": token}), 200
    except Exception as e:
        print(f"Error during login: {e}")  # Debug log
        return jsonify({"error": "Internal server error"}), 500

# Route: Get user profile (protected with JWT)
@user_routes.route('/profile', methods=['GET'])
def profile():
    """
    Get user profile (JWT-protected)
    ---
    tags:
      - User Management
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        example: Bearer <your_jwt_token>
    responses:
      200:
        description: Profile retrieved successfully
      401:
        description: Unauthorized
      400:
        description: Missing Authorization header
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 400

    try:
        token = auth_header.split(" ")[1]
        payload = decode_jwt(token)
        if not payload:
            return jsonify({"error": "Unauthorized"}), 401

        user = get_user_profile(payload["email"])
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user": user}), 200
    except Exception as e:
        print(f"Error retrieving profile: {e}")  # Debug log
        return jsonify({"error": "Internal server error"}), 500