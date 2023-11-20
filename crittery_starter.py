# task1.py
import pygame
import random
from cursor import Cursor
from critter2 import Critter
pygame.mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "Crittery"

LEVEL_UP_SOUND = pygame.mixer.Sound("assets/sounds/level_up.wav")
LOSE_SOUND = pygame.mixer.Sound("assets/sounds/lose.wav")
CHOPSTICK_SOUND = pygame.mixer.Sound("assets/sounds/chopstick.wav")
SPRAY_SOUND = pygame.mixer.Sound("assets/sounds/spray.wav")
BGM = pygame.mixer.Sound("assets/sounds/bgm2.mp3")
BGM.set_volume(0.5)
BGM.play(-1)

def make_critters_list(count, screen, images):
    critters_list = []
    for _ in range(count):
        critter_type = "good" if len(critters_list) < count // 2 else "bad"
        critter_image = random.choice(images[critter_type])
        critter = Critter(screen, critter_type, critter_image)
        critters_list.append(critter)
    return critters_list

def display_text(screen, message, color, position):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, color)
    screen.blit(text, position)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()


    background_image = pygame.image.load("assets/images/background.jpg")  
    bg_rect = background_image.get_rect()

    cursor = Cursor("assets/images/tool1.png") 

    good_critter_image = pygame.image.load("assets/images/good.png")  # Replace with your image
    bad_critter_image = pygame.image.load("assets/images/bad.png")  # Replace with your image
    critter_images = {"good": [good_critter_image], "bad": [bad_critter_image]}

    critter_count = 10
    critters_list = make_critters_list(critter_count, screen, critter_images)

    game_over = False
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    # Reset Game
                    game_over = False
                    critter_count += 10
                    critters_list = make_critters_list(critter_count, screen, critter_images)
                    
                elif event.key == pygame.K_RETURN and game_over:
                    # Reset Game
                    game_over = False
                    start_time = pygame.time.get_ticks()
                    critter_count += 10
                    critters_list = make_critters_list(critter_count, screen, critter_images)
                    if cursor.tool == "tool2":
                        cursor.change_tool()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if cursor.tool == "tool1":
                        CHOPSTICK_SOUND.play()
                    else:
                        SPRAY_SOUND.play()

                    if not game_over:
                        for critter in critters_list:
                            critter_type = critter.did_get(cursor.pos, cursor.tool)
                            if critter_type is not None:
                                if critter_type == "good" and cursor.tool == "tool1":
                                    critters_list.remove(critter)
                                    cursor.change_tool()
                                        
                                elif critter_type == "bad" and cursor.tool == "tool2":
                                    critters_list.remove(critter)
                                    cursor.change_tool() 
            
                                else:
                                    temp_critter_type = critter_type
                                    game_over = True
                                    critter_count = 0 
                                    LOSE_SOUND.play()

    

        cursor.update_pos(pygame.mouse.get_pos())

        for critter in critters_list:
            critter.move_critter()
            critter.check_bounce()
        
        if not game_over:
            if len(critters_list) == 0:
                elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 
                LEVEL_UP_SOUND.play()
                game_over = True
            


        screen.blit(background_image, bg_rect)

        if game_over and len(critters_list)==0:
            message = f"You did it in {elapsed_time:.2f} seconds"
            display_text(screen, message, (0, 250, 0), (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 150))
            display_text(screen, "Hit enter for the next round", (0, 250, 0), (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100))
        
        elif game_over and len(critters_list) > 0:
            if temp_critter_type == "good":
                message = "You killed a butterfly!"
            else:
                message = "You caught a wasp!"

            display_text(screen, message, (250, 0, 0), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
            display_text(screen, "Hit Enter to try again", (250, 0, 0), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
        
        if len(critters_list) > 0: 
            for critter in critters_list:
                critter.draw()

            cursor.draw(screen)

        pygame.display.flip()
        clock.tick(CLOCK_TICK)

if __name__ == "__main__":
    main()

