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

# Esto [u.serialize() for u in users] es igual a esto otro:
# serialized_users = []
# for u in users:
#     serialized_users.append(u.serialize())

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = add_new_user(
        # Modificar en función de la tabla user en cada caso
        username=data['username'],
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        password=data['password']
    )
    return jsonify({"id": user.id, "username": user.username}), 201

if __name__ == '__main__':
    app.run(debug=True)