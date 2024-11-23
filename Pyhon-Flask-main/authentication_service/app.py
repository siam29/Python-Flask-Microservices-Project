from flask import Flask
from flasgger import Swagger
from flask_cors import CORS  # Add CORS support
from routes import auth_routes

app = Flask(__name__)

# Enable CORS
CORS(app)

# Enable Swagger for API documentation
swagger = Swagger(app)

# Register the authentication routes Blueprint
app.register_blueprint(auth_routes, url_prefix='/auth')

@app.route('/')
def home():
    return "Welcome to the Authentication Service!", 200

if __name__ == '__main__':
    app.run(debug=True)
