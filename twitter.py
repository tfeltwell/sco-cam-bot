import oauth2 as oauth
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

def getTimeline():
	url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
	http_method="GET"
	post_body=""
	http_headers=None
	resp, data = client.request(url, method=http_method, body=post_body, headers=http_headers)
	tweets = json.loads(data)
	return data

def tweet(tweet):
	url='https://api.twitter.com/1.1/statuses/update.json'
	http_method="POST"
	post_body="status="+str(tweet)
	http_headers=None
	resp, data = client.request(url, method=http_method, body=post_body, headers=http_headers)
	return data

#Get timeline
tweets = getTimeline()
for i, tweet in enumerate(tweets):
    print i

# Post a tweet
errors = tweet("Hello world!")

