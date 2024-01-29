from bs4 import BeautifulSoup
import progressbar
import os
import json

import utils

parsed_rooms = []

def main():
    for filename in os.listdir("../resources/"):
        with open(os.path.join("../resources/" + filename)) as file:
            soup = BeautifulSoup(file, features="lxml-xml")
            rooms = soup.find_all("room", width="13", height="7")
            with progressbar.ProgressBar(redirect_stdout=True, max_value=len(rooms)) as bar:
                for i in range(len(rooms)):
                    parsed_rooms.append(utils.parse_room(rooms[i], filename))
                    bar.update(i)
                
    with open("./parsed_rooms.json", "w") as output_file:
        json.dump(parsed_rooms, output_file)

if __name__ == "__main__":
    main()