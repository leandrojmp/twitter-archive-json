# twitter-archive-parser

scripts to convert the `.js` files containing your tweets from your twitter archive into `.json` files that can be pushed into `elasticsearch` for analysis and search.

the tweets `.js` files is named `tweet.js`, depending on your tweet count you could have more files named `tweet-partX.js`, those files are located in the root leve on the directory where you extract zip file with your archive.

*ps:* the twitter archive used to be a collection of `.js` files organized by year and month, somewhere between the end of 2018 and the beginning of 2019 twitter changed the way it shares your archive and now all the tweets are in one or more files.
