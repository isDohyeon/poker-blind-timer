from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.blind_timer

# db.users.insert_one({
#     "name": "tester",
#     "email": "test@test.com",
#     "password": "test123"
# })


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
