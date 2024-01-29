import emojifier

def pos_to_idx(x, y, width):
    return ((y * width) + x)

def extract_room_info(room):
    room_info = {
        "variant"   : room["variant"],
        "name"      : room["name"],
        "type"      : room["type"],
        "subtype"   : room["subtype"],
        "shape"     : room["shape"],
        "width"     : room["width"],
        "height"    : room["height"],
        "difficulty": room["difficulty"],
        "weight"    : room["weight"]
    }
    return room_info

def extract_door_info(room):
    doors_clean = []
    doors = room.find_all("door", exists="True")
    for door in doors:
        # this madman made door positions at negative numbers
        door_info = {
            "pos_x": int(door["x"]) + 1,
            "pos_y": int(door["y"]) + 1
        }
        doors_clean.append(door_info)
    return doors_clean

def extract_entity_info(spawns):
    entities = []
    for spawn in spawns:
        entity_list = spawn.find_all("entity")
        for entity in entity_list:
            entity_info = {
                "pos_x": int(entity.parent["x"]) + 1,
                "pos_y": int(entity.parent["y"]) + 1,
                "type_combined": entity["type"] + "." + entity["variant"] + "." + entity["subtype"],
                "weight": entity["weight"]
            }
            entities.append(entity_info)
    return entities

def entities_to_emoji(entities):
    for entity in entities:
        entity["emoji"] = emojifier.entity_to_emoji(entity)

def build_room(room_info, doors, floor):
    room = []
    tile = ""
    width = int(room_info["width"]) + 2
    height = int(room_info["height"]) + 2
    floor = int(floor)

    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                match floor:
                    case 3:
                        tile = "🟧"
                    case 10 | 11 | 12:
                        tile = "🟥"
                    case 6 | 15:
                        tile = "🟦"
                    case 14 | 16:
                        tile = "⬛"
                    case 17:
                        tile = "🟨"
                    case _:
                        tile = "🟫"
            else:
                match floor:
                    case 15:
                        tile = "⬜"
                    case 14 | 16 | 17:
                        tile = "🟫"
                    case _:
                        tile = "⬛"
            room.append(tile)

    for door in doors:
        room[pos_to_idx(door["pos_x"], door["pos_y"], width)] = "🚪"

    return room


def populate_room(room, entities, room_info):
    width = int(room_info["width"]) + 2
    height = int(room_info["height"]) + 2
    pop_room = room

    for entity in entities:
        if entity["emoji"] != "":
            pop_room[pos_to_idx(entity["pos_x"], entity["pos_y"], width)] = entity["emoji"]

    return pop_room

def stringify_room(room, room_info):
    width = int(room_info["width"]) + 2
    room_str = ""

    chunks = [room[i:i + width] for i in range(0, len(room), width)]
    for chunk in chunks:
        room_str += "".join(chunk)
        room_str += "\n"

    return room_str

def parse_room(room, filename):
    room_info = extract_room_info(room)
    doors = extract_door_info(room)
    spawns = room.find_all("spawn")
    entities = extract_entity_info(spawns)
    entities_to_emoji(entities)
    built_room = build_room(room_info, doors, filename.split(".")[0])
    populated_room = populate_room(built_room, entities, room_info)
    room_str = stringify_room(populated_room, room_info)

    info = "Floor: " + filename.split(".")[1].title() + "\n"
    info += "Variant: " + room_info["variant"] + " Difficulty: " + room_info["difficulty"] +" Weight: " + room_info["weight"] + "\n"
    info_list = [info, room_str]

    print(info)
    
    return info_list