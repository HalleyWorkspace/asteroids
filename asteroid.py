from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", radius=self.radius, center=self.position,width=2)

    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle=random.uniform(20,50)
            vector1=self.velocity.rotate(random_angle)
            vector2=self.velocity.rotate(random_angle*-1)
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            a1=Asteroid(self.position.x,self.position.y,new_radius)
            a2=Asteroid(self.position.x,self.position.y,new_radius)
            a1.velocity=vector1*1.2
            a2.velocity=vector2*1.2