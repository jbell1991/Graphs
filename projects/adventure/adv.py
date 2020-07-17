from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', 's', 's', 's', 's', 'n', 'n', 'w', 'w', 'e', 'e', 'e', 'e']
traversal_path = []

def build_traversal_graph():
    graph = {}
    # build a graph by running a traversal through the map
    # until you reach every room in the map
    
    while len(graph) < len(room_graph):
        # start at room 0
        current_room = player.current_room.id
        room_exits = {direction : '?' for direction in player.current_room.get_exits()}
        graph[current_room] = room_exits
        # logic that looks at each direction in a room
        # if there are no question marks (no unexplored paths) backtrack?
        # if '?' not in graph:
        #     # go back to where you came
        #     direction = 
        # # if there are question marks, pick a random one to explore
        # else:
            
        # do this until there are no more question marks in the graph

        # logic that chooses a direction if its a question mark
        random_direction = random.choice(list(graph[player.current_room.id]))
        # logic that changes a question mark to pointer that points to room in that direction
        # move player
        player.travel(direction=random_direction)
        # set next room equal to the new current room id 
        next_room = player.current_room.id
        # change direction key from '?' to pointer
        graph[current_room][random_direction] = next_room
        # append direction to path
        traversal_path.append(random_direction)
    # pick a randomly unexplored direction as denoted by a '?'
    # move in that direction
    # and add your move into the traversal_path
    # keep doing that until there are no unexplored directions?
    print(traversal_path)
    print(len(graph))
    return graph

print(build_traversal_graph())

# print(f'current player room id: {player.current_room.id}')
# print(f'current room exits: {player.current_room.get_exits()}')
# player.travel(direction='n')
# print(f'current player room id: {player.current_room.id}')
# print(f'current room exits: {player.current_room.get_exits()}')
# player.travel(direction='n')
# print(f'current player room id: {player.current_room.id}')
# print(f'current room exits: {player.current_room.get_exits()}')
# print(len(traversal_path), len(room_graph))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
