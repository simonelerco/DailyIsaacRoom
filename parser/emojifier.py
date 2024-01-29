
# range for pattern matching
chests = range(50, 61)
rocks = [1000, 1001, 1008, 1009, 1010, 1011]
poops = range(1494, 1502)
enemies = range(10, 952)


def entity_to_emoji(entity):
    # cleanup
    entityType = [int(n) for n in entity["type_combined"].split(".")]
    match entityType:
        case [5, 10, variant]:
            # hearts
            match variant:
                case 3:
                    # spirit heart
                    return "💙"
                case 10:
                    # eternal heart
                    return "🤍"
                case 7:
                    # gold heart
                    return "💛"
                case 6:
                    # black heart
                    return "🖤"
                case _:
                    # any other heart
                    return "❤️"
        case [5, 20, _]:
            # coin
            return "🪙" 
        case [5, 30, _]:
            # key
            return "🔑"
        case [5, 40, _]:
            # bomb
            return "💣"
        case [5, chest, _] if chest in chests:
            # chest
            return "🧰"
        case [5, 300, _]:
            # cards, runes, souls...
            return "🃏"
        case [5, 301, _]:
            # random rune
            return "🃏"
        case [5, 360, _]:
            # red chest
            return "🧰"
        case [5, 380, 0]:
            # bed
            return "🛏"
        case [5, 70, _]:
            # pill
            return "💊"
        case [5, 90, _]:
            # battery
            return "🔋"
        case [5, 100 | 150, _]:
            # random item
            return "❔"
        case [5, 340 | 370, 0]:
            # big chest and trophy
            return "🏆"
        case [5, 350, _]:
            # trinkets
            return "🟰"
        
        case [1002, _, _]:
            # pot
            return "🫖"
        case [rock, 0, _] if rock in rocks:
            # rocks
            return "🪨"
        case [1300, 0, 0]:
            # TNT
            return "🛢️"
        case [poop, _, _] if poop in poops:
            # poop
            return "💩"
        case [33, _, _]:
            # fire
            return "🔥"
        case [1930 | 1931, _, _]:
            # spikes
            return "🍴"
        case [6, _, _]:
            # beggars and slot machines
            return "🎰"
        case [17, _, _]:
            # keepers
            return "🤑"
        case [5000, 0, 0]:
            # devil statue
            return "😈"
        case [5001, 0, 0]:
            # angel statue
            return "👼"
        case [291 | 9000 | 9100, 0, 0]:
            # exits
            return "🕳"
        
        case [enemy, _, _] if enemy in enemies:
            # ANY enemy
            return "😠"

        case _:
            return ""