# Tera Donica

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

#The player starts in the Great Hall
player_room = 'Great Hall'

if __name__ == "__main__":
    while player_room != 'exit':
        """Main Gameplay Loop"""

        #Display the player's status
        print(f'You are in the {player_room}.')
        player_move = input('Please enter a direction: North, South, West, East or Exit: ').title().strip()

        #determine destination
        if player_move == 'Exit':
            player_room = 'exit'
            print('Thanks for Playing!')
        elif rooms.get(player_room).get(player_move, False): #validates inputs via False default value
            player_room = rooms[player_room][player_move]
            print(f'You moved to {player_room}.\n')
        else:
            print('\nPlease enter a valid direction.\n')
