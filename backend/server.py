from flask import Flask, request, jsonify
from flask_cors import CORS 
from connect import connection_to_db
from connect import fetch_from_db
import jwt

app = Flask(__name__)
CORS(app) 
@app.route('/register' , methods = ['POST'])
def register():
    try:
        data = request.get_json()
        data= request.data
        data=eval(data)
        print(data)
        if fetch_from_db("SELECT user_id FROM register WHERE user_id = %s", (data['id'],) ):
                return jsonify({"error": "ID already exists."}), 400
        db=connection_to_db(f"INSERT INTO register (user_id, user_name, user_email,user_contact, user_password, designation) VALUES ('{data['id']}','{data['name']}','{data['email']}','{data['contact']}','{data['password']}','2');")
        print("DB",db)
        print("Done")
        return ({"data":"recieved data"})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Failed to register user."}), 500

@app.route('/login' , methods = ['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    id = fetch_from_db(f"SELECT user_id FROM register WHERE user_id='{username}'")
    password1 = fetch_from_db(f"SELECT user_password FROM register WHERE user_id='{username}'")
    
    if id and password1 and username == id and password == password1:
        print("Login successful!")
        return jsonify({'message': 'Done'})
    else:
        print("Invalid credentials!")
        return jsonify({'message': 'None'})
if __name__ == '__main__':
    app.run(debug = True)