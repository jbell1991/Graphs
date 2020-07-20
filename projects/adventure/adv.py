from room import Room
from player import Player
from world import World


import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', 's', 's', 's', 's', 'n', 'n', 'w', 'w', 'e', 'e', 'e', 'e']
traversal_path = []

# mapping of opposite directions
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# track opposite of traversal_path
opposite_path = []

# set up graph
graph = {}

# use set to track which rooms have been visited
visited = set()

def build_graph():
    # repeat until the length of the visited rooms == length of the room map
    while len(visited) < len(room_graph):
        # start at the first room
        current_room = player.current_room.id
        # if current room is not in visited 
        if current_room not in visited:
            # mark room exits as unexplored
            room_exits = {direction : '?' for direction in player.current_room.get_exits()}
            graph[current_room] = room_exits
            # mark that room as visited
            visited.add(player.current_room.id)
        # mark the opposite of the previously moved direction as the last room id
        if any(opposite_path):
            graph[current_room][opposite_path[-1]] = prev_room
        # find unexplored directions in the current room
        unexplored_directions = []
        for key, value in graph[current_room].items():
            if value == '?':
                unexplored_directions.append(key)
        # if there are any unexplored directions in the current room
        if len(unexplored_directions) > 0:
            # pick a random direction to move in 
            random_direction = random.choice(unexplored_directions)
            # or pick the last item from the list
            # random_direction = unexplored_directions[-1] 
            # keep track of previous room's id
            prev_room = player.current_room.id
            # move the player in the random direction
            player.travel(random_direction)
            # assign variable next_room to new room id after move
            next_room = player.current_room.id
            # set the key equal to the room in that direction
            graph[prev_room][random_direction] = next_room
            # track the direction 
            traversal_path.append(random_direction)
            # track the opposite direction
            opposite_path.append(opposite[random_direction])
        # if there are no unexplored directions
        else:
            # until you reach a room where there are any unexplored paths
            if len(unexplored_directions) == 0:
                # move in the opposite direction
                opposite_direction = opposite_path[-1]
                # set previous room
                prev_room = player.current_room.id
                # move player
                player.travel(opposite_direction)
                # set next room
                next_room = player.current_room.id
                # set the key equal to the room in that direction
                graph[prev_room][random_direction] = next_room
                # remove from path
                opposite_path.pop()
                # track the direction
                traversal_path.append(opposite_direction)
    print(graph)
    return graph


print(build_graph())


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
