import pymongo
import pandas as pd

connection_url = "mongodb+srv://CS6400:CS6400@cluster0.frsk3.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_url)
db = client["test"]
table = db["NYTimes"]

website_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv"

df = pd.read_csv(website_url, header = 0)



# result_df =  df[df['date'] == '2020-01-21'] 
# result_df = result_df.set_index('state')
# result_df = result_df.drop('date', 1)
# result_df = result_df.to_dict('index')
# print(result_df)

#start date: 2020-01-21

for i in range(21,32):
    result_df =  df[df['date'] == '2020-01-{}'.format(i)] 
    result_df = result_df.set_index('state')
    result_df = result_df.drop('date', axis=1)
    object_df = result_df.to_dict('index')
    table.insert_one({"_id": "2020-01-{}".format(i),"data": object_df})

#2020-02 ~ 2020 -12

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(2, 13):
    for j in range(1, days_in_month[i - 1] + 1):
        temp = i
        if j < 10:
            j = "0{}".format(j)
        if i < 10:
            i = "0{}".format(i)
        result_df =  df[df['date'] == '2020-{}-{}'.format(i, j)] 
        result_df = result_df.set_index('state')
        result_df = result_df.drop('date', axis=1)
        object_df = result_df.to_dict('index')
        table.insert_one({"_id": "2020-{}-{}".format(i, j),"data": object_df})
        i = temp

#2021 - 01 ~ 2021 - 10
for i in range(1, 10):
    for j in range(1, days_in_month[i - 1] + 1):
        temp = i
        if j < 10:
            j = "0{}".format(j)
        if i < 10:
            i = "0{}".format(i)
        result_df =  df[df['date'] == '2021-{}-{}'.format(i, j)] 
        result_df = result_df.set_index('state')
        result_df = result_df.drop('date', axis=1)
        object_df = result_df.to_dict('index')
        table.insert_one({"_id": "2021-{}-{}".format(i, j),"data": object_df})
        i = temp

#2021 - 11 - 01 ~ 2021-11-17
for i in range(1,18):
    if i < 10:
        i = "0{}".format(i)
    result_df =  df[df['date'] == '2021-11-{}'.format(i)] 
    result_df = result_df.set_index('state')
    result_df = result_df.drop('date', axis=1)
    object_df = result_df.to_dict('index')
    table.insert_one({"_id": "2021-11-{}".format(i),"data": object_df})

