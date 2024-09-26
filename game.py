import json

class Player:
    def __init__(self, items=None):
        self.items = items
        self.alive = True
        self.room = None
        self.win = False

    def move(self, direction):
        """Causes the player to move between rooms. Assume 'direction' parameter is a player-inputted string.
         This method accepts the words north, south, east, and west in any case."""

        self.room = eval(f'self.room.{direction.lower().strip()}')
        print(f'Moved to {self.room}')


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
    def __init__(self, name='notNamed', defeat_items = None, text = None):
        self.name = name
        self.defeat_items = defeat_items
        self.text = text
        self.alive = True

    def __str__(self):
        return self.name

    def status(self):
        out_str = f'Enemy: {self.name}'

        if self.alive:
            out_str += ' (alive)'
        else: out_str += ' (dead)'

        print(out_str)

    def fight(self):
        """Returns True if player wins, False otherwise."""
        #TODO: implement fight flavor text for enemies
        if self.alive:
            if self.defeat_items is not None:
                for item in self.defeat_items:
                    if item in player.items: continue
                    else: return False
                else: return True
            else: return True
        else: return True

if __name__ == '__main__':

    #Read level data from file
    #TODO: add a menu that reads level data from user input

    with open('level.json', 'r') as level:
        level_data = json.load(level)

    #Initializes game

    # Initialize all objects first, then assign relationships
    for class_type in level_data.keys():
        for entry in level_data[f'{class_type}'].keys():
            exec(f'{entry.lower()} = {class_type.title().rstrip('s')}()')


    for player in level_data['players'].keys():
        eval(player).items = []
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
        eval(room).text = level_data['rooms'][room]['text']

    for item in level_data['items'].keys():
        eval(item).name = level_data['items'][item]['name']
        eval(item).text = level_data['items'][item]['text']

    # I used "enemys" instead of "enemies" so that I can use the .rstrip method to depluralize it.
    for enemy in level_data['enemys'].keys():
        eval(enemy).name = level_data['enemys'][enemy]['name']
        eval(enemy).text = level_data['enemys'][enemy]['text']

        eval(enemy).defeat_items = []
        for item in level_data['enemys'][enemy]['defeat_items']:
            eval(enemy).defeat_items.append(eval(item))

    player = eval(f'{list(level_data['players'].keys())[0]}')

    #FIXME: create gameplay loop

    # Display any one-time starting text for the game

    while True:
    # for each room, display the room's description text.
        print(player.room.text)
        if player.room.item is not None:
            print(player.room.item.text)

    # if enemies are present, describe them. Then, fight them and describe the results. If the player loses the fight, the game is over.
        if player.room.enemy is not None:
            if player.room.enemy.alive:
                print(player.room.enemy.text)
                if not player.room.enemy.fight():
                    player.alive = False
                    break
                else:
                    player.room.enemy.alive = False
            else:
                #TODO: implement death text for enemies
                ...


    # FIXME:if the player defeated all enemies, they win!

    # FIXME:if the game is not yet over, continue with the game:

    # FIXME:if the room has an item, describe it and ask the player if they want to pick it up.

    # prompt the player to choose where to go next.
        player_move = input('Please enter a direction: North, South, West, East or Exit: ').lower().strip()
        if player_move == 'exit':
            break
        elif eval(f'player.room.{player_move}') is not None:
            player.room = eval(f'player.room.{player_move}')
            print(f'Moved to {player.room}')

        else: print('Please enter a valid direction!')

    # When gameplay loop terminates, summarize the game and display text for winning, losing, and quitting.
    if player.win:
        print('You win!')
    elif not player.alive:
        print('You died!')

    print('Thanks for playing!')

    #TODO: Before main menu: add a "play again?" option. Once main menu implemented: return to the main menu after the summary.