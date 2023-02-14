# Architecture
L'ensemble des fonctions utiles est disponible dans le fichier Maze.py.
Les tests associés aux fonctions de Maze.py se trouve dans test.py
main_aléatoire.py est un executable
main_Q.py est un executable


# MazeQL
On utilise l'algorithme d'apprentissage par renforcement Q-Learning pour générer un petit labyrinthe contenant, un trésor, un début, une fin.


On représente le labyrinthe de la façon suivante :

En premier lieu, les coordonnées des cases du labyrinthe sont mises en dimension 1 par besoin de simplification (la case (2, 1) devient la case numéro 4)
Le labyrinthe est représenté par une liste de 27 chiffres.
Les 3 premiers correspondent aux coordonnées de la case de départ, la case de fin et la case trésor. Cette séquence est suivie de 12 chiffres binaires : 1 indique la présence d'un mur vertical, 0 indique l'absence de mur vertical.
Cette séquence est suivie d'une autre de 12 chiffres aussi, indiquant la présence ou l'absence d'un mur horizontale. (le numéro d'un mur est établi par sa position dans le labyrinthe de gauche à droite et de haut en bas.)
Avec cette modélisation, on peut calculer exactement le nombre de labyrinthes possible : 16 * 15 * 14 * 2²⁴ = 56.3 milliards de combinaisons. Cependant, il est bon de noter que la plupart serait vraisemblablement non resolvable.




# Pathfinding


Pour vérifier qu'un labyrinthe est bien résolvable on procède de la façon suivante : depuis la case de départ, on découvre par récursion toutes les cases atteignables depuis cette dernière. Si la case d'arrivé et le trésor sont dans ces cases, alors il y a un chemin allant du premier au deuxième et du deuxième au troisième, le labyrinthe est donc valide. Dans le cas contraire, il n'est pas valide.




# Modélisation




L'algorithme de Q-learning est un algorithme d'exploration de graphe permettant d'associer pour chaque nœud du graphe une espérance de gain.
Pour appliquer cet algorithme à notre problème, nous modélisons la génération de labyrinthes par le problème de graphe suivant :

On choisit d'abord aléatoirement les cases des keypoints (on ne s'intéresse pas à savoir quel keypoint est sur quelle case précisément, car cela n'a pas d'impact sur la resolvabilité de notre labyrinthe.).
À partir de l'information des keypoints, on choisit la présence ou non d'un mur.

À la fin de la génération, on vérifie si le labyrinthe est résolvable ou non. Si c'est le cas, on applique une récompense positive au dernier état, si ce n'est pas le cas, on applique une récompense négative au dernier état. Ces récompenses sont les seules rétropropagés par l'algorithme.

Un paramètre d'exploration est ajouté dans le modèle. Ce paramètre permet de choisir une action aléatoire dans certains cas, permettant ainsi la diversification des labyrinthes produits.




# Expérimentation

On compare la résolvabilité d'un labyrinthe produit aléatoirement et avec notre Q algorithme.


**Pour lancer l'expérimentation aléatoire, lancez le fichier main_aléatoire.py avec python3**


Sur 10 000 labyrinthes produits, on observe autour de 27% de labyrinthe resolvable.
On lance ensuite notre algorithme de Q value avec les paramètres suivant : gamma = 0.99, lr=0.2, explo = 0.01


**Pour lancer l'expérimentation avec l'algorithme de Q value, lancez le fichier main_Q.py avec python3**


Au bout de 1 000 000 itérations, on observe un taux de construction de labyrinthes résolvables à plus de 98%, prouvant l'efficacité de notre algorithme.

PS : On peut noter le faible taux d'exploration donné en paramètre pour cet entraînement et on pourrait douter de la diversité des labyrinthes produits.

À cette accusation, on peut noter la diversité des "seed", les cases keypoints générés aléatoirement et garantissant ainsi une certaine diversité dans notre production. Augmenter le paramètre d'exploration a comme conséquence de moins bonne performance sur le taux de labyrinthe résolvable produits. Il sera bon d'introduire une mesure de similarité entre labyrinthes, permettant ainsi la maximisation du taux de labyrinthe résolvable et la diversité de ces derniers.




# BONUS
On veut implémenter une mesure de difficulté d'un labyrinthe.
Une possibilité est de considérer le nombre de cases à parcourir entre le début du labyrinthe, le trésor et la sortie du labyrinthe. Cependant, si le labyrinthe est linéaire, il peut être grand et pour autant très simple à effectuer.
Une autre mesure possible est donc de calculer le nombre d'embranchements possible dans le labyrinthe. Le nombre de choix à prendre.
Cependant, le nombre d'embranchements peut être globalement élevé dans le labyrinthe et les keypoints proches les uns devant les autres rendant la résolution du labyrinthe facile.
On peut donc faire une somme pondérée de ces deux valeurs. On peut également compter le nombre d'embranchements entre l'entrée-trésor et trésor-sortie ainsi que le nombre d'embranchements filles des premières.