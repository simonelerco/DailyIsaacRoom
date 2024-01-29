import json

rooms = []

if __name__ == "__main__":
    with open("./scrambled_rooms.json", "r") as parsed:
        rooms = json.load(parsed)
        with open("./current_index.txt", "r+") as index:
            i = int(index.read())
            print(rooms[i][0]) # info data
            print(rooms[i][1]) # room

            # updating index in file
            i += 1
            index.seek(0)
            index.write(str(i))