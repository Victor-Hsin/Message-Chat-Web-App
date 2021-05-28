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
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # connect to database

    if request.method == "GET":
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)