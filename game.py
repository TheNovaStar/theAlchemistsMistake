#Tera Donica

import json
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
    level_file = 'alchemistsMistake.json'
    with open(level_file, 'r') as level:
        level_data = json.load(level)

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

        player_move = input('Please enter a direction: North, South, West, East or Quit: ').lower().strip()
        if player_move == 'quit':
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