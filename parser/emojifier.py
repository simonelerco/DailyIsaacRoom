
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
            return "🀄"
        
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
        case [3000, 0, 0]:
            # pit
            return "🕳️"
        case [291 | 9000 | 9100, 0, 0]:
            # exits
            return "🕳️"
        
        case [enemy, _, _] if enemy in enemies:
            # ANY enemy
            return enemy_identifier(entityType)

        case _:
            return ""
        
flies = [13, 14, 18, 25, 29, 61, 67, 80, 214, 222, 249, 281, 288, 296, 808, 819, 838, 868]
popcorns = [16, 22, 205, 310, 822]
maggots = [21, 23, 31, 77, 243, 810, 853, 855]
hosts = [27, 204, 247, 815, 859]
horsemen = [63, 64, 65, 66]
ghosts = [219, 260, 285, 816]
spiders = [85, 94, 100, 101, 206, 207, 215, 240, 241, 246, 250, 303, 304, 814, 818, 851, 869, 884, 900]
stone_shooters = [42, 202, 203, 235, 236, 302, 804, 809]
oomfies = [10, 35, 41, 53, 208, 209, 226, 228, 252, 257, 278, 283, 284, 297, 299,
           806, 807, 811, 813, 820, 821, 831, 834, 839, 841, 888, 889, 890, 891, 912]
bodies = [11, 34, 54, 210, 211, 280, 827, 843, 851, 858, 879]
heads = [12, 26, 86, 212, 248, 254, 286, 311, 812, 828]
def enemy_identifier(enemy):
    match enemy:
        case [fly, _, _] if fly in flies:
            return "🪰"
        case [popcorn, _, _] if popcorn in popcorns:
            return "🍿"
        case [maggot, _, _] if maggot in maggots:
            return "🐛"
        case [host, _, _] if host in hosts:
            return "💀"
        case [oomfie, _, _] if oomfie in oomfies:
            # technically gaper-likes, but generally enemies that follow the player
            # and have both a body and a head
            return "🧍"
        case [body, _, _] if body in bodies:
            return "🫥"
        case [head, _, _] if head in heads:
            return "😐"
        case [24, _, _]:
            # globins
            return "😡"
        case [29, 0 | 3, 0]:
            # these oomfs have spiders mixed in their category
            return "🫥"
        case [32 | 301 | 840, _, _]:
            # brain
            return "🧠"
        case [38 | 259, _, _]:
            # fetuses
            return "👶"
        case [39 | 836 | 865, _, _]:
            # vis
            return "🍑"
        case [shooter, _, _] if shooter in stone_shooters:
            return "🗿"
        case [46 | 87, _, _]:
            # sloth, gurgle
            return "🤢"
        case [57, 0, 0]:
            # big brain
            return "🧠"
        case [60 | 201, _, _]:
            # eyes
            return "👁"
        case [horseman, _, _] if horseman in horsemen:
            return "🏇"
        case [spider, _, _] if spider in spiders:
            return "🕷"
        case [92 | 98, _, _]:
            # heart (enemy)
            return "🫀"
        case [213 | 287, _, _]:
            # moms hand
            return "🫳"
        case [ghost, _, _] if ghost in ghosts:
            # wizoob, haunts
            return "👻"
        case [817, 1, 0]:
            # another ghost but other enemies mixed in the category
            return "👻"
        case [227 | 277 | 830, _, _]:
            # boneys
            return "☠"
        case [234 | 258 | 803, _, _]:
            # bats
            return "🦇"
        case [300, _, _]:
            # mushroom enemy
            return "🍄"
        case [306, _, _]:
            # portal
            return "🌀"
        
        case _:
            return "😠"