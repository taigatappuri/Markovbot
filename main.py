import markovify
import tweepy
from requests_oauthlib import OAuth1Session
import html
import os
from dotenv import load_dotenv

load_dotenv()
post = True

API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

twitter = OAuth1Session(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
# ツイート用のapiアクセス先
input = open('./splitted.txt','r',encoding='utf-8')
model = markovify.NewlineText(input.read(),state_size=3)
sentence = model.make_sentence()

text = sentence.replace(" ","")
escaped_text = html.escape(text).replace('\n', '<br>')
print(escaped_text)
if post:
    client.create_tweet(text=escaped_text)
input.close()