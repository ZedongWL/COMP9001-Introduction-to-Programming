"""
This is the entry point to your game.

Launch the game by running `python3 launch_game.py`
"""
from time import time
from game_engine import Engine
from gui import GUI
from player import Player
t1 = time()
game = Engine('complexc.txt', Player, GUI)

game.run_game()
t2 = time()
print(t2-t1)