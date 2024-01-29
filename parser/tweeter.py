import json
import tweepy
import schedule
import time
import random

rooms = []
room = []

api_key="1rIas53qHLr3qjt8ZBdoGE3qU"
api_secret="aSAuxCiZVzB32r6amysK1Tis6C2jB2DpRk5XUoiEiThCqMT9Fv"
bearer=r"AAAAAAAAAAAAAAAAAAAAANyRsAEAAAAAsM1KjdxaTRTz3chsMr0oXLL5XPA%3DNVpdgTvlH2CWTaChSbLUznQwvtkMpQInoVrukegl5wNwrob4EF"
access="1530283296512479232-b0ZlhlfCFBDz33o6sXOR70Z0H8gpkg"
access_secret="tLcDfsFrL6LV1NNh9zwKdYJ0ZnCQqTDGeLqPORKTdMzYN"

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