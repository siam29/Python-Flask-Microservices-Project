# import hashlib
import jwt
import json
import bcrypt
from datetime import datetime, timedelta, timezone
# from datetime import datetime,   # Import timezone


# In-memory storage for users
#users = []

# Secret key for signing JWT tokens
SECRET_KEY = "your_secret_key"

# File to store tokens persistently
TOKEN_FILE = "tokens.json"
USERS_FILE = "users.json"


# Hash a password securely
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


# Verify a hashed password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


# Function to load users from the JSON file
def load_users():
    global users
    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print(f"{USERS_FILE} not found. Initializing a new file.")
        users = []
    except json.JSONDecodeError:
        print(f"Error decoding {USERS_FILE}. Initializing an empty list.")
        users = []
'''
# Function to save users to the JSON file
def save_users():
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

'''
'''
# Function to register a user
def register_user(name, email, password, role):
    for user in users:
        if user["email"] == email:
            return None  # Email already exists
    new_user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "role": role,
        "created_at": datetime.utcnow().isoformat() + "Z"  # ISO 8601 format
    }
    users.append(new_user)
    save_users()  # Save updated users list to file
    return new_user

    '''
        

        #users = []  # This should be the global list to hold user data

def register_user(name, email, password, role):
    """Register a new user if the email is not already taken."""
    global users  # Ensure we modify the global `users` list
    for user in users:
        if user["email"] == email:
            return None  # Email already exists

    new_user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "role": role,
        "created_at": datetime.now(timezone.utc).isoformat()  # Use timezone-aware timestamp
    }
    users.append(new_user)
    
    try:
        save_users()  # Save the updated users list to `users.json`
        print(f"User {email} saved successfully to users.json")  # Debug log
    except Exception as e:
        print(f"Error saving user {email}: {e}")  # Debug log for errors

    return new_user


def save_users():
    """Save the users list to the JSON file."""
    try:
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)
        print(f"Saved users to {USERS_FILE}")  # Debug log
    except Exception as e:
        print(f"Error saving users: {e}")  # Debug log for save errors


# Function to authenticate a user
def authenticate_user(email, password):
    for user in users:
        if user["email"] == email and verify_password(password, user["password"]):
            return user
    return None


# Function to generate a JWT token with role
def generate_jwt(email, role):
    payload = {
        "email": email,
        "role": role,  # Include role in the token
        "exp": datetime.utcnow() + timedelta(hours=5),  # Token expires in 5 hours
        "iat": datetime.utcnow()  # Issued at timestamp
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    save_token(email, token)
    return token


# Function to decode and validate a JWT token
def decode_jwt(token):
    try:
        # print(SECRET_KEY)
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Decoded Payload:", payload)  # Debug: Print the decoded payload
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token


# Function to save a token in the JSON file
def save_token(email, token):
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tokens = []

    # Add or update the token for the user
    tokens = [t for t in tokens if t["email"] != email]  # Remove old token for the same email
    tokens.append({"email": email, "token": token})
    with open(TOKEN_FILE, "w") as file:
        json.dump(tokens, file, indent=4)


# Function to retrieve a token from the JSON file
def get_token(email):
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = json.load(file)
            for t in tokens:
                if t["email"] == email:
                    return t
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return None


# Function to retrieve a user's profile by email
def get_user_profile(email):
    for user in users:
        if user["email"] == email:
            return {"name": user["name"], "email": user["email"], "role": user["role"]}
    return None


# Load users at startup
load_users()