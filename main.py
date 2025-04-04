import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(
            "black"
        )
        pygame.display.flip()

        #End of Gameloop 
        delta_time = game_clock.tick(60) #tick 60 limits the FPS to 60
        dt = delta_time / 1000 #convert to ms



if __name__ == "__main__":
    main()
