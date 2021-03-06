from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from flaskext.mysql import MySQL
import pymysql 
import time

app = Flask(__name__)
app.secret_key = "evou\x878\xa0\xe0FF\x8e~\x92\xf1xvCE\xe0\x15\x81\x17=\xf1"

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'messageApp'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

def createTables():
    # connect to database
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                user_id int(20) NOT NULL AUTO_INCREMENT,
                username varchar(45) NOT NULL,
                password varchar(45) NOT NULL,
                PRIMARY KEY (user_id)
            )
        """)  
        conn.commit()
    except: 
        print("**************Fail to create user table!!!***************")  
    

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS message (
                message_id int(20) NOT NULL AUTO_INCREMENT,
                user_id int(20) NOT NULL,
                creation_date datetime NOT NULL,
                message text,
                PRIMARY KEY (message_id),
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            )
        """)    
        conn.commit()
    except: 
        print("**************Fail to create message table!!!***************") 
    


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
            session["userId"] = user["user_id"]
            session["username"] = username
            return redirect(url_for("messagePage"))
        else:
            msg = "Incorrect username or password. Please try again."
    return render_template('login.html', msg=msg)


@app.route('/logout', methods=['GET'])
def logOut():
    # remove session variables
    session.pop("loggedin", None) 
    session.pop("userId", None)
    session.pop("username", None)
    return render_template('login.html')


@app.route('/sign-up', methods=["POST"])
def signUp():
    # connect to database
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # output an message for whether things go wrong
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


@app.route('/messages', methods=['GET', 'POST'])
def messages():
    # connect to database
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    msg = ""
    if request.method == "POST":
        requestData = request.get_json()
        if "userId" in requestData and "message" in requestData:
            userId = requestData['userId']
            inputMessage = requestData['message']
            currTime = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO message(user_id, creation_date, message) VALUES(%s, %s, %s)", (userId, currTime, inputMessage))
            conn.commit()
            msg = "sucess"
        else:
            msg = "userId or username data was not provided."
        return jsonify({"message": msg})
    elif request.method == "GET":
        cursor.execute("""
            SELECT u.username, m.message
              FROM message AS m
                   INNER JOIN user AS u
                   ON m.user_id = u.user_id
          ORDER BY m.creation_date
        """)
        userMessages = cursor.fetchall()
        return jsonify({"userMessages": userMessages})



if __name__ == '__main__':
    createTables()
    app.run(debug=True, host='0.0.0.0', port=5000)