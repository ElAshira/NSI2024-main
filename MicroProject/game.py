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


def game():
    exit = False
    fenetre_jeu = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("En jeu!")

    game_background = pygame.image.load("Assets\\game_background.png")
    fenetre_jeu.blit(game_background, dest=(0, 0))

    grille_image = pygame.image.load("Assets\\PlateauDeJeu.png")
    fenetre_jeu.blit(grille_image, dest=(-85, 150))
    file_level = open("file_level.txt")
    level = int(file_level.readline())
    if level == 1:
        pink = mclass(200, 250, "Assets\\molecule\\8.png")
        virus = mclass(500, 245, 'Assets\\molecule\\3.png')
        collisionneur = cclass(490, 400)
        collisionneur2 = cclass(200, 400)
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
        fenetre_jeu.blit(collisionneur2.image, dest=(collisionneur2.x, collisionneur2.y))
        fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
        fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
    selected = "pink"
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                print(selected)
                if selected == "pink":
                    selected = "virus"
                elif selected == "virus":
                    selected = "pink"
            if selected == "pink":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pink.move(-5,-5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    pink.move(5,5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    pink.move(-5, 5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    pink.move(5, -5)
            if selected == "virus":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    virus.move(-5,-5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    virus.move(5,5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    virus.move(-5, 5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    virus.move(5, -5)
        # Redraw the game elements
        fenetre_jeu.blit(game_background, dest=(0, 0))
        fenetre_jeu.blit(grille_image, dest=(-85, 150))
        fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
        fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
        fenetre_jeu.blit(collisionneur2.image, dest=(collisionneur2.x, collisionneur2.y))

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
                    game()
                    exit = True
                    print("Jeu")
        pygame.display.update()


main_menu()
