import random
import pygame
class Molecule:
    def __init__(self, x,y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.can_move = True

    def move(self,x,y):
        self.x += x
        self.y += y
    def get_image(self):
        return self.image
    def get_position(self):
        return (self.x, self.y)

    def set_position(self,x,y):
        self.x = x
        self.y = y

class Colisionneur:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Assets\\molecule\\block.png")
        self.can_move = False
    def set_position(self,x,y):
        self.x = x
        self.y = y
