#Tera Donica

import time

class Player:
    def __init__(self, items=None):
        self.items = items
        self.alive = True
        self.room = None
        self.win = False
        self.intro = None

    def move(self, direction):
        """Causes the player to move between rooms. Assume 'direction' parameter is a player-inputted string.
         This method accepts the words north, south, east, and west in any case."""

        self.room = eval(f'self.room.{direction.lower().strip()}')
        print(f'You moved to {self.room}.')


class Room:
    def __init__(self, room_name='notNamed', item=None, enemy=None, room_text=None):
        self.name = room_name
        self.item = item
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.enemy = enemy
        self.text = room_text

    def __str__(self):
        return self.name

    def status(self):
        out_str = f'Room: {self.name}'
        if self.item is not None:
            out_str += f', Item: {self.item}'

        if self.enemy is not None:
            out_str += f', Enemy: {self.enemy}'

        if self.north is not None:
            out_str += f', North: {self.north}'

        if self.south is not None:
            out_str += f', South: {self.south}'

        if self.east is not None:
            out_str += f', East: {self.east}'

        if self.west is not None:
            out_str += f', West: {self.west}'

        print(out_str)

class Item:
    def __init__(self, name='notNamed', item_text=None):
        self.name = name
        self.text = item_text

    def __str__(self):
        return self.name

    def status(self):
       print(f'Item: {self.name}')

class Enemy:
    def __init__(self, name='notNamed', defeat_items = None, intro_text = None, fight_text = None, death_text = None):
        self.name = name
        self.defeat_items = defeat_items
        self.intro_text = intro_text
        self.fight_text = fight_text
        self.death_text = death_text
        self.alive = True

    def __str__(self):
        return self.name

    def status(self):
        out_str = f'Enemy: {self.name}'

        if self.alive:
            out_str += ' (alive)'
        else: out_str += ' (dead)'

        print(out_str)

    def fight(self, player):
        """This method both narrates the battle and returns the result.
        Returns True if player wins, False otherwise."""

        if self.alive:
            if self.defeat_items is not None:
                for item in self.defeat_items:
                    if item in player.items:
                        for line in self.fight_text[item]["True"]:
                            print(line)
                            time.sleep(1)
                        print()
                        time.sleep(0.5)
                        continue
                    else:
                        for line in self.fight_text[item]["False"]:
                            print(line)
                            time.sleep(1)
                        print()
                        time.sleep(0.5)
                        return False
                else: return True
            else: return True
        else: return True

if __name__ == '__main__':

    #Read level data from file
    #TODO: add a menu that reads level data from user input
    #level_file = 'alchemistsMistake.json'
    #with open(level_file, 'r') as level:
    #    level_data = json.load(level)

    level_data = {
        "players": {
            "ryan": {
                "starting_items": ["None"],
                "starting_room": "lobby",
                "intro":
                    [
                        "The Alchemist's Mistake",
                        " --an adventure game--",
                        "    by Tera Donica  ",
                        "",
                        "You get called to deal with a particular kind of problem.",
                        "The violent kind, usually.",
                        "",
                        "In this case, you've been asked to deal with a problem",
                        "at Lab Inc.",
                        "",
                        "When you enter the building, you see an elderly man in a",
                        "lab coat. His name tag identifies him as Dr. Shultz. He",
                        "seems to be the only one left in the building, and he ",
                        "shakes your hand appreciatively as you enter.",
                        "",
                        "\"Thank you so much for helping us. My experiment is",
                        "out of control! You have to destroy the carnivorous",
                        "plant in the greenhouse before it takes over the",
                        "whole facility!\"",
                        "",
                        "You nod. \"What do I need to do?\"",
                        "",
                        "\"I've prepared a poison that can kill it, if you spray",
                        "it on the plant's roots. It's in the lab. But that's not all!",
                        "If you walk in that greenhouse unprepared, the plant will eat",
                        "you alive! In addition to the formula, you'll need something to",
                        "distract the plant with. It may have a taste for flesh,",
                        "but it isn't picky about what kind. You also need",
                        "something to help you cut through the brambles blocking",
                        "the plant's roots.\"",
                        "",
                        "\"Lastly, the formula needs to be sprayed to be effective,",
                        "so you'll need a way to dispense it. Since the formula",
                        "isn't safe to handle, you'll also need protection for",
                        "your hands and eyes. That equipment will also help you",
                        "defeat the plant.\"",
                        "",
                        "\"Don't enter the greenhouse until you're prepared to",
                        "face the flesh-eating plant! Good luck, and thank you.\"",
                        "",
                        "After giving you these instructions, the elderly alchemist",
                        "exits the building, leaving you alone inside.",
                        "",
                        "  ------  "
                    ]
            }
        },
        "rooms": {
            "lobby": {
                "name": "lobby",
                "item": "None",
                "north": "None",
                "south": "None",
                "east": "None",
                "west": "hallway",
                "enemy": "None",
                "text": [
                    "The front lobby would normally feature a receptionist and",
                    "a hot pot of coffee, but right now it is empty. The big",
                    "metal doors leading into the hallway usually require a",
                    "security rune to pass, but they've been helpfully propped",
                    "open for you to pass through."
                ]
            },
            "hallway": {
                "name": "main hallway",
                "item": "ax",
                "north": "lab",
                "south": "cafeteria",
                "east": "lobby",
                "west": "greenhouse",
                "enemy": "None",
                "text": [
                    "The greenhouse sits at the far end of the hallway.",
                    "Menacing vines protrude out of the doors, dripping a sour",
                    "smelling goo onto the floor. The tiles on the floor have",
                    "started to pit and discolor where the slime sits on them.",
                    "",
                    "The hallway also has doors leading into the labs and into",
                    "the employee cafeteria. Naturally, it also connects back",
                    "to the lobby."
                ]
            },
            "lab": {
                "name": "lab",
                "item": "formula",
                "north": "None",
                "south": "hallway",
                "east": "None",
                "west": "storage",
                "enemy": "None",
                "text": [
                    "The alchemists who work here clearly left in a hurry.",
                    "Bottles and vials still sit across the counters and",
                    "workstations, though they did take care to disable all the",
                    "heat runes before they left. There is a storage closet",
                    "attached to the lab, and a few exits leading back out",
                    "to the main hallway."
                ]
            },
            "storage": {
                "name": "lab storage closet",
                "item": "goggles",
                "north": "None",
                "south": "None",
                "east": "lab",
                "west": "None",
                "enemy": "None",
                "text": [
                    "The storage closet is packed full of vials, bottles,",
                    "and other carefully-labelled containers neatly arranged",
                    "in rows. You don't know enough about alchemy to identify",
                    "what's in most of the vials, but you do recognize the",
                    "protective runes woven into every corner of the closet.",
                    "Even a powerful mage would struggle to cast a spell in here."
                ]
            },
            "cafeteria": {
                "name": "cafeteria",
                "item": "bottle",
                "north": "hallway",
                "south": "None",
                "east": "closet",
                "west": "kitchen",
                "enemy": "None",
                "text": [
                    "The employee cafeteria looks... like a cafeteria.",
                    "Salt, pepper, citrine, and ketchup sit beside the napkin",
                    "dispenser on every table. Plates of food, most of them",
                    "now cold, sit casually on the tables as though their owners",
                    "might be back from a bathroom visit at any moment."
                ]
            },
            "kitchen": {
                "name": "kitchen",
                "item": "meat",
                "north": "None",
                "south": "None",
                "east": "cafeteria",
                "west": "None",
                "enemy": "None",
                "text": [
                    "Much of the food in the kitchen seems to have been left out",
                    "on various cutting boards, though large containers of food",
                    "seem to have all been put away. Fortunately, the fire runes",
                    "have all been disabled."
                ]
            },
            "closet": {
                "name": "janitor's closet",
                "item": "gloves",
                "north": "None",
                "south": "None",
                "east": "None",
                "west": "cafeteria",
                "enemy": "None",
                "text": [
                    "The janitor's closet is filled with mostly the things you",
                    "would expect: bags of salt, cleaning potions, brooms, and",
                    "mops. It seems like the janitor also serves as the lab's",
                    "landscaper, because the closet also contains fertilizer,",
                    "a weed whacker, and a few herbicides. Nothing strong enough",
                    "for your purposes, though."
                ]
            },
            "greenhouse": {
                "name": "greenhouse",
                "item": "None",
                "north": "None",
                "south": "None",
                "east": "hallway",
                "west": "None",
                "enemy": "plant",
                "text": [
                    "The doors to the greenhouse have already been forced open by",
                    "the plant's vines. You take a deep breath and head inside."
                ]
            }
        },
        "items": {
            "formula": {
                "name": "special herbicide",
                "text": [
                    "Although there are many vials here, one of them",
                    "has been helpfully labelled 'Special Herbicide Formula.'"
                ]
            },
            "ax": {
                "name": "fire ax",
                "text": [
                    "On the wall next to the lobby door, there is an ax sitting",
                    "in a glass case. 'Break in case of Emergency' is written on",
                    "the glass in big red letters."
                ]
            },
            "goggles": {
                "name": "goggles",
                "text": [
                    "On one of the shelves, there is a collection of equipment,",
                    "also covered in protective runes. Most of it looks heavily",
                    "used, but one pair of goggles stands out to you. Its runes",
                    "are still bright and fresh, and you think they would do",
                    "a good job of protecting you in your quest."
                ]
            },
            "gloves": {
                "name": "gardener's gloves",
                "text": [
                    "The gardening gloves, on the other hand, could be useful.",
                    "They're nice and thick and should protect your hands against",
                    "anything short of a proper blade."
                ]
            },
            "bottle": {
                "name": "ketchup bottle",
                "text": [
                    "One of the ketchup bottles is pretty much empty.",
                    "You could probably use it to spray the herbicide.",
                    "The leftover ketchup probably won't hurt anything, right?"
                ]
            },
            "meat": {
                "name": "griffin breast",
                "text": [
                    "On one of the tables, a few raw griffin breasts have been",
                    "left out. A little bit of blood has dribbled down from the",
                    "table onto the tile floor."
                ]
            }
        },
        "enemys": {
            "plant": {
                "name": "Flesh-Eating Plant",
                "defeat_items": ["ax", "gloves", "meat", "formula", "bottle", "goggles"],
                "intro_text": [
                    "You immediately find yourself surrounded by vines so thick",
                    "that you can barely see. When you step on one, it moves.",
                    "One of the plant's mouths hisses as it senses your presence."
                ],
                "fight_text": {
                    "ax": {
                        "False": [
                            "You try to run, but the vines block your path.",
                            "A dozen hungry plant mouths surround you.",
                            "As they sink their teeth into you, your flesh begins to dissolve."
                        ],
                        "True": [
                            "You cut a path through the vines, narrowly avoiding the",
                            "hungry plant's snapping mouths."
                        ]
                    },
                    "gloves": {
                        "False": [
                            "As you cut, the stinging slime burns your hands.",
                            "You drop the ax and the plant catches up to you.",
                            "",
                            "A dozen hungry plant mouths surround you.",
                            "As they sink their teeth into you, your flesh begins to dissolve."
                        ],
                        "True": [
                            "As you cut, the acidic goo gets on your hands.",
                            "Fortunately, the gloves protect you from the slime."
                        ]
                    },
                    "meat": {
                        "False": [
                            "As you cut your way further into the room, more",
                            "of the plant heads start to follow you.",
                            "",
                            "It must be hungry.",
                            "",
                            "Can it smell you?",
                            "",
                            "",
                            "You turn a corner and find yourself surrounded by hissing",
                            "plant heads, hungry for your flesh. The last thing you feel",
                            "is their acid dissolving you."
                        ],
                        "True": [
                            "As you cut your way further into the room, more",
                            "of the plant heads start to follow you.",
                            "You throw the bloody, dripping griffin breast as far away",
                            "from yourself as you can.",
                            "",
                            "As soon as you throw it, multiple plant heads bite into it.",
                            "Looks like you bought yourself a little time.",
                            "",
                            "Breathing a little easier, you head towards the roots."
                        ]
                    },
                    "formula": {
                        "False": [
                            "When you get to the roots, you realize that you don't have",
                            "a way to kill the plant. Regular herbicides won't kill a",
                            "monster like this - you need Dr. Shultz's special formula.",
                            "",
                            "You hear a screech from the plant's heads.",
                            "Looks like they're done eating.",
                            "",
                            "You try to cut at the plant's roots with your ax, but",
                            "you aren't fast enough. You're quickly surrounded by hungry,",
                            "salivating plant mouths.",
                            "",
                            "The last thing you feel is your flesh being dissolved by their saliva."
                        ],
                        "True": [
                            "After some cutting, you make it to the roots of the plant.",
                            "You pull out the Doc's special formula and get to work.",
                            "",
                            "Behind you, you hear a screech from the plant's heads.",
                            "Looks like they're done eating."
                        ]
                    },
                    "bottle": {
                        "False": [
                            "You fumble a bit with the glass vial, but you get it open",
                            "and start pouring. Every root the herbicide touches dies,",
                            "but it's slow going putting a few drops on each root.",
                            "",
                            "As frantically start pouring the herbicide, you hear the",
                            "flesh-eating plant's heads snapping behind you.",
                            "",
                            "Time's up.",
                            "",
                            "You're quickly surrounded by hungry, salivating plant mouths.",
                            "The last thing you feel is your flesh being dissolved by their saliva."
                        ],
                        "True": [
                            "You use the ketchup bottle to spray the herbicide on as many",
                            "of the roots as you can. Every root the formula touches dies.",
                            "",
                            "The decay quickly spreads through the vines and stalks,",
                            "and you hear the plant's heads scream in agony.",
                            "They're right behind you, now, but they're in too much pain",
                            "to worry about eating you."
                        ]
                    },
                    "goggles": {
                        "False": [
                            "Unfortunately, as you're spraying, you feel a stinging pain",
                            "in your eyes. It didn't even take a drop to start eating",
                            "away at your corneas.",
                            "",
                            "While you're desperately clawing at your eyes, you hear",
                            "an angry hiss overhead. The plant seems to have recovered",
                            "its senses, and one of its surviving heads has found you.",
                            "",
                            "Blind, you find yourself at the mercy of the plant.",
                            "Its few remaining heads sink their teeth into you."
                        ],
                        "True": [
                            "As you spray, the salt runes in your goggles flare.",
                            "Even the mist from your spraying is enough to activate the",
                            "protection runes. You're glad you grabbed them.",
                            "",
                            "Before long, you manage to spray every one of the plant's",
                            "roots. The plant tries to bite you with its heads, but you",
                            "easily fight them off in their weakened state."
                        ]
                    }
                },
                "death_text": [
                    "After a few minutes, the plant's heads are still. It's over."
                ]
            }
        }
    }

    #Initializes game

    # Initialize all objects first, then assign relationships
    for class_type in level_data.keys():
        for entry in level_data[f'{class_type}'].keys():
            exec(f'{entry.lower()} = {class_type.title().rstrip('s')}()')


    for player in level_data['players'].keys():
        eval(player).items = []
        eval(player).intro = level_data['players'][player]['intro']
        for item in level_data['players'][player]['starting_items']:
            eval(player).items.append(eval(item))

        eval(player).room = eval(level_data['players'][player]['starting_room'])

    for room in level_data['rooms'].keys():
        eval(room).name = level_data['rooms'][room]['name']
        eval(room).item = eval(level_data['rooms'][room]['item'])
        eval(room).north = eval(level_data['rooms'][room]['north'])
        eval(room).south = eval(level_data['rooms'][room]['south'])
        eval(room).east = eval(level_data['rooms'][room]['east'])
        eval(room).west = eval(level_data['rooms'][room]['west'])
        eval(room).enemy = eval(level_data['rooms'][room]['enemy'])
        eval(room).text = tuple(level_data['rooms'][room]['text'])

    for item in level_data['items'].keys():
        eval(item).name = level_data['items'][item]['name']
        eval(item).text = tuple(level_data['items'][item]['text'])

    # I used "enemys" instead of "enemies" so that I can use the .rstrip method to depluralize it.
    enemies_list = []
    for enemy in level_data['enemys'].keys():
        enemies_list.append(eval(enemy))
        eval(enemy).name = level_data['enemys'][enemy]['name']
        eval(enemy).intro_text = level_data['enemys'][enemy]['intro_text']
        eval(enemy).death_text = level_data['enemys'][enemy]['death_text']

        eval(enemy).fight_text = {}
        eval(enemy).defeat_items = ()
        for item in level_data['enemys'][enemy]['defeat_items']:
            eval(enemy).defeat_items += tuple((eval(item),))
            eval(enemy).fight_text[eval(item)] = level_data['enemys'][enemy]['fight_text'][item]

    player = eval(f'{list(level_data['players'].keys())[0]}')

    for line in player.intro:
        print(line)
        time.sleep(1.25)
    print()
    time.sleep(5)

    while True:
        # for each room, display the room's description text.
        for line in player.room.text:
            print(line)
            time.sleep(1)
        print()
        time.sleep(2)

        # if enemies are present, describe them. Then, fight them and describe the results. If the player loses the fight, the game is over.
        if player.room.enemy is not None:
            if player.room.enemy.alive:
                for line in player.room.enemy.intro_text:
                    print(line)
                    time.sleep(1)
                print()
                time.sleep(2)
                if not player.room.enemy.fight(player):
                    player.alive = False
                    break
                else:
                    player.room.enemy.alive = False
                    for line in player.room.enemy.death_text:
                        print(line)
                        time.sleep(1)
                    print()
                    time.sleep(2)


        # Check if the player has won
        for enemy in enemies_list:
            if enemy.alive:
                break           #Stop checking if any enemy is alive

        else:                   #If the loop ends without breaking, the player wins.
            player.win = True
            break               #Stops the main gameplay loop.


        # If the room contains an item, prompt the player to pick it up
        if player.room.item is not None:
            for line in player.room.item.text:
                print(line)
                time.sleep(1)
            print()
            time.sleep(2)

            while True:
                item_choice = input(f'Would you like to pick up the {player.room.item}? [y/n] ')
                if item_choice.lower().strip() == 'y':
                    player.items.append(player.room.item) #This is hardcoded for rooms to only have one item.
                    time.sleep(0.25)
                    print(f'\nYou picked up the {player.room.item}!\n')
                    time.sleep(0.5)
                    player.room.item = None
                    break
                elif item_choice.lower().strip() == 'n':
                    time.sleep(0.25)
                    print(f'\nYou did not pick up the {player.room.item}.\n')
                    time.sleep(0.5)
                    break
                else:
                    print('Please choose a valid response.\n')
                    print()
                    time.sleep(0.5)


        # prompt the player to choose where to go next.
        for direction in ['north', 'south', 'east', 'west']:
            if eval(f'player.room.{direction}') is not None:
                print(f'The {eval(f'player.room.{direction}')} is to the {direction}.')
                time.sleep(0.75)
        else:
            print()
            time.sleep(0.5)

        player_move = input('Please enter a direction: North, South, West, East or Exit: ').lower().strip()
        if player_move == 'exit':
            time.sleep(0.5)
            break
        elif hasattr(player.room, player_move) and eval(f'player.room.{player_move}') is not None:
            time.sleep(0.25)
            player.room = eval(f'player.room.{player_move}')
            print(f'\nMoved to the {player.room}.\n')
            time.sleep(0.5)

        else:
            time.sleep(0.01)
            print('Please enter a valid direction!\n')
            time.sleep(0.5)

    # When gameplay loop terminates, summarize the game and display text for winning, losing, and quitting.
    if player.win:
        print('You win!\n')
        time.sleep(1)
    elif not player.alive:
        print('You died!\n')
        time.sleep(1)

    print('\n --- Thanks for playing! --- \n')

    #TODO: Before main menu: add a "play again?" option. Once main menu implemented: return to the main menu after the summary.