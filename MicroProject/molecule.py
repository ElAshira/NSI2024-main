import random
import pygame
class Molecule:
    def __init__(self, x,y, image,hitbox_list):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox_list= hitbox_list
        self.hitbox= pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        for i in self.hitbox_list:
            i[0] += dx
            i[1] += dy


    def get_image(self):
        return self.image
    def get_position(self):
        return (self.x, self.y)

    def set_position(self,x,y):
        self.x = x
        self.y = y

class Colisionneur:
    def __init__(self, x,y, width,height):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Assets\\molecule\\block.png")
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x +5, self.y+5, self.width, self.height)
        self.can_move = False
    def set_position(self,x,y):
        self.x = x
        self.y = y