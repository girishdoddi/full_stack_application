from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
from hashlib import md5
from random import randint
import json

from email_service import send_otp_to_mail


app = Flask(__name__)


app.config['MYSQL_HOST'] = "database-1.clm00secym6r.ap-south-1.rds.amazonaws.com"
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "7416252855aA"
app.config['MYSQL_DB'] = "Authentication"


mysql = MySQL(app)
@app.route('/', methods = ["GET"])
def func():
    return "Working"

@app.route("/signup", methods = ["POST"])
def signUp():
    input_json = request.data
    input_json = json.loads(input_json.decode())
    print(input_json)
    print("Working")
    email = input_json.get("email")
    password = input_json.get("password")
    password = str(md5(password.encode()).hexdigest())
    print(password)
    print(type(password))
    user_name = input_json.get("username")
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM otp_verification WHERE email_id = %s", (email,))
    account = cur.fetchall()
    print(account)
    print("Working 2")
    cur.close()
    if account:
        print(account)
        return {"message" : "Account Already Exists"}
    else:
        otp = randint(10000, 99999)
        send_otp_to_mail(email = email, otp= otp)
        date_time = datetime.now() + timedelta(minutes=5)
        #send otp to the given email id
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO otp_verification (email_id, otp, expiry_date, password_hashed, user_name)
                     VALUES(%s, %s, %s, %s, %s)''', (email, otp, date_time.strftime('%Y-%m-%d %H:%M:%S'), password, user_name))
        mysql.connection.commit()
        cur.close()
        return {"message" : "OTP Sent Successfully"}


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)


