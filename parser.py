# parser.py
# 
# parse the tweet archive file, each tweet will be in one line
#
# usage: parse.py -e 0 /path/to/tweet.js
# the output is saved as json/tweet.js

import json
import os
import argparse

# arguments
options = argparse.ArgumentParser(description="twitter archive parser")

options.add_argument (
    '-e',
    default=0,
    help='parse the entities fields, 1 will parse, 0 will not parse (default: 0)'
)

options.add_argument (
    'file',
    help='filename to parse'
)

args = options.parse_args()

# input and output files
src_file = open(args.file,'r') 
parsed_file = 'json/' + os.path.basename(str(src_file)).split('.')[0] + '.json'

# need to skip the first 25 characters on each file
# the first 25 chars are something like: window.YTD.tweet.part0 = [
src_file.seek(25)

# reads the file and parse the json
archive_data = src_file.read()
json_data = json.loads(archive_data)
# save each tweet as a line in the output file
with open(parsed_file,'a') as dst_file:
    for tweet in json_data:
        # if -e 0 or not present, do not parse the entities and extended_entities fields
        if args.e == 0:
            tweet['tweet'].pop("entities", None)
            tweet['tweet'].pop("extended_entities", None)
        tweet['tweet']['source'] = tweet['tweet']['source'].split('>')[1].split('<')[0]
        tweet['tweet']['tweet_length'] = len(tweet['tweet']['full_text'])
        # check the type of the tweet
        if tweet['tweet']['full_text'][:1] == "@":
            tweet['tweet']['tweet_type'] = "reply"
        elif tweet['tweet']['full_text'][:3] == "RT ":
            tweet['tweet']['tweet_type'] = "retweet"
        else:
            tweet['tweet']['tweet_type'] = "tweet"
        # check if the tweet has the geo field and convert it to string
        if "geo" in tweet['tweet']:
            geo_str = str(tweet['tweet']['geo']['coordinates'][0]) + "," + str(tweet['tweet']['geo']['coordinates'][1])
            tweet['tweet']['geo']['coordinates'] = geo_str
            tweet['tweet'].pop("coordinates", None)
        json.dump(tweet,dst_file)
        dst_file.write('\n')