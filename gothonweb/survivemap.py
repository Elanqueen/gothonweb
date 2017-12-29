#coding=utf-8
from map import Room
#class SurviveRoom(Room):
    # ========================================各房间详情================================================
central_corridor = Room("Central Corridor",
                            """
                            The Gothons of Planet Percal #25 have invaded your ship and destroyed
                            your entire crew. You are the last surviving member and your last
                            mission is to get the neutron destruct bomb from the Weapons Armory,
                            put it in the bridge, and blow the ship up after getting into an 
                            escape pod.

                            You're running down the central corridor to the Weapons Armory when 
                            a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
                            flowing around his hate filled body. He's blocking the door to the 
                            Armory and about to pull a weapon to blast you.
                            """)
central_corridor.actions = ["tell a joke", "bite him", "run away"]

laser_weapon_armory = Room("Laser Weapon Armory",
                               """
                               Lucky for you they made you learn Gothon insults in the academy.
                               You tell the one Gothon joke you know:
                               Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
                               The Gothon stops, tries not to laugh, then busts out laughing and can't move.
                               While he's laughing you run up and shoot him square in the head
                               putting him down, the jump through the Weapon Armory door.

                               You do a dive roll into the Weapon Armory, crouch and scan the room
                               for more Gothons that might be hiding. It's dead quiet, too quiet.
                               You stand up and run to the far side of the room and find the 
                               neutron bomb in its container. There's a keypad lock on the box 
                               and you need the code to get the bomb out. If you get the code 
                               wrong 10 times then the lock closes forever and you can't 
                               get the bomb. The code is 3 digits.
                               """)
laser_weapon_armory.actions = [333, 666, 999]

the_bridge = Room("The Bridge",
                      """
                      The container clicks open and the seal breaks, letting gas out.
                      You grab the neutron bomb and run as fast as you can to the 
                      bridge where you must place it in the right spot.
                      """)
the_bridge.actions = ["run", "sing a song", "sleep"]

death = Room("death", """You died!!!""")
win = Room("win", """You survived!""")

# ======================================list======================================

path_list = ("death", "win", "Central Corridor", "Laser Weapon Armory",
                 "The Bridge", "player type number", "player tell joke", "player run")
room_list = {"Central Corridor": central_corridor, "Laser Weapon Armory": laser_weapon_armory,
                 "The Bridge": the_bridge, "death": death, "win": win}

# 错误反馈
generic_death = None

# =============================房间之间逻辑添加========================================
START = central_corridor
START.add_paths({"player tell joke": laser_weapon_armory})
laser_weapon_armory.add_paths({"player type number": the_bridge})
the_bridge.add_paths({"player run": win})
