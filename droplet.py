import pygame
import random
import math

class Droplet:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.vy = 0

    def update(self, height):
        self.vy += self.speed
        self.y += self.vy

        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy = -self.vy * 0.8

class Simulation:
    def __init__(self, width, height, num_droplets):
        self.width = width
        self.height = height
        self.droplets = [self.create_random_droplet() for _ in range(num_droplets)]

    def create_random_droplet(self):
        x = random.randint(50, self.width - 50)
        y = random.randint(50, self.height // 2)
        radius = random.randint(5, 10)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        speed = random.uniform(0.1, 0.3)
        return Droplet(x, y, radius, color, speed)

    def update(self):
        for droplet in self.droplets:
            droplet.update(self.height)

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Liquid Droplets Simulation")

    def render(self, simulation):
        self.screen.fill((0, 0, 0))
        for droplet in simulation.droplets:
            pygame.draw.circle(self.screen, droplet.color, (int(droplet.x), int(droplet.y)), droplet.radius)

        pygame.display.flip()

    def quit(self):
        pygame.quit()

def main():
    simulation = Simulation(800, 600, 20)
    renderer = Renderer(800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.update()
        renderer.render(simulation)

    renderer.quit()

if __name__ == '__main__':
    main()