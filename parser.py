# parser.py
# 
# parse the tweet archive file, each tweet will be in one line
#
# usage: parse.py /path/to/tweet.js
# the output is saved as json/tweet.js

import json
import os
import datetime
import calendar
from sys import argv

# input and output files
src_file = open(argv[1],'r') 
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
        json.dump(tweet,dst_file)
        dst_file.write('\n')