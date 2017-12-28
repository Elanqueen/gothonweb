#coding=utf-8
from map import Room
#class ForestRoom(Room):
forest_plane = Room("Forest Plane","""Behind the little heal, there is a broomy forest.
                    There are lots of beautiful flowers and big trees. 
                    They wave there hands in the wind. In a hug tree, 
                    you find a tree room hiding in leaves.
                    There is a ladder you can climbing to the tree room.""")
forest_plane.actions=["climb on the ladder","leave away","fire the ladder"]

squirrel_room = Room("Squirrel Room","""When you are climbing, a creaking voice goes to you ears.
                        "Wow, it is amazing!" You find a squirrel living in the hole in the tree.
                        You try your best to find the squirrel in the hole, but it is too dark in it.
                        You have to find a way.
                        
                        That is great, you bring the pine nuts out of your bag which you peek on the way coming.
                        And you sing a song to catch the attention of the squirrel. 
                        
                        The squirrel comes out, take the pine nuts,and make frinds with you. 
                        He tells you there is a mysterious thing in the tree room. 
                        You continue to climb with the squirrel.
                           """)
squirrel_room.actions=["ignore the squirrel","give pine nuts to the squirrel","bite the squirrel"]

tree_room=Room("Tree Room","""Open the door. A wondrous world comes in your eyes. 
                You gradually walk into the room with a hot-bloooded heart. 
                There is a little bed  decorated with flowers and leaves, layed on the window.
                A desk and four bamboo stools stand in the middle of the room. Four little cups 
                lay on the desk. You walk in the room around and around. Oh, you find a wood box on the 
                desk behind the window. It needs a key to open it.""")
tree_room.actions=["find the key","ignore the box","open the box with hammer"]

death = Room("death", """You died!!!""")
win = Room("win", """A fairy fly out!""")

generic_death = None

#==================================添加room间的逻辑关系====================================
START = forest_plane
START.add_paths({"climb on the ladder":squirrel_room})
squirrel_room.add_paths({"give pine nuts to the squirrel":tree_room})
tree_room.add_paths({"find the key":win})

path_list = ("death", "win", "climb on the ladder","give pine nuts to the squirrel","find the key")
room_list = {"Forest Plane":forest_plane,"Squirrel Room":squirrel_room,"Tree Room":tree_room}
