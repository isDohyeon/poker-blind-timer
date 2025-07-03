from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.blind_timer


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/api/users/signup', methods=['POST'])
def signup_api():
    name = request.form['name']
    print(name)
    email = request.form['email']
    print(email)
    password = request.form['password']
    print(password)

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

    signup_user = {
        "name": name,
        "email": email,
        "password": password
    }
    db.users.insert_one(signup_user)

    return jsonify({
        "success": True,
        "message": "Success: Signup complete!"
    }), 201


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
