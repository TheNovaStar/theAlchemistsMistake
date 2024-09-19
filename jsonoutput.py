class Player:
    def __init__(self, items=None):
        self.alive = True
        self.items = items
        self.room = None

class Room:
    def __init__(self, room_name, items=None, enemy=None, room_text=None):
        self.name = room_name
        self.items = items
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
        if self.items is not None:
            out_str += ', Items:'
            for item in self.items:
                out_str += f', {item},'
            out_str = out_str.strip(',')

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

        return out_str

class Item:
    def __init__(self, name, item_text=None):
        self.name = name
        self.text = item_text

    def __str__(self):
        return self.name

    def status(self):
        return f'Item: {self.name}'

class Enemy:
    def __init__(self, name, items = None):
        self.name = name
        self.items = items
        self.alive = True

    def __str__(self):
        return self.name

    def status(self):
        out_str = f'Enemy: {self.name}'

        if self.alive:
            out_str += ' (alive)'
        else: out_str += ' (dead)'

        return out_str

    def fight(self):
        """Returns True if player wins, False otherwise."""
        if self.items is not None:
            for item in self.items:
                if item in player.items: continue
                else: return False
            else: return True
        else: return True

#FIXME: this part should be read from the json file, not hardcoded

#First, declare and name all objects

player = Player()
goblin = Enemy('Goblin')
sword = Item('Sword')
shield = Item('Shield')
potion = Item('Potion')
center = Room('Center')
top = Room('Top')
left = Room('Left')
right = Room('Right')
bottom = Room('Bottom')

# initialize rooms and mapping

center.north = top
center.west = left
center.east = right
center.south = bottom

top.south = center
top.enemy = goblin

left.east = center
left.items = [sword]

right.west = center
right.items = [shield]

bottom.north = center
bottom.items = [potion]

#initialize enemies
goblin.items = [sword]

if __name__ == '__main__':
#FIXME: this section should run the actual game

    player.items = [sword, potion]

    print(center.status())
    print(top.status())
    print(left.status())
    print(right.status())
    print(bottom.status())
    print(goblin.fight())