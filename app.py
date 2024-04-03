from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from mongo_connector import user_col, contact_us_col, meeting_col
app = Flask(__name__)
CORS(app)


###### Pages
## Homepage
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

from pages.about.about import about

app.register_blueprint(about)

from pages.contact_us.contact_us import contact_us

app.register_blueprint(contact_us)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.post('/create_user')
def create_user_post():
    input = request.json
    result = user_col.insert_one(input)
    return jsonify(message="user has been created")


@app.post('/login')
def login_post():
    input = request.json
    user_email = input.get('email')
    user_password = input.get('password')
    print(user_email)
    print(user_password)
    user_cred = {"email": user_email, 'password': user_password}

    user = user_col.find(user_cred)
    for x in user:
        del x['_id']
        del x['password']
        return x

    return jsonify(message="user not found")


@app.post('/back_contact_us')
def contact_us_post():
    print('fffff')
    input = request.json
    # user_first_name = input.get('first_name')
    # user_last_name = input.get('last_name')
    # user_phone = input.get('phone')
    # user_email = input.get('email')
    # user_message = input.get('message')

    result = contact_us_col.insert_one(input)
    return jsonify(message="message has been saved")


@app.post('/create_meeting')
def meeting_post():
    input = request.json
    user_first_name = input.get('first_name')
    user_last_name = input.get('last_name')
    user_phone = input.get('phone')
    user_email = input.get('email')
    user_message = input.get('message')

    result = meeting_col.insert_one(input)
    return jsonify(message="meeting has been saved")


app.run(debug=True)
# app.run()

#