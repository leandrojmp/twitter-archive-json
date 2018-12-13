import json
import os
from sys import argv

# input and output files

js_file = argv[1]
json_file = os.path.basename(js_file).split('.')[0] + '.json'

# first tests, pass the file as an argument
with open(js_file,'r') as j_file:
    discard = next(j_file)
    j_data = json.loads(j_file.read())

with open(json_file,'a') as out_file:
    for i in j_data:
        geo = True
        tweet_id = i['id']
        timestamp = i['created_at']
        source = i['source'].split('>')[1].split('<')[0].lower()
        tweet = i['text'].replace('\n','').replace('"','').replace('\'','')
        tweet_lenght = len(tweet)
        if tweet[:1] == "@":
            tweet_type = "reply"
        elif tweet[:3] == "RT ":
            tweet_type = "retweet"
        else:
            tweet_type = "tweet"
        try:
            try_geo = i['geo']['coordinates']
        except KeyError:
            geo = False
        if geo:
            geolocation = i['geo']['coordinates']
            print('{\"timestamp\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.source\":\"%s\",\"tweet.geo\":%s}' % (timestamp, tweet_id, tweet, tweet_type, tweet_lenght, source, geolocation),file=out_file)
        else:
            print('{\"timestamp\":\"%s\",\"tweet.id\":\"%s\",\"tweet.text\":\"%s\",\"tweet.type\":\"%s\",\"tweet.length\":%d,\"tweet.source\":\"%s\"}' % (timestamp, tweet_id, tweet, tweet_type, tweet_lenght, source),file=out_file)