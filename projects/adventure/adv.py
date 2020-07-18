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
# traversal_path = []

# opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# opposite_path = []

# graph = {}

# def build_graph():
#     visited = set()
#     # build a graph by running a traversal through the map
#     # until you reach every room in the map
#     while len(visited) < len(room_graph):
#         # start at room 0
#         current_room = player.current_room.id
#         if current_room not in visited:
#             room_exits = {direction : '?' for direction in player.current_room.get_exits()}
#             graph[current_room] = room_exits
#             visited.add(player.current_room.id)
#         unexplored_directions = []
#         for key, value in room_exits.items():
#             if value == '?':
#                 unexplored_directions.append(key)
#         print('Unexplored Directions', unexplored_directions)
#         print(graph[current_room])
#         if len(unexplored_directions) != 0 :
#             random_direction = unexplored_directions[-1]
#             unexplored_directions.pop()
#             traversal_path.append(random_direction)
#             opposite_path.append(opposite[random_direction])


#             player.travel(direction=random_direction)
#             # set next room equal to the new current room id
#             next_room = player.current_room.id
#             # change direction key from '?' to pointer
#             # if '?' not in directions there an no unexplored paths so turn back the way you came
#             graph[current_room][random_direction] = next_room
#             # else change the '?' to
#             # append direction to path
#         else:
#             # random_direction = random.choice(list(graph[player.current_room.id]))
#             # traversal_path.append(random_direction)
#             # random_direction = opposite[last_direction]
#             # when i reach a dead end go back to the nearest room that does contain and unexplored path
#             # random_direction = opposite_path[-1]
#             # opposite_path.remove(random_direction)
#             # traversal_path.append(random_direction)
#             # random_direction = random.choice(list(graph[player.current_room.id]))
#             opposite_direction = opposite_path[-1]
#             opposite_path.pop()
#             # reverse directions
#             player.travel(direction=opposite_direction)
#             print('Current room', player.current_room.id)
#             traversal_path.append(opposite_direction)
#             break

#         # print(len(unexplored_directions))
#         # print(random_direction)
#         # player.travel(direction=random_direction)
#         # # set next room equal to the new current room id 
#         # next_room = player.current_room.id
#         # # change direction key from '?' to pointer
#         # # if '?' not in directions there an no unexplored paths so turn back the way you came
#         # graph[current_room][random_direction] = next_room
#         # # else change the '?' to
#         # # append direction to path
#         print(player.current_room.id)
#         print('Traversal path', traversal_path)
#         print('Opposite path', opposite_path)
#         print(graph)
#     return graph


# print(build_graph())


traversal_path = []

opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

opposite_path = []

graph = {}

def build_graph():
    visited = set()
    # repeat until the length of the visited rooms == length of the room map
    while len(graph) < len(room_graph):
        # start at the first room
        current_room = player.current_room.id
        # if current room is not in visited 
        if current_room not in visited:
            room_exits = {direction : '?' for direction in player.current_room.get_exits()}
            graph[current_room] = room_exits
            # mark that room as visited
            visited.add(player.current_room.id)
            # find unexplored directions in the current room
        unexplored_directions = []
        for key, value in graph[current_room].items():
            if value == '?':
                unexplored_directions.append(key)
        print(unexplored_directions)
        # if there are any unexplored directions in the current room
        if len(unexplored_directions) > 0:
            # pick a random direction to move in 
            random_direction = random.choice(unexplored_directions)
            # move the player in that direction
            player.travel(random_direction)
            # assign variable next_room to new room id after move
            next_room = player.current_room.id
            # set the key equal to the room in that direction
            graph[current_room][random_direction] = next_room
            # track the direction 
            traversal_path.append(random_direction)
            # track the opposite direction
            opposite_path.append(opposite[random_direction])
        # if there are no unexplored paths
        else:
            # until you reach a room where there are any unexplored paths
            if len(unexplored_directions) == 0:
                # move in the opposite direction
                opposite_direction = opposite_path[-1]
                player.travel(opposite_direction)
                opposite_path.pop()
                # track the direction
                traversal_path.append(opposite_direction)
        print(graph)
        print(traversal_path)
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
