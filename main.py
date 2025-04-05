import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Shot.containers = (shots_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

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

        for shot in shots_group:
            shot.update(dt)

        for asteroid in asteroids_group:
            collision = asteroid.check_collision(player)
            if collision:
                print("Game over!")
                return
            
            for shot in shots_group:
                collision = asteroid.check_collision(shot)
                if collision:
                    asteroid.split()
                    shot.kill()


        pygame.display.flip()

        #End of Gameloop 
        delta_time = game_clock.tick(60) #tick 60 limits the FPS to 60
        dt = delta_time / 1000 #convert to ms



if __name__ == "__main__":
    main()
