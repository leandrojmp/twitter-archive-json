import json
import os
import datetime
import calendar
from sys import argv

# input and output files

src_dir = argv[1]
#js_file = argv[1]

# create days and months lists
days = list(calendar.day_name)
months = list(calendar.month_name)

for f in os.listdir(src_dir):
    json_file = 'json/' + os.path.basename(f).split('.')[0] + '.json'
    # first tests, pass the file as an argument
    with open(src_dir + f,'r') as j_file:
        discard = next(j_file)
        j_data = json.loads(j_file.read())

    with open(json_file,'a') as out_file:
        for i in j_data:
            tweet_users = []
            tweet_id = i['id']
            timestamp = i['created_at']
            # create a date time variable to extract the year, the day of week and the month
            tweet_date = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S +0000')
            tweet_year = tweet_date.year
            tweet_day = days[tweet_date.weekday()].lower()
            tweet_month = months[tweet_date.month].lower()
            # 
            source = i['source'].split('>')[1].split('<')[0].lower()
            tweet = i['text'].replace('\n','').replace('"','').replace('\'','').replace('\\','')
            tweet_length = len(tweet)
            if tweet[:1] == "@":
                tweet_type = "reply"
            elif tweet[:3] == "RT ":
                tweet_type = "retweet"
            else:
                tweet_type = "tweet"
            if tweet_type == "reply":
                for u in tweet.split():
                    if u[0] == "@":
                        tweet_users.append(u)
            if "coordinates" in i['geo']:
                geo_lat = i['geo']['coordinates'][0]
                geo_lon = i['geo']['coordinates'][1]
                geolocation = str(geo_lat) + "," + str(geo_lon)
                if tweet_users:
                    print('{\"tweet.timestamp\":\"%s\",\"tweet.year\":\"%d\",\"tweet.day\":\"%s\",\"tweet.month\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.users\":\"%s\",\"tweet.source\":\"%s\",\"tweet.geo\":\"%s\"}' % (timestamp, tweet_year, tweet_day, tweet_month, tweet_id, tweet, tweet_type, tweet_length, tweet_users, source, geolocation),file=out_file)
                else:
                    print('{\"tweet.timestamp\":\"%s\",\"tweet.year\":\"%d\",\"tweet.day\":\"%s\",\"tweet.month\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.source\":\"%s\",\"tweet.geo\":\"%s\"}' % (timestamp, tweet_year, tweet_day, tweet_month, tweet_id, tweet, tweet_type, tweet_length, source, geolocation),file=out_file)
            else:
                if tweet_users:
                    print('{\"tweet.timestamp\":\"%s\",\"tweet.year\":\"%d\",\"tweet.day\":\"%s\",\"tweet.month\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.users\":\"%s\",\"tweet.source\":\"%s\"}' % (timestamp, tweet_year, tweet_day, tweet_month, tweet_id, tweet, tweet_type, tweet_length, tweet_users, source),file=out_file)
                else:
                    print('{\"tweet.timestamp\":\"%s\",\"tweet.year\":\"%d\",\"tweet.day\":\"%s\",\"tweet.month\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.source\":\"%s\"}' % (timestamp, tweet_year, tweet_day, tweet_month, tweet_id, tweet, tweet_type, tweet_length, source),file=out_file)