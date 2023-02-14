import numpy as np

class Maze:
    def __init__(self, size = 4):
        self.size  = size

    def pathfinder(self, maze):
        '''
        Maze est un string représentant le labyrinthe par des septuplet espacé par un espace
        '''
        #Transformation de la chaine de caractère en matrice d'entier, ligne pour état et colonne pour variable
        maze = np.array([[int(j) for j in list(i)] for i in maze.split("")])

        #On vérifie que le labyrinthe est correcte
        tmp = np.sum(maze[:,5:], axis = 1)
        if np.any(tmp > 1) : raise Exception("Même contenu présent plusieurs fois")
        if np.any(tmp = 0) : raise Exception("Un Contenu absent")
        if np.any(np.sum(maze[:,5:], axisz = 1)>1): raise Exception("Case avec plusieurs contenus")

        #On commence par l'entrée du labyrinthe
        begin = 

    def creat(self):
        self.