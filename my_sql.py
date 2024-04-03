from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "database-1.clm00secym6r.ap-south-1.rds.amazonaws.com"
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "7416252855aA"
app.config['MYSQL_DB'] = "Authentication"


mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Persons''')
    data = cur.fetchall()
    cur.close()
    print(data)
    return {"Data" : data}
    # return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


