import json
import tweepy
import schedule
import time
import random
import os
from dotenv import load_dotenv

rooms = []
room = []

load_dotenv()

api_key=os.getenv('API_KEY')
api_secret=os.getenv('API_SECRET')
bearer=os.getenv('BEARER')
access=os.getenv('ACCESS')
access_secret=os.getenv('ACCESS_SECRET')

client = tweepy.Client(bearer, api_key, api_secret, access, access_secret)

def get_random_room():
    room = []
    with open("./parsed_rooms.json", "r") as parsed:
        rooms = json.load(parsed)

        i = random.randrange(0, len(rooms))
        room = rooms[i]
        print(rooms[i][0]) # info data
        print(rooms[i][1]) # room

        return room

def job():
    scheduled_room = get_random_room()
    new_tweet = client.create_tweet(text=scheduled_room[1])
    while new_tweet.data == None:
        time.sleep(3)
    print(new_tweet.data)
    new_reply = client.create_tweet(text=scheduled_room[0], in_reply_to_tweet_id=new_tweet.data['id'])


if __name__ == "__main__":
    schedule.every().day.at("00:00", "Europe/Amsterdam").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)