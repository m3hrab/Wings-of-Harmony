import pygame, random

class Cursor:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.pos = [0, 0]
        pygame.mouse.set_visible(False) 

        self.tool = "tool1"
    
    def change_tool(self):
        if self.tool == "tool1":
            self.tool = "tool2"
            self.image = pygame.image.load("assets/images/tool2.png")

        else:
            self.tool = "tool1"
            self.image = pygame.image.load("assets/images/tool1.png")


    def update_pos(self, pos):
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)


