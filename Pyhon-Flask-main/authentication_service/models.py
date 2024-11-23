import jwt
import json
import os
from datetime import datetime, timedelta

# Construct the correct path to tokens.json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Navigate up to PYTHON-FLASK-1 directory
TOKEN_FILE = os.path.join(BASE_DIR, "user_service", "tokens.json")


# Secret key for signing JWT tokens
SECRET_KEY = "your_secret_key"

# Path to the tokens.json file
#TOKEN_FILE = os.path.join(os.path.dirname(__file__), "tokens.json")

# Function to decode and validate a JWT token
def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Decoded payload:", payload)  # Log the decoded payload
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired!")  # Log expired token
        return None
    except jwt.InvalidTokenError:
        print("Invalid token!")  # Log invalid token
        return None

# Function to retrieve token details from tokens.json
def get_token_details(token):
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = json.load(file)
            print("Loaded tokens:", tokens)  # Log all tokens
            for t in tokens:
                print("Comparing with token:", t["token"])  # Log comparison
                if t["token"] == token:
                    print("Token matched:", t)  # Log matched token
                    return t
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading tokens.json:", e)  # Log file access errors
        return None
    print("No matching token found!")  # Log no match
    return None



with open(TOKEN_FILE, "r") as file:
    tokens = file.read()
    print("Successfully loaded tokens.json:", tokens)
