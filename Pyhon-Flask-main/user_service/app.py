from flask import Flask
from flasgger import Swagger
from routes.routes import user_routes

app = Flask(__name__)

# Enable Swagger for API documentation
swagger = Swagger(app)

# Register the user routes Blueprint
app.register_blueprint(user_routes, url_prefix='/users')

@app.route('/')
def home():
    return "Welcome to the User Service!", 200

if __name__ == '__main__':
    app.run(debug=True)