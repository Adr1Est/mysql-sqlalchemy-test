# Servidor Flask
from flask import Flask, jsonify, request
from config import Config
from models import db, User
from db_utils import get_all_users, add_new_user

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([u.serialize() for u in users]), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = add_new_user(
        username=data['username'],
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        password=data['password']
    )
    return jsonify({"id": user.id, "username": user.username}), 201

if __name__ == '__main__':
    app.run(debug=True)