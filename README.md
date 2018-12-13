# twitter-archive-json

scripts to convert the `.js` files from your twitter archive into `.json` files that can be pushed into `elasticsearch` for analysis and search.

the `.js` files are located in the `./data/js/tweets/` directory, inside the directory where the zip file was unzipped.

if you remove the first line in each of these files, it becomes a file with a `JSON Array` where each `JSON Object` in this array is a tweet, this script removes the first line of each file and loads the rest of the file into a `list`, where each item is a tweet, then it will iterate on the `list` and extract some fields.

at this moment i'm working with the following fields:

| python list name| json field name | description|
|---|---|---|
|`list_name[index]['source']`|`tweet.source`|the source client of the tweet|     
|`list_name[index]['id']`|`tweet.id`|the id of the tweet|
|`list_name[index]['created_at']`|`timestamp`|the timestamp of the tweet|
|`list_name[index]['geo']['coordinates']`|`tweet.geo`|the geo point with latitude and longitude|
|`list_name[index]['text']`|`tweet.text`|the full text of the tweet|

two new fields are created:

- `tweet.type`: can have the value of `tweet`, `reply` or `retweet` based on `tweet.text`
- `tweet.length`: the length of `tweet.text`