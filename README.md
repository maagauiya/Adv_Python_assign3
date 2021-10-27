# Authorization using jwt tokens (Flask)

**Installation**<br />
pip install flask<br />
pip install psycopg2<br />
pip install PyJWT <br />

**Usage**<br />
import psycopg2 as pos <br />
from datetime import datetime, timedelta <br />
from flask import Flask <br />
from flask.helpers import make_response <br />
from flask import request <br />
from flask.json import jsonify<br />
import jwt <br />

**Examples**<br />
for route /login
#You should enter your login and password on the "http://127.0.0.1:5000/login" page and you will get a token
#input
username: usernama1
password: password1
#output
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlcm5hbWUzIiwiZXhwIjoxNjM1MzU5MTkxfQ.GeiSBaYHmMQ-X6tT7KdEevnGOrY_1LACBgyHopg9nPM"
}
for route /protected
#You should pass a token on as a parameter then it will be check if this token in User table it output correct h1 tag:
#input 
http://127.0.0.1:5000/protected?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlcm5hbWUzIiwiZXhwIjoxNjM1MzU5MTkxfQ.GeiSBaYHmMQ-X6tT7KdEevnGOrY_1LACBgyHopg9nPM
#output
Hello, token which is provided is correct

