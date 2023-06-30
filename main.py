# Using Flask framework along with Mysql database to store user information
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_cors import CORS
from flask_cors import cross_origin
import requests
from flask_mysqldb import MySQL
import MySQLdb.cursors
import phonenumbers
import config
import bcrypt

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config["HOST"] = config.host
app.config["MYSQL_USER"] = config.mysql_user
app.config["MYSQL_PASSWORD"] = config.mysql_password
app.config["MYSQL_DB"] = config.database

mysql = MySQL(app)
app.secret_key = 'xyzsdfg'      # for using sessions


@app.route("/", methods=['GET'])  # Landing homepage.
@cross_origin(supports_credentials=True)
def homepage():
    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def register():
    message = ''
    cur = mysql.connection.cursor()
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = str(request.form["name"])
        email = str(request.form["email"])
        country_code = str(request.form["country"])
        phoneNum = country_code + str(request.form["phone"])
        isValid = validate_phone_number(phoneNum)
        print(isValid)
        password = str(request.form["password"])
        confirmPassword = str(request.form["confirmpassword"])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from users where email like %s", (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!!'
            print(message)
        else:
            if isValid[0] == True:
                if password == confirmPassword and len(password) > 6:
                    cursor.execute("insert into users (name, email, phone_num, password, confirm_password) values (%s, %s, %s, %s, %s)",
                                   (userName, email, phoneNum, password, confirmPassword))
                    mysql.connection.commit()
                    message = 'Successfully registered.'
                    print(message)
                    return redirect(url_for('login'))
                else:
                    if password != confirmPassword:
                        message = 'Passwords do not match!'
                    else:
                        message = 'Minimum Length of password is 6.'
            else:
                message = 'Invalid Phone Number'

    return render_template('register.html', message=message)


@app.route("/login", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', (email, password, ))
        users = cursor.fetchone()
        if users:
            session['loggedin'] = True
            session['name'] = users['name']
            session['email'] = users['email']
            mesage = 'Logged in successfully !'
            return redirect(url_for('dashboard'))
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage=mesage)


@app.route('/dashboard')
def dashboard():
    if session.get('loggedin'):
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/myprofile', methods=['GET'])
def myprofile():
    if session.get('loggedin'):
        userProfile = ''
        if request.method == 'GET':
            emailId = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM users WHERE email= % s', (emailId, ))
            userProfile = cursor.fetchone()

        return render_template('myprofile.html', userProfile=userProfile)
    return redirect(url_for('login'))


def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        is_valid = phonenumbers.is_valid_number(parsed_number)

        if is_valid:
            formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
            return True, formatted_number
        else:
            return False, None

    except phonenumbers.phonenumberutil.NumberParseException:
        return False, None


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
