import pygame
import random

WIDTH = 800
HEIGHT = 600
NUM_PARTICLES = 50

class Particle:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def update(self):
        self.x += random.uniform(-2, 2)
        self.y += random.uniform(-2, 2)

def create_particle():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    size = random.uniform(2, 5)
    return Particle(x, y, color, size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion Simulation")

    particles = [create_particle() for _ in range(NUM_PARTICLES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for particle in particles:
            particle.update()

        screen.fill((0, 0, 0))
        for particle in particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), int(particle.size))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()