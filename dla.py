import pygame
import random

WIDTH = 800
HEIGHT = 600
NUM_PARTICLES = 500

class Particle:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def update(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

def create_particle(aggregated_particles):
    while True:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        if not any(p.x == x and p.y == y for p in aggregated_particles):
            break
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    size = 2
    return Particle(x, y, color, size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Diffusion-Limited Aggregation Simulation")

    aggregated_particles = [Particle(WIDTH // 2, HEIGHT // 2, (255, 255, 255), 2)]
    moving_particles = [create_particle(aggregated_particles) for _ in range(NUM_PARTICLES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for particle in moving_particles:
            particle.update()
            for aggregated_particle in aggregated_particles:
                dx = particle.x - aggregated_particle.x
                dy = particle.y - aggregated_particle.y
                distance = dx * dx + dy * dy
                if distance <= 4:
                    aggregated_particles.append(particle)
                    moving_particles.remove(particle)
                    moving_particles.append(create_particle(aggregated_particles))
                    break

        screen.fill((0, 0, 0))
        for particle in aggregated_particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)
        for particle in moving_particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()