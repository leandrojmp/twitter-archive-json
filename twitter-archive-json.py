import json
from sys import argv

# first tests, pass the file as an argument
with open(argv[1],'r') as jfile:
    discard = next(jfile)
    jdata = json.loads(jfile.read())
