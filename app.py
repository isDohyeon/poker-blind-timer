from flask import Flask, render_template, jsonify, request
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)

bcrypt = Bcrypt(app)

client = MongoClient('localhost', 27017)
db = client.blind_timer


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/api/users/login', methods=['POST'])
def login_api():
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Fail: email or password required."
        }), 400

    user = db.users.find_one({"email": email})
    if not user:
        return jsonify({
            "success": False,
            "message": "Fail: email not found."
        }), 401

    if not bcrypt.check_password_hash(user["password"], password):
        return jsonify({
            "success": False,
            "message": "Fail: Incorrect password."
        }), 401

    return jsonify({
        "success": True,
        "message": "Success: Login complete!"
    }), 200


@app.route('/api/users/signup', methods=['POST'])
def signup_api():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "Fail: name, email, and password are required."
        }), 400

    exsisting_user = db.users.find_one({"email": email})
    if exsisting_user:
        return jsonify({
            "success": False,
            "message": "Fail: Email already exists."
        }), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    signup_user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }
    db.users.insert_one(signup_user)

    return jsonify({
        "success": True,
        "message": "Success: Signup complete!"
    }), 201


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
