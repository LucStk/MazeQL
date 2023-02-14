from Maze import *

m = Maze()
m.Qlearning(nb_itération = 1000000, gamma = 0.99, lr=0.2, explo = 0.01, verbose= True,check_periode=10000)
print("\nNouveau labyrinthe :")
print(m.Q_generation())