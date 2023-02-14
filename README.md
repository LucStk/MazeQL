# MazeQL

On utilise l'algorithme d'apprentissage par renforcement Q-Learning pour générer un petit labyrinthe contenant, un trésor, un début, une fin.
L'algorithme de Q-learning est un algorithme d'exploration de graphe permettant d'associer pour chaque nœud du graphe une espérance de gain.

Pour appliquer cet algorithme à notre problème, nous modélisons la génération de labyrinthes par le problème de graphe suivant :

Chaque case est décrite par une séquence de 7 bit les quatre premiers indique la présence d'un mur aux orientations : nord, est, sud et ouest.
Les trois bits restants représentent les "contenus" possibles : départ, arrivé, trésor.

On assigne un état pour chaque case de gauche à droite, ligne par ligne.
Chaque nœud est constitué de l'état de toutes les cases précédentes (pour choisir le septuplet de la troisième case, on utilise l'état de la première et de la seconde case).

Les nœuds à récompense négative possèdent une des propriétés suivantes :
- Aucune / plusieurs entrée ont été posées (ne nécessite pas un labyrinthe complet pour le deuxième cas).
- Aucune / plusieurs sorties ont été posées (ne nécessite pas un labyrinthe complet pour le deuxième cas).
- Le labyrinthe n'est pas résolvable.
- Le labyrinthe n'est pas entouré de murs.
- Une case est simultanément : un trésor et une entrée / une sortie et un trésor / une entrée et une sortie.

Les nœuds à récompense positive possèdent la propriété suivante :
- Le labyrinthe est correct structurellement et est résolvable

Une solution pour résoudre ce problème est de laisser entièrement l'algorithme de Q learning tester et se tromper sur chaque nœud du graphe.
Le nombre de nœud possible dans notre graphe est alors de 2⁷ * 4 * 4 = 2048. Ce nombre n'étant pas très grand, cette solution est clairement envisageable pour sa simplicité d'implémentation.

Une autre solution est de bloquer un certain nombre de récompenses négatives. Par exemple, on peut empêcher une case de posséder plusieurs "contenu". De cette manière, on passe de 2048 à (2⁴+3)*4*4 = 256 nœuds dans notre graphe, ce qui est largement plus rapide à explorer.

# Pathfinder
L'algorithme pour vérifier la validité d'un labyrinthe est simple, on