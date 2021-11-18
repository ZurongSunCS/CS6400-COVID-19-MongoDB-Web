import pymongo
import pandas as pd

connection_url = "mongodb+srv://CS6400:CS6400@cluster0.frsk3.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_url)
db = client["test"]
table = db["JHU"]


# website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv"
# df = pd.read_csv(website_url, header=0)
# df = df.set_index('Province_State')

# object_df = df.to_dict('index')

# table.insert_one({"_id": "2021-01-01", "data": object_df})



# start data: 2020-4-12

for i in range(12, 31):
    website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/04-{}-2020.csv".format(i)
    df = pd.read_csv(website_url, header = 0)
    df = df.set_index('Province_State')
    object_df = df.to_dict('index')
    table.insert_one({"_id": "2020-04-{}".format(i),"data": object_df})

# 2020-5 ~ 2020 - 12
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(5, 13):
    for j in range(1, days_in_month[i - 1] + 1):
        temp = i
        if j < 10:
            j = "0{}".format(j)
        if i < 10:
            i = "0{}".format(i)
        website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}-{}-2020.csv".format(i,j)
        df = pd.read_csv(website_url, header = 0)
        df = df.set_index('Province_State')
        object_df = df.to_dict('index')
        table.insert_one({"_id": "2020-{}-{}".format(i, j),"data": object_df})
        i = temp

# 2021-1 ~ 2021-10

for i in range(1, 11):
    for j in range(1, days_in_month[i - 1] + 1):
        temp = i
        if j < 10:
            j = "0{}".format(j)
        if i < 10:
            i = "0{}".format(i)
        website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}-{}-2021.csv".format(i,j)
        df = pd.read_csv(website_url, header = 0)
        df = df.set_index('Province_State')
        object_df = df.to_dict('index')
        table.insert_one({"_id": "2021-{}-{}".format(i, j),"data": object_df})
        i = temp

# 2021-11-1 ~ 2021-11-17
for i in range(1, 18):
        if i < 10:
            i = "0{}".format(i)
        website_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/11-{}-2021.csv".format(i)
        df = pd.read_csv(website_url, header = 0)
        df = df.set_index('Province_State')
        object_df = df.to_dict('index')
        table.insert_one({"_id": "2021-11-{}".format(i),"data": object_df})