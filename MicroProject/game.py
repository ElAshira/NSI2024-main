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


def selection_level():
    level_selection = pygame.display.set_mode((800, 800))
    exit = False
    level_selection.blit(background_image, dest=(0, 0))

    image_easy = pygame.image.load("Assets/level_png/ez.png")
    image_medium = pygame.image.load("Assets/level_png/medium.png")
    hit_medium = level_selection.blit(image_medium, dest=(205, 250))
    image_easy = level_selection.blit(image_easy, dest=(200, 100))
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()
                if hit_medium.collidepoint(pos):
                    level_2()
                    exit = True
                if image_easy.collidepoint(pos):
                    game()
                    exit = True

        pygame.display.update()


def game():
    exit = False
    fenetre_jeu = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("En jeu!")
    fleche_sortie = pygame.image.load("Assets/fleche.png")
    fleche_sortie_rotated = pygame.transform.rotate(fleche_sortie, -5)
    virus_on = pygame.image.load("Assets/SelectionMoleculeImage/virus_on.png")
    virus_off = pygame.image.load('Assets/SelectionMoleculeImage/virus_off.png')
    pink_on = pygame.image.load("Assets/SelectionMoleculeImage/piece_1.png")
    pink_off = pygame.image.load("Assets/SelectionMoleculeImage/piece_1_off.png")

    game_background = pygame.image.load("Assets\\game_background.png")
    fenetre_jeu.blit(game_background, dest=(0, 0))

    grille_image = pygame.image.load("Assets\\PlateauDeJeu.png")
    fenetre_jeu.blit(grille_image, dest=(-85, 150))

    file_level = open("file_level.txt")
    level = int(file_level.readline())
    if level == 1:  #
        pink = mclass(200, 250, "Assets\\molecule\\5.png",
                      [pygame.Rect((215, 265, 72, 75)), pygame.Rect((250, 285, 180, 35)),
                       pygame.Rect((365, 265, 72, 75)), pygame.Rect((235, 330, 30, 70)),
                       pygame.Rect((210, 410, 80, 70))])
        virus = mclass(280, 320, 'Assets\\molecule\\3.png',
                       [pygame.Rect((290, 335, 70, 70)), pygame.Rect((330, 375, 70, 70)),
                        pygame.Rect((370, 415, 70, 70))])
        collisionneur = cclass(490, 400, 60, 60)
        wincondition = pygame.Rect(70, 130, 70, 70)
        topborder = pygame.Rect(180, 150, 500, 25)
        rightborder = pygame.Rect(660, 180, 25, 480)
        bottomborder = pygame.Rect(660, 720, -500, 25)
        leftborder = pygame.Rect(100, 750, 25, -500)
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
        fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
        fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
        hitboxes_pink = [virus.hitbox_list[0], virus.hitbox_list[1], virus.hitbox_list[2],
                         collisionneur.hitbox_liste[0],
                         collisionneur.hitbox_liste[1], collisionneur.hitbox_liste[2], topborder, rightborder,
                         bottomborder, leftborder]
        hitboxes_virus = [pink.hitbox_list[0], pink.hitbox_list[1], pink.hitbox_list[2], pink.hitbox_list[3],
                          pink.hitbox_list[4], collisionneur.hitbox_liste[0],
                          collisionneur.hitbox_liste[1],
                          collisionneur.hitbox_liste[1],
                          collisionneur.hitbox_liste[2], topborder, rightborder, bottomborder, leftborder]

        # Create a copy of pink's hitbox with its current position
    show_hitbox = False
    selected = "pink"
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            for rect in hitboxes_pink:
                if rect.colliderect(wincondition):
                    exit = True
                    main_menu()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                if show_hitbox:
                    show_hitbox = False
                else:
                    show_hitbox = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                print("condition vérifié")
                if selected == "pink":
                    selected = "virus"
                    fenetre_jeu.blit(virus_on, dest=(80, 20))
                    fenetre_jeu.blit(pink_off, dest=(100, 20))
                elif selected == "virus":
                    fenetre_jeu.blit(virus_off, dest=(80, 20))
                    fenetre_jeu.blit(pink_on, dest=(100, 20))
                    selected = "pink"
            if selected == "pink":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pink.move(-40, -40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(40, 40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

                    pink.move(40, 40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(-40, -40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    pink.move(-40, 40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(40, -40)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    pink.move(40, -40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(-40, 40)

            if selected == "virus":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    virus.move(-40, -40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(40, 40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    virus.move(40, 40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(-40, -40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    virus.move(-40, 40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(40, -40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    virus.move(40, -40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(-40, 40)
        # Redraw the game elements
        fenetre_jeu.blit(game_background, dest=(0, 0))
        fenetre_jeu.blit(grille_image, dest=(-85, 150))
        fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
        fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
        if selected == "virus":
            fenetre_jeu.blit(virus_on, dest=(80, 20))
            fenetre_jeu.blit(pink_off, dest=(170, 19))
        elif selected == "pink":
            fenetre_jeu.blit(virus_off, dest=(80, 20))
            fenetre_jeu.blit(pink_on, dest=(170, 19))
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))

        if show_hitbox:
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), collisionneur.hitbox, 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), virus.hitbox_list[0], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), virus.hitbox_list[1], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), virus.hitbox_list[2], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), pink.hitbox_list[0], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), pink.hitbox_list[1], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), pink.hitbox_list[2], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), pink.hitbox_list[2], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (70, 130, 70, 70), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (180, 150, 480, 25), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (660, 180, 25, 500), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (660, 720, -500, 25), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (0, 750, 25, -500), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), collisionneur.hitbox_liste[1], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), collisionneur.hitbox_liste[0], 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (235, 330, 30, 90), 2)
            pygame.draw.rect(fenetre_jeu, (255, 0, 0), (210, 410, 80, 70), 2)
        fenetre_jeu.blit(fleche_sortie_rotated, dest=(10, 100))
        pygame.display.update()


def pop_up():
    pop_up = pygame.display.set_mode((200, 200))
    pop_up.fill((255, 255, 255))


def level_2():
    fleche_sortie = pygame.image.load("Assets/fleche.png")
    fleche_sortie_rotated = pygame.transform.rotate(fleche_sortie, -5)
    virus_on = pygame.image.load("Assets/SelectionMoleculeImage/virus_on.png")
    virus_off = pygame.image.load('Assets/SelectionMoleculeImage/virus_off.png')
    pink_on = pygame.image.load("Assets/SelectionMoleculeImage/piece_1.png")
    pink_off = pygame.image.load("Assets/SelectionMoleculeImage/piece_1_off.png")
    orange_on = pygame.image.load("Assets/SelectionMoleculeImage/piece_2_on.png")
    orange_off = pygame.image.load("Assets/SelectionMoleculeImage/piece_2_off.png")
    exit = False
    selected = "pink"
    fenetre_jeu = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("En jeu!")
    grille_image = pygame.image.load("Assets\\PlateauDeJeu.png")

    fenetre_jeu.blit(background_image, dest=(0, 0))
    fenetre_jeu.blit(grille_image, dest=(-85, 100))

    pink = mclass(420, 470, "Assets/molecule/8_rotated.png",
                  [pygame.Rect(445, 435, 80, 70), pygame.Rect((470, 500, 35, 100)),
                   pygame.Rect((445, 590, 80, 70))])
    virus = mclass(440, 330, 'Assets\\molecule\\3.png',
                   [pygame.Rect((450, 290, 70, 70)), pygame.Rect((490, 330, 70, 70)),
                    pygame.Rect((525, 365, 70, 70))])
    orange = mclass(350, 170, "Assets/molecule/4.png", [
        pygame.Rect((365, 265, 70, 70)), pygame.Rect((525, 265, 70, 70)), pygame.Rect((445, 190, 70, 70)),
        pygame.Rect((445, 170, 70, 70)), pygame.Rect((365, 265, 70, 70))])
    collisionneur = cclass(345, 390, 60, 60)
    wincondition = pygame.Rect(70, 130, 70, 70)
    topborder = pygame.Rect(180, 150, 500, 25)
    rightborder = pygame.Rect(660, 180, 25, 480)
    bottomborder = pygame.Rect(660, 720, -500, 25)
    leftborder = pygame.Rect(100, 750, 25, -500)
    fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
    fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
    fenetre_jeu.blit(orange.image, dest=(orange.x, orange.y))
    fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
    hitboxes_pink = [virus.hitbox_list[0], virus.hitbox_list[1], virus.hitbox_list[2],
                     collisionneur.hitbox_liste[0],
                     collisionneur.hitbox_liste[1], collisionneur.hitbox_liste[2], topborder, rightborder, bottomborder,
                     leftborder, orange.hitbox_list[0], orange.hitbox_list[1], orange.hitbox_list[2],
                     orange.hitbox_list[3], orange.hitbox_list[4]]
    hitboxes_virus = [pink.hitbox_list[0], pink.hitbox_list[1], pink.hitbox_list[2], collisionneur.hitbox_liste[0],
                      collisionneur.hitbox_liste[1],
                      collisionneur.hitbox_liste[1],
                      collisionneur.hitbox_liste[2], topborder, rightborder, bottomborder, leftborder,
                      orange.hitbox_list[0], orange.hitbox_list[1], orange.hitbox_list[2], orange.hitbox_list[3],
                      orange.hitbox_list[4]]
    hitboxes_orange = [virus.hitbox_list[0], virus.hitbox_list[1], virus.hitbox_list[2],
                       collisionneur.hitbox_liste[0],
                       collisionneur.hitbox_liste[1], collisionneur.hitbox_liste[2], topborder, rightborder,
                       bottomborder, leftborder, pink.hitbox_list[0], pink.hitbox_list[1], pink.hitbox_list[2]

                       ]
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (450, 290, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (490, 330, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (525, 365, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (445, 435, 80, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (470, 500, 35, 100), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (445, 590, 80, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (365, 215, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (400, 190, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (445, 130, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (500, 190, 70, 70), 2)
    pygame.draw.rect(fenetre_jeu, (255, 0, 0), (525, 215, 70, 70), 2)
    selected = "pink"
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            for rect in hitboxes_pink:
                if rect.colliderect(wincondition):
                    exit = True
                    main_menu()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                if show_hitbox:
                    show_hitbox = False
                else:
                    show_hitbox = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                if selected == "pink":
                    selected = "virus"
                    fenetre_jeu.blit(virus_on, dest=(80, 20))
                    fenetre_jeu.blit(pink_off, dest=(170, 19))
                    fenetre_jeu.blit(orange_off, dest=(280, 27))

                elif selected == "virus":
                    fenetre_jeu.blit(virus_off, dest=(80, 20))
                    fenetre_jeu.blit(pink_off, dest=(170, 19))
                    fenetre_jeu.blit(orange_on, dest=(280, 27))

                    selected = "orange"
                elif selected == "orange":
                    fenetre_jeu.blit(virus_off, dest=(80, 20))
                    fenetre_jeu.blit(pink_on, dest=(170, 19))
                    fenetre_jeu.blit(orange_off, dest=(280, 27))
                    selected = "pink"

            if selected == "pink":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pink.move(-40, -40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(40, 40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

                    pink.move(40, 40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(-40, -40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    pink.move(-40, 40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(40, -40)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    pink.move(40, -40)
                    for rect1 in hitboxes_pink:
                        index = rect1.collidelist(pink.hitbox_list)
                        if index >= 0:
                            pink.move(-40, 40)

            if selected == "virus":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    virus.move(-40, -40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(40, 40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    virus.move(40, 40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(-40, -40)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    virus.move(-40, 40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(40, -40)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    virus.move(40, -40)
                    for rect1 in hitboxes_virus:
                        index = rect1.collidelist(virus.hitbox_list)
                        if index >= 0:
                            virus.move(-40, 40)
            if selected == "orange":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    orange.move(-30, -30)
                    for rect1 in hitboxes_orange:
                        index = rect1.collidelist(orange.hitbox_list)
                        if index >= 0:
                            orange.move(30, 30)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    orange.move(30, 30)
                    for rect1 in hitboxes_orange:
                        index = rect1.collidelist(orange.hitbox_list)
                        if index >= 0:
                            orange.move(-30, -30)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    orange.move(-30, 30)
                    for rect1 in hitboxes_orange:
                        index = rect1.collidelist(orange.hitbox_list)
                        if index >= 0:
                            orange.move(30, -30)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    orange.move(30, -30)
                    for rect1 in hitboxes_orange:
                        index = rect1.collidelist(orange.hitbox_list)
                        if index >= 0:
                            orange.move(-30, 30)
        # Redraw the game elements
        fenetre_jeu.blit(background_image, dest=(0, 0))
        fenetre_jeu.blit(grille_image, dest=(-85, 150))
        fenetre_jeu.blit(pink.image, dest=(pink.x, pink.y))
        fenetre_jeu.blit(virus.image, dest=(virus.x, virus.y))
        fenetre_jeu.blit(orange.image, dest=(orange.x, orange.y))
        fenetre_jeu.blit(collisionneur.image, dest=(collisionneur.x, collisionneur.y))
        if selected == "virus":
            fenetre_jeu.blit(virus_on, dest=(80, 20))
            fenetre_jeu.blit(pink_off, dest=(170, 19))
            fenetre_jeu.blit(orange_off, dest=(280, 27))
        elif selected == "pink":
            fenetre_jeu.blit(virus_off, dest=(80, 20))
            fenetre_jeu.blit(pink_on, dest=(170, 19))
            fenetre_jeu.blit(orange_off, dest=(280, 27))
        elif selected == "orange":
            fenetre_jeu.blit(virus_off, dest=(80, 20))
            fenetre_jeu.blit(pink_off, dest=(170, 19))
            fenetre_jeu.blit(orange_on, dest=(280, 27))
        fenetre_jeu.blit(fleche_sortie_rotated, dest=(10, 100))
        pygame.display.update()


def main_menu():
    exit = False
    fenetre.blit(background_image, dest=(-25, 0))
    fenetre.blit(title, dest=(175, -0))
    j = fenetre.blit(boutton_jouer, dest=(100, 245))
    o = fenetre.blit(boutton_option, dest=(100, 500))
    print(type(j))
    while not exit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()
                if o.collidepoint(pos):
                    selection_level()
                    exit = True
                if j.collidepoint(pos):
                    game()
                    exit = True

        pygame.display.update()


main_menu()
