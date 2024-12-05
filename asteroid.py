import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y
        #self.radius = radius
        #self.position = pygame.Vector2(x, y)
 
    def draw(self, screen):
        line_width = 2
        [x, y] = self.position
    
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
