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
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#return back to the previous path i. e. reverse path
reverse_path = []
# mark room as visited
visited = {}
# state movement order
m = {"n": "s", "e": "w", "s": "n", "w": "e"}
#set the current_room that is occupied as visited and get exits(i.e neighbors)
visited[player.current_room.id] = player.current_room.get_exits()
#while visited rooms are less than rooms in room_graph. This loop continues until all the rooms are visited
while len(visited) < len(room_graph):
    #check to see if the room
    #  which the player is, is not as marked  as visited
    if player.current_room.id not in visited:
        # mark the room as visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # get the most previous path
        p = reverse_path[-1]
        #remove the path from the direction of the current visited room's direction
        visited[player.current_room.id].remove(p)
    # check to see if there is no other place which a player can move to 
    if len(visited[player.current_room.id]) == 0:
        # get the most recent path
        p = reverse_path[-1]
        # remove the path from reverse path
        reverse_path.pop()
        # add the path to p to the traversal path
        traversal_path.append(p)
        # go to the previous path
        player.travel(p)
   # otherwise
    else:
        # get the last path visited
        l = visited[player.current_room.id][-1] 
        # remove the last path visited
        visited[player.current_room.id].pop()
        # add path l to the traversal path
        traversal_path.append(l) 
        # add the path that someone can move to give l in the reverse path
        reverse_path.append(m[l]) 
        # travel to l
        player.travel(l) 




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
