import pygame 
import random

class Critter():
    def __init__(self, screen, critter_type, image):
        self.screen = screen
        self.critter_type = critter_type
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.move = [random.randint(-15, 15), random.randint(-15, 15)]

        # Set the initial position of the critter
        self.rect.center = [self.screen.get_width() // 2, self.screen.get_height() // 2]
        self.radius = min(self.rect.width, self.rect.height) // 2

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move_critter(self):
        self.rect.centerx += self.move[0]
        self.rect.centery += self.move[1]

    def check_bounce(self):
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.move[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.move[1] *= -1

    def did_get(self, location, cursor_tool):

        # Create a rectangle for the location
        if cursor_tool == "tool1":
            location_rect = pygame.Rect(location[0], location[1], 80, 80)
        else:
            location_rect = pygame.Rect(location[0], location[1], 110, 110)
        if location_rect.collidepoint(self.rect.centerx, self.rect.centery):
            return self.critter_type
        
        else:
            return None