"""from player import Player
from space_object import SpaceObject
spaceship=SpaceObject(10,80,300,400,90,"spaceship",0)
asteroid_ls=[SpaceObject(5,90,300,400,80,"asteroid_small",0)]
c = SpaceObject(5,120,300,400,90,"asteroid_small",0)
c.move_count = 1
bullet_ls=[c]
fuel=100
score = 0
a = Player()

b = a.action(spaceship,asteroid_ls,bullet_ls,fuel,score)
print(b)

class a:
    def __init__(self,num):
        self.num = num
b = [a(6),a(5),a(5),a(4),a(8),a(2)]


ls=sorted(b,key=lambda x:x.num)
print(b)
print(ls)
from time import time
t1 = time()
def A(n):
    if n<0:
        return 0
    return n + A(n-1)
print(A(500))
t2 = time()
print(t2 - t1)
"""


from game_engine import Engine, isfloat, isint
from player import Player
from gui import GUI
a = Engine("examples/game_state_good.txt", Player, GUI)
