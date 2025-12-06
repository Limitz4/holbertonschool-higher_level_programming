#!/usr/bin/python3
"""Flask API with Basic Auth and JWT authentication."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['JWT_SECRET_KEY'] = 'jwt-super-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials."""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@auth.error_handler
def auth_error():
    """Handle basic auth errors."""
    return jsonify({"error": "Unauthorized"}), 401


# JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# Basic Auth protected route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint."""
    return "Basic Auth: Access Granted"


# JWT login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Login and get JWT token."""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400
        
        if username not in users:
            return jsonify({"error": "Invalid credentials"}), 401
        
        if not check_password_hash(users[username]['password'], password):
            return jsonify({"error": "Invalid credentials"}), 401
        
        # Create access token with identity and role
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]['role']}
        )
        return jsonify(access_token=access_token)
    
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


# JWT protected route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """JWT protected endpoint."""
    return "JWT Auth: Access Granted"


# Admin only route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin only endpoint."""
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(debug=True)
