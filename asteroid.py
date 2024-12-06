import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 
    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        else :
            rand_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate( rand_angle) * 1.2
            velocity2 = self.velocity.rotate(-rand_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity1
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity2

