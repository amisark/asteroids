# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pyg_clock = pygame.time.Clock()
    dt        = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x      = SCREEN_WIDTH / 2
    y      = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    tplayer = Player(x, y)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        #screen.fill([0,0,0])
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        elased_milliseecond = pyg_clock.tick(60)
        dt += elased_milliseecond / 1000


if __name__ == "__main__":
    main()
