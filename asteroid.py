import circleshape
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", radius=self.radius, center=self.position,width=2)

    def update(self, dt):
        self.position+=self.velocity*dt