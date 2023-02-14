from Maze import *

"""
On considère le labyrinthe jouet suivant
#########
#B'0|0'T#
#- ~ ~ -#
#0|0|0'0#
#- ~ - ~#
#E'0'0'0#
#- ~ - ~#
#0|0|0'0#
#########
B : begin
E : end
T : tresor
0 : empty
| : murs vertical
' : absence de murs vertical
- : murs horizontale
~ : absence de murs horizontale

La séquence de murs vertical est : 010 110 000 110
La séquence de murs horizontale est : 1001 1010 1010.
L'entrée est en 1, la sortie en 8, le trésor en 3.
Ce labyrinthe est résolvable par la séquence 0 1 5 9 10 6 2 6 9 8
"""

lV = [0,1,0,1,1,0,0,0,0,1,1,0]
lH = [1,0,0,1,1,0,1,0,1,0,1,0]

#Test pour voir si l'accesibilité est bonne
assert set(Maze.accessibles(0, lV, lH)) == {1}   , f"got: {Maze.accessibles(0, lV, lH)}"
assert set(Maze.accessibles(3, lV, lH)) == {2} , f"got: {Maze.accessibles(3, lV, lH)}"
assert set(Maze.accessibles(15, lV, lH)) == {14,11}   , f"got: {Maze.accessibles(15, lV, lH)}"
assert set(Maze.accessibles(9, lV, lH)) == {5,8,10,13}, f"got: {Maze.accessibles(9, lV, lH)}"
assert len(Maze.accessibles(4, lV, lH)) == 0, f"got: {Maze.accessibles(4, lV, lH)}"
assert set(Maze.accessibles(6, lV, lH)) == {2,7}, f"got: {Maze.accessibles(6, lV, lH)}"
print("\nAccessible is good \n")

assert Maze.resolvable(1, 8, 3, lV, lH, verbose=True)==True
assert Maze.resolvable(8, 1, 3, lV, lH, verbose=True)==True
assert Maze.resolvable(8, 3, 1, lV, lH, verbose=True)==True
"""
#########
#B'0|0|T#
#- ~ ~ -#
#0|0|0'0#
#- ~ - ~#
#E'0'0'0#
#- ~ - ~#
#0|0|0'0#
#########
"""

lV = [0,1,1,1,1,0,0,0,0,1,1,0]
lH = [1,0,0,1,1,0,1,0,1,0,1,0]

assert Maze.resolvable(1, 8, 3, lV, lH, verbose=True)==False

lV = [0,1,0,1,1,0,1,0,0,1,1,0]
lH = [1,0,0,1,1,0,1,0,1,0,1,0]

assert Maze.resolvable(1, 8, 3, lV, lH, verbose=True)==False
assert Maze.resolvable(4, 8, 3, lV, lH, verbose=True)==False

print("\nResolvable is good\n")