import random


def lancer(n):
    tab = [random.randint(1,6) for i in range(0,n)]
    return tab


def pair_6(liste):
    print(liste)
    nb_6 = [x for x in liste if x == 6]
    if len(nb_6) >= 2:
        return True
    else:
        return False
    
print(pair_6(lancer(5)))


def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)
def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])
def negatif(image):
    '''renvoie le négatif de l'image sous la forme
    d'une liste de listes'''
    # on crée une image de 0 aux mêmes dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]  # Calcul du négatif
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inférieure au seuil
    et 1 sinon'''
    # on crée une image de 0 aux mêmes dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
