import json
import os
import datetime
import calendar
from sys import argv

# input and output files

src_dir = argv[1]

# create days and months lists
days = list(calendar.day_name)
months = list(calendar.month_name)

for f in os.listdir(src_dir):
    json_file = 'json/' + os.path.basename(f).split('.')[0] + '.json'
    # first tests, pass the file as an argument
    with open(src_dir + f,'r') as j_file:
        next(j_file)
        j_data = json.loads(j_file.read())

    with open(json_file,'a') as out_file:
        for i in j_data:
            tweets = {}
            tweet_users = []
            tweets['tweet.id'] = str(i['id'])
            tweets['tweet.timestamp'] = i['created_at']
            # create a date time variable to extract the year, the day of week and the month
            tweet_date = datetime.datetime.strptime(tweets['tweet.timestamp'], '%Y-%m-%d %H:%M:%S +0000')
            tweets['tweet.year'] = tweet_date.year
            tweets['tweet.day'] = days[tweet_date.weekday()].lower()
            tweets['tweet.month'] = months[tweet_date.month].lower()
            # 
            tweets['tweet.source'] = i['source'].split('>')[1].split('<')[0].lower()
            tweet = i['text'].replace('\n','').replace('"','').replace('\'','').replace('\\','')
            tweets['tweet.length'] = len(tweet)
            tweets['tweet.text'] = tweet
            if tweet[:1] == "@":
                tweets['tweet.type'] = "reply"
            elif tweet[:3] == "RT ":
                tweets['tweet.type'] = "retweet"
            else:
                tweets['tweet.type'] = "tweet"
            if tweets['tweet.type'] == "reply":
                for u in tweet.split():
                    if u[0] == "@":
                        tweet_users.append(u)
                tweets['tweet.users'] = tweet_users
            if "coordinates" in i['geo']:
                geo_lat = i['geo']['coordinates'][0]
                geo_lon = i['geo']['coordinates'][1]
                tweets['tweet.geo'] = str(geo_lat) + "," + str(geo_lon)
            
            json.dump(tweets, out_file)
            out_file.write('\n')
