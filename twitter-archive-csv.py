import json
import os
from sys import argv

# input and output files

src_dir = argv[1]
#js_file = argv[1]

for f in os.listdir(src_dir):
    csv_file = 'csv/' + os.path.basename(f).split('.')[0] + '.csv'
    # first tests, pass the file as an argument
    with open(src_dir + f,'r') as j_file:
        discard = next(j_file)
        j_data = json.loads(j_file.read())

    with open(csv_file,'a') as out_file:
        for i in j_data:
            tweet_id = i['id']
            timestamp = i['created_at']
            source = i['source'].split('>')[1].split('<')[0].lower()
            tweet = i['text'].replace('\n','').replace('"','').replace('\'','').replace('\\','')
            tweet_length = len(tweet)
            if tweet[:1] == "@":
                tweet_type = "reply"
            elif tweet[:3] == "RT ":
                tweet_type = "retweet"
            else:
                tweet_type = "tweet"
            print('%s;%s;%s;%d;%s' % (timestamp, tweet_id, tweet_type, tweet_length, source),file=out_file)