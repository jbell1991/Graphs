from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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

opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def build_graph():
    graph = {}
    visited = set()
    # build a graph by running a traversal through the map
    # until you reach every room in the map
    while len(visited) < len(room_graph):
        # start at room 0
        current_room = player.current_room.id
        if current_room not in visited:
            room_exits = {direction : '?' for direction in player.current_room.get_exits()}
            graph[current_room] = room_exits
            # logic that changes a question mark to pointer that points to room in that direction
            visited.add(player.current_room.id)
        random_direction = random.choice(list(graph[player.current_room.id]))
        # move player
        player.travel(direction=random_direction)
        # set next room equal to the new current room id 
        next_room = player.current_room.id
        # change direction key from '?' to pointer
        graph[current_room][random_direction] = next_room
        # append direction to path
        # traversal_path.append(random_direction)
    return graph


print(build_graph())

def search_graph():
    # find the shortest path in the graph using breadth first traversal
    # append the path to the traversal_path
    # check if the steps are low enough to pass the tests
    pass



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
