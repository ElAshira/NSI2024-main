import pygame

pygame.init()

fenetre = pygame.display.set_mode((800,800))

pygame.display.set_caption("Antivirus")

background_image =  pygame.image.load("Assets\\background.png")
title = pygame.image.load("Assets\\title.png")
boutton_jouer = pygame.image.load("Assets\\BOUTTON_JOUER.png")
boutton_option = pygame.image.load("Assets\\boutton_option.png")
exit = False

def game(fenetre):

    pygame.display.set_caption("Antivirus")

    game_background = pygame.image.load("Assets\\game_background.png")
    fenetre.blit(game_background, dest=(0, 0))

    grille_image = pygame.image.load("Assets\\PlateauDeJeu.png")
    fenetre.blit(grille_image, dest=(-85,150))




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
                    print("Jeu")
        pygame.display.update()

main_menu()

