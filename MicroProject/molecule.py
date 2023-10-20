import random
import pygame
class Molecule:
    def __init__(self, x,y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)

    def move(self,x,y):
        self.x += x
        self.y += y

    def get_position(self):
        return (self.x, self.y)

    def set_position(self,x,y):
        self.x = x
        self.y = y

