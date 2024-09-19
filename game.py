class Player:
    def __init__(self, items=None):
        self.alive = True
        self.items = items

class Room:
    def __init__(self, room_name, items=None, north=None, south=None, east=None, west=None, enemy=None, room_text=None):
        self.name = room_name
        self.items = items
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enemy = enemy
        self.text = room_text

class Item:
    def __init__(self, name, item_text):
        self.name = name
        self.text = item_text

class Enemy:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items
        self.alive = True

#with open('level.json', 'r') as level:
    '''Load the map into Room and Enemy objects.'''
    #FIXME: Load the map
    ...