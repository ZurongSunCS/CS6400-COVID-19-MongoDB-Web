from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xeeL\xbf\x8ec=\xff\xb0d}\xbc\x91\x94r\xc7L'


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
    return render_template('HomePage.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/Confirmed_Case')
def Confirmed_Case():
    return render_template('Confirmed_Case.html')

@app.route('/Recovered_Case')
def Recovered_Case():
    return render_template('Recovered_Case.html')

@app.route('/Death_Case')
def Death_Case():
    return render_template('Death_Case.html')

