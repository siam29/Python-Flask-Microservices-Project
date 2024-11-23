from flask import Flask
import sys
import os
from flasgger import Swagger

# Ensure the current folder is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the destination routes blueprint
from routes.destination_routes import destination_routes

# Create the Flask application
app = Flask(__name__)

# Add Swagger documentation
app.config['SWAGGER'] = {
    'title': 'Destination Service API',
    'uiversion': 3
}
swagger = Swagger(app)

# Register the blueprint for destination routes
app.register_blueprint(destination_routes, url_prefix='/destinations')

if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)
