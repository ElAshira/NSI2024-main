
# Jeu Antivirus

Il s'agit d'un jeu simple développé en utilisant la bibliothèque Pygame. L'objectif est de naviguer à travers des niveaux, d'éviter les collisions et d'atteindre la zone désignée.

## Installation

1. **Python** : Assurez-vous d'avoir Python installé. Vous pouvez le télécharger depuis [python.org](https://www.python.org/).
2. **Pygame** : Installez Pygame en utilisant pip :
   ```bash
   pip install pygame
   ```
3. **Cloner le dépôt** : Clonez ce dépôt sur votre machine locale.

## Comment Jouer

1. Exécutez `main.py` pour démarrer le jeu.
2. Dans le menu principal, cliquez sur le bouton "Jouer" pour commencer le jeu ou sur le bouton "Option" pour sélectionner un niveau.

## Contrôles du Jeu

- **Touches directionnelles** : Déplacer la molécule sélectionnée (rose ou virus).
- **Touche F3** : Afficher ou masquer les hitbox.
- **Touche Right Ctrl** : Changer le contrôle entre la molécule rose et le virus.

## Structure des Fichiers

- `main.py` : Contient la logique principale du jeu et sa configuration.
- `molecule.py` : Inclut les classes `Molecule` et `Colisionneur` pour les éléments du jeu.
- `Assets/` : Contient les images utilisées dans le jeu.

## Composants du Jeu

### Classe `Molecule`

La classe `Molecule` représente les entités mobiles du jeu. Elle est utilisée pour définir les molécules, telles que la molécule rose et le virus. Cette classe possède les attributs suivants :

- **`image`**: L'image représentant la molécule.
- **`x`, `y`**: Les coordonnées de la molécule sur l'écran.
- **`hitbox_list`**: Une liste de rectangles représentant les zones de collision de la molécule.

La classe `Molecule` offre les fonctionnalités suivantes :

- **`move(dx, dy)`**: Déplace la molécule selon les valeurs `dx` (déplacement horizontal) et `dy` (déplacement vertical).
- **`get_image()`**: Renvoie l'image associée à la molécule.
- **`get_position()`**: Renvoie les coordonnées actuelles de la molécule.
- **`set_position(x, y)`**: Définit de nouvelles coordonnées pour la molécule.

### Classe `Colisionneur`

La classe `Colisionneur` gère les éléments de collision dans le jeu. Elle est utilisée pour définir les obstacles et les zones de collision. Voici ses attributs principaux :

- **`x`, `y`**: Les coordonnées du collisionneur sur l'écran.
- **`image`**: L'image représentant le collisionneur.
- **`width`, `height`**: La largeur et la hauteur du collisionneur.
- **`hitbox_liste`**: Une liste de rectangles représentant les zones de collision du collisionneur.

La classe `Colisionneur` offre les fonctionnalités suivantes :

- **`set_position(x, y)`**: Définit de nouvelles coordonnées pour le collisionneur.
- **`can_move`**: Un indicateur indiquant si le collisionneur peut se déplacer (booléen).



## Crédits

- Développé par Pierre-Antoine SOUBRIER

