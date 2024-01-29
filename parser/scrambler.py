import json
import random

rooms = []

if __name__ == "__main__":
    with open("./parsed_rooms.json", "r") as parsed:
        rooms = json.load(parsed)
        random.shuffle(rooms)
        with open("./scrambled_rooms.json", "w") as output_file:
            json.dump(rooms, output_file)