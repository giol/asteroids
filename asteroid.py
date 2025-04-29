from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # overriden
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # overriden
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        left_velocity = self.velocity.rotate(random_angle * -1) * 1.2
        right_velocity = self.velocity.rotate(random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a_left = Asteroid(self.position[0], self.position[1], new_radius)
        a_right = Asteroid(self.position[0], self.position[1], new_radius)
        a_left.velocity = left_velocity
        a_right.velocity = right_velocity

