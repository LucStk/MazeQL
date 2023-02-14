import random

class Maze:
    def resolvable(begin, end, tresor, mursV, mursH, verbose=False):
        '''
            "begin"  : case entrée du labyrinthe
            "end"    : case fin du labyrinthe
            "tresor" : case tresor à prendre
            "murh"   : liste murs horizontales
            "murv"   : liste murs verticaux
        '''
        visited = set(); l = [begin]
        while True:
            if len(l) == 0: break
            i = l.pop()
            visited.add(i)
            tmp = Maze.accessibles(i, mursV,mursH)
            l += list(filter(lambda i : i not in visited, tmp))

        if verbose:
            print("Visited :", visited)

        if tresor in visited and end in visited:
            return True
        
        #Il n'existe pas de chemin menant de l'entrée à la sortie et au trésor
        return False

    def accessibles(c, mursV, mursH):
        """
        Depuis une case c, avec une suite de murs horizontale et verticaux, retourne les cases atteignables.
        """
        
        l = []
        #Si non sur le bord droit et pas de murs à droite, on peut avancer à droite
        if (c+1)%(4) !=0 and not mursV[c-c//4] : l += [c+1] 

        #Si non sur le bord gauche et pas de murs à gauche, on peut avancer à gauche
        if c%(4) !=0   and not mursV[c-c//4-1] : l += [c-1] 
        
        # Si non sur bord bas et pas de murs en bas, on peut descendre
        if c+4 < 4**2 and not mursH[c] : l += [c+4] 

        # Si non sur bord haut et pas de murs en haut, peut monter
        if c-4 > 0 and not mursH[c-4]  : l += [c-4]

        return l
    
    def Q_learning(nb_itération = 1000000, gamma = 0.99, lr=0.1, explo = 0.2, verbose= False):
        '''
        Génère l'emplacement du trésor, début, fin aléatoirement.
        Créer les murs du l'abyrinthe avec l'algorithme Q value
        '''
        Qvalue = dict()
        nbr_laby_ok = 0

        for i in range(nb_itération):
            #Choisit une case de départ, d'arrivé, de trésor aléatoirement
            tmp = list(range(4))
            random.shuffle(tmp)
            #BET = [tmp.pop() for _ in range(3)]
            BET = [1, 8, 3]
            bet = str(set(BET))

            #On construit le labyrinthe
            for j in range(3*4*2):
                q0 = Qvalue.get(bet+'0')
                q1 = Qvalue.get(bet+'1')

                if q0 is None: 
                    q0 = random.random()
                    Qvalue[bet+'0'] = q0
                if q1 is None: 
                    q1 = random.random()
                    Qvalue[bet+'1'] = q1

                if random.random() < explo:
                    #On choisit une action au hasard
                    bet += random.choice(['0', '1'])
                else:#On choisit la meilleur des Q actions
                    bet += '01'[q1 == max(q0, q1)]

                #Rétropropagation de la Q valeur
                if j > 0:
                    Qvalue[bet[:-1]] = Qvalue[bet[:-1]] + lr*(gamma*Qvalue[bet] - Qvalue[bet[:-1]])
            
            #On a construit le labyrinthe, on cherche à savoir s'il est résolvable
            murs = list(map(lambda a : int(a),bet[-24:]))
            mursH = murs[-12:]
            mursV = murs[-24:-12]
            
            if (Maze.resolvable(BET[0], BET[1], BET[2],mursV, mursH)):
                Qvalue[bet] = 10
                nbr_laby_ok += 1
            else :
                Qvalue[bet] = -10

            if verbose and (i+1)% 1000 == 0:
                print("Itération {}, labyrinthe correct : {}%, taille Qtable {}".format(i, nbr_laby_ok/1000, len(Qvalue)))
                nbr_laby_ok = 0

        return Qvalue



