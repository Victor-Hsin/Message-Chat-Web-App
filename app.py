from crypt import methods
from flask import Flask, request, session, redirect, url_for, render_template
from flaskext.mysql import MySQL
import pymysql 
import re 

app = Flask(__name__)
app.secret_key = "evou\x878\xa0\xe0FF\x8e~\x92\xf1xvCE\xe0\x15\x81\x17=\xf1"

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'messageApp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # connect to database
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # provide an error message if things go wrong
    msg = ''
    if request.method == "POST" and "username" in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # check whether those are valid username and password.
        cursor.execute("""
            SELECT user_id
              FROM user
             WHERE username = %s
               AND password = %s
        """, (username, password))
        user = cursor.fetchone()

        if user:
            session["loggedin"] = True
            session["id"] = user["user_id"]
            session["username"] = username
            return redirect(url_for("messagePage"))
        else:
            msg = "Incorrect username or password. Please try again."
    return render_template('login.html', msg=msg)


@app.route('/sign-up', methods=["POST"])
def signUp():
    # connect to database
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # provide an error message if things go wrong
    msg = ''
    if request.method == "POST" and "username" in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # check whether the username is already taken or not
        cursor.execute("""
            SELECT *
              FROM user
             WHERE username = %s
        """, (username))    
        user = cursor.fetchone()

        if user == None:
            cursor.execute("INSERT INTO user(username, password) VALUES(%s, %s)", (username, password)) 
            conn.commit()
            msg = "Sign up sucessfully! Please enter the username and password again to log in."
        else:
            msg = "This username was already taken. Please try another username."

    return render_template('login.html', msg=msg)


@app.route('/message-page', methods=["GET"])
def messagePage():
    if "loggedin" in session:
        return render_template('message-page.html')
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)