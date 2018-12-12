import json
from sys import argv

# first tests, pass the file as an argument
with open(argv[1],'r') as jfile:
    discard = next(jfile)
    jdata = json.loads(jfile.read())

with open('out.json','a') as out_file:
    for i in jdata:
        geo = True
        timestamp = i['created_at']
        tweet = i['text'].replace('\n','')
        tweet = tweet.replace('"','')
        tweet = tweet.replace('\'','')
        try:
            try_geo = i['geo']['coordinates']
        except KeyError:
            geo = False
        if geo:
            geolocation = i['geo']['coordinates']            
            print('{\"timestamp\":\"%s\",\"tweet.text\":\"%s\",\"tweet.geo\":%s}' % (timestamp, tweet, geolocation),file=out_file)
        else:
            print('{\"timestamp\":\"%s\",\"tweet.text\":\"%s\"}' % (timestamp, tweet),file=out_file)