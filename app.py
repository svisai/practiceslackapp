from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os

app = Flask(__name__)


# Configure the MySQL Server
app.mysql = MySQL()


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    return "hi";


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)