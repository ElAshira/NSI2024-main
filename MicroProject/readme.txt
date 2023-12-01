
Le jeu "Antivirus" est une copie du jeu de Smart Games au succès interplanétaire : Anti-Virus.

Fonctionnalités Principales :

    - Menu Principal : Affiche le titre du jeu et propose des boutons pour jouer et accéder aux options.
    - Sélection des Niveaux : Permet au joueur de sélectionner le niveau de jeu souhaité.
    - Déplacement des Molécules : Le joueur peut contrôler les molécules pour les déplacer dans le plateau de jeu.
    - Gestion des Collisions : Le jeu détecte les collisions entre les molécules et les obstacles.
    - Objectif du Niveau : Chaque niveau a un objectif spécifique que le joueur doit atteindre pour progresser.

    Éléments de Code Principaux
        Fichiers Python

            molecule.py : Contient les classes pour représenter les molécules et les collisionneurs.
            main.py : Fichier principal du jeu, contient le code principal pour les fonctionnalités du jeu.

Fonctions Principales

    - main_menu() : Affiche le menu principal et gère les intéractions utilisateur pour accéder aux options ou commencer le jeu.
    - selection_level() : Permet au joueur de sélectionner le niveau et lance le niveau choisi.
    - game() : Gère le gameplay du niveau 1, y compris le déplacement des molécules et la détection des collisions.
    - level_2() : Fonction spécifique pour le deuxième niveau du jeu, similaire à la fonction game() mais pour un niveau différent.
Contrôles du Jeu "Antivirus"

    Utilisez les touches directionnelles (haut, bas, gauche, droite) pour déplacer les molécules sur le plateau de jeu.

    Appuyez sur la touche F3 pour activer ou désactiver l'affichage des hitboxes des éléments du jeu (collisionneurs, molécules, frontières, etc.).

    Changez de molécule contrôlée en appuyant sur la touche Ctrl.
