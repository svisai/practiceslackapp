from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
import os
import emoji

app = Flask(__name__)


# Configure the MySQL Server
# Configure the MySQL Server
app.mysql = MySQL()
app.config['MYSQL_USER'] = 'b496bd057a62f4'
app.config['MYSQL_PASSWORD'] = '283921dc'
app.config['MYSQL_DB'] = 'heroku_743551ffa3cefc4'
app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-04.cleardb.net'

app.mysql.init_app(app)


@app.route('/hello', methods=['POST'])
def hello():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM hi")

    data = cursor.fetchall()
    str = data[0]
    cursor.close()
    return emoji.emojize(':thumbs_up_sign:')


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)