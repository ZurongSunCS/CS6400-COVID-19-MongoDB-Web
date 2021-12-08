from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
import pandas as pd
import datetime

app = Flask(__name__)
app.secret_key = b'\xeeL\xbf\x8ec=\xff\xb0d}\xbc\x91\x94r\xc7L'

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
    connection_url = "mongodb+srv://CS6400:CS6400@cluster0.frsk3.mongodb.net/test?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["test"]
    table = db["JHU-test"]
    today = datetime.date.today() - datetime.timedelta(days=2)
    print(today)
    with open('updatedDay.txt') as f:
        lines = f.readlines()
    
    last_day = datetime.date(int(lines[0].split("-")[0]), int(lines[0].split("-")[1]), int(lines[0].split("-")[2]))
    last_day = last_day + datetime.timedelta(days=1)
    run_day = last_day
    while run_day <= today:
        if (run_day.month < 10) :
            month = "0" + str(run_day.month)
        else:
            month = run_day.month
        if (run_day.day < 10):
            day = "0" + str(run_day.day)
        else:
            day = run_day.day
        website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}-{}-{}.csv".format(month, day, run_day.year)
        df = pd.read_csv(website_url, header = 0)
        df['Date']="{}-{}-{}".format(run_day.year, month, day)
        d = df.to_dict(orient='index')
        for m in range (len(d)):
            table.insert_one(d[m])
        run_day += datetime.timedelta(days=1)

    table = db["NYTimes-test"]
    website_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv"
    df = pd.read_csv(website_url, header = 0)
    d = df.to_dict(orient='index')

    for m in range (len(d)):
        this_date = d[m]['date']
        this_date_reformat = datetime.date(int(this_date.split("-")[0]), int(this_date.split("-")[1]), int(this_date.split("-")[2]))
        if ((this_date_reformat >= run_day) & (this_date_reformat <= today)):
            table.insert_one(d[m])

    f = open("updatedDay.txt", "w")
    f.write("{}-{}-{}".format(today.year, today.month, today.day))
    f.close()


    return render_template('HomePage.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/1point3acres_Confirmed_Case')
def Confirmed_Case():
    return render_template('1point3acres_Confirmed_Case.html')

@app.route('/1point3acres_Recovered_Case')
def Recovered_Case():
    return render_template('1point3acres_Recovered_Case.html')

@app.route('/1point3acres_Death_Case')
def Death_Case():
    return render_template('1point3acres_Death_Case.html')

@app.route('/JHU_Confirmed_Case')
def JHU_Confirmed():
    return render_template('JHU_Confirmed_Case.html')

@app.route('/JHU_Death_Case')
def JHU_Death():
    return render_template('JHU_Death_Case.html')

@app.route('/New_York_Time_Confirmed_Case')
def New_York_Confirmed():
    return render_template('New_York_Time_Confirmed_Case.html')

@app.route('/Sources')
def Sources():
    return render_template('Sources.html')

@app.route('/1point3acres')
def point3acres():
    return render_template('1point3acres.html')

@app.route('/JHU')
def JHU():
    return render_template('JHU.html')

@app.route('/New_York_Time')
def NYT():
    return render_template('New_York_Time.html')

@app.route('/MongoDBLineGraph')
def MongoDB():
    return render_template('MongoDB_Line_Graph.html')

@app.route('/MongoDB_JHU')
def MongoDB_JHU():
    return render_template('MongoDB_JHU.html')
