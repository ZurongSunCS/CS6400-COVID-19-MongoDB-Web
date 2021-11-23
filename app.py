from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xeeL\xbf\x8ec=\xff\xb0d}\xbc\x91\x94r\xc7L'
# Database
#client = pymongo.MongoClient('localhost', 27017)
#db = client.user_login_system

#Routes
from user import routes

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/embeded')
def embeded():
    return render_template('index.html')

@app.route('/embeded2')
def embeded2():
    return render_template('index2.html')