# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
#from player import Player
from player import Player
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pyg_clock = pygame.time.Clock()
    dt        = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x      = SCREEN_WIDTH / 2
    y      = SCREEN_HEIGHT / 2
    tplayer = Player(x, y, PLAYER_RADIUS)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill([0,0,0])
        tplayer.draw(screen)
        pygame.display.flip()
        elased_milliseecond = pyg_clock.tick(60)
        dt += elased_milliseecond / 1000


if __name__ == "__main__":
    main()
