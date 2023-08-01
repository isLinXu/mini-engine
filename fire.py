import pygame
import random

WIDTH = 800
HEIGHT = 600
NUM_PARTICLES = 200

class Particle:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-5, -1)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1
        self.color = (self.color[0], max(0, self.color[1] - 2), max(0, self.color[2] - 2))

def create_particle(x, y):
    color = (255, random.randint(100, 255), 0)
    size = random.uniform(1, 4)
    return Particle(x, y, color, size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fire Simulation")

    particles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        particles.append(create_particle(WIDTH // 2, HEIGHT - 10))

        if len(particles) > NUM_PARTICLES:
            particles.pop(0)

        for particle in particles:
            particle.update()

        screen.fill((0, 0, 0))
        for particle in particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), int(particle.size))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()