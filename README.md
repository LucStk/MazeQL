# MazeQL

On utilise l'algorithme d'apprentissage par renforcement Q-Learning pour générer un petit labyrinthe contenant, un trésor, un début, une fin.
L'algorithme de Q-learning est un algorithme d'exploration de graphe permettant d'associer pour chaque nœud du graphe une espérance de gain.

Pour appliquer cet algorithme à notre problème, nous modélisons la génération de labyrinthes par le problème de graphe suivant :

    On choisit trois cases différentes pour le trésor, le début et la fin du labyrinthe.
    Les murs horizontales sont représentés par une séquence de 3*3 = 9 bit. Les murs vertical sont représentés de la même façon.
    


# Pathfinder
L'algorithme pour vérifier la validité d'un labyrinthe est simple, on