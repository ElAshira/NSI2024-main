import pygame
from molecule import Molecule as mclass
from molecule import Colisionneur as cclass
pygame.init()

fenetre = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Antivirus")

background_image = pygame.image.load("Assets\\background.png")
title = pygame.image.load("Assets\\title.png")
boutton_jouer = pygame.image.load("Assets\\BOUTTON_JOUER.png")
boutton_option = pygame.image.load("Assets\\boutton_option.png")
exit = False


def game(fenetre):
    exit = False
    fenetre_jeu = pygame.display.set_mode((800,800))
    pygame.display.set_caption("En jeu !")

    game_background = pygame.image.load("Assets\\game_background.png")
    fenetre_jeu.blit(game_background, dest=(0, 0))

    grille_image = pygame.image.load("Assets\\PlateauDeJeu.png")
    fenetre_jeu.blit(grille_image, dest=(-85, 150))
    file_level = open("file_level.txt")
    level = int(file_level.readline())
    if level == 1:
        piece_1 = mclass(200,250, "Assets\\molecule\\8.png")
        piece_2 = mclass(500,245,'Assets\\molecule\\3.png')
        collisionneur = cclass(490, 400)
        collisionneur2 = cclass(200, 400)
        fenetre_jeu.blit(piece_1.get_image(), dest=(piece_1.x, piece_1.y))
        fenetre_jeu.blit(piece_2.get_image(), dest=(piece_2.x, piece_2.y))
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
        fenetre_jeu.blit(collisionneur2.image, dest=(collisionneur2.x, collisionneur2.y))
    while not exit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

def main_menu():
    exit = False
    fenetre.blit(background_image, dest=(-25, 0))
    fenetre.blit(title, dest=(175, -0))
    j = fenetre.blit(boutton_jouer, dest=(100, 245))
    o = fenetre.blit(boutton_option, dest=(100, 500))
    while not exit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()
                if o.collidepoint(pos):
                    print("Options")

                if j.collidepoint(pos):
                    game(fenetre)
                    exit = True
                    print("Jeu")
        pygame.display.update()


main_menu()
