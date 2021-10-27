import psycopg2 as pos
from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
con=pos.connect("dbname=python_ass3 user=postgres password=magauiyainc")
cur=con.cursor()
# cur.execute("CREATE TABLE usertable (id int PRIMARY KEY, login varchar(16), password varchar(16),token varchar(200));")
# cur.execute("insert into usertable(id,login,password) values ('1','username1','password1'),('2','username2','password2'),('3','username3','password3');")
# con.commit()


@app.route('/protected')
def protected():
    token=request.args.get('token')
    cur.execute("select *from usertable")
    user_records=cur.fetchall()
    for i in user_records:
        if i[3]==str(token):
            return '''<h1>Hello, token which is provided is correct </h1>'''
    return '''<h1>Hello, Could not verify the token </h1>'''

    
@app.route('/login')
def login():
    auth = request.authorization
    cur.execute("select *from usertable")
    user_records=cur.fetchall()
    for i in user_records:
        if auth and auth.username==i[1] and auth.password == i[2]:
            token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            cur.execute("""update usertable set token=%s where login like %s;""",(token,i[1]) )
            con.commit()
            return jsonify({'token': token})
        return make_response('Could not found a user with login:f{i[1]}', 401,{'WWW-Authenticate': 'Basic realm="Login required'})


if __name__ == '__main__':
    app.run(debug=True)
