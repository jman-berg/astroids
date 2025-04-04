import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(
            "black"
        )

        updatable_group.update(dt)

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        #End of Gameloop 
        delta_time = game_clock.tick(60) #tick 60 limits the FPS to 60
        dt = delta_time / 1000 #convert to ms



if __name__ == "__main__":
    main()
