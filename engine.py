import pygame
import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.ax = 0
        self.ay = 0.1
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.size = random.randint(3, 8)

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

class Scene:
    def __init__(self, width, height, num_particles):
        self.width = width
        self.height = height
        self.particles = [Particle(random.uniform(0, width), random.uniform(0, height)) for i in range(num_particles)]

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.x < 0 or particle.x > self.width:
                particle.vx *= -1
            if particle.y < 0 or particle.y > self.height:
                particle.vy *= -1

    def handle_mouse_motion(self, mouse_x, mouse_y):
        for particle in self.particles:
            dx = mouse_x - particle.x
            dy = mouse_y - particle.y
            distance = (dx**2 + dy**2)**0.5
            if distance < 100:
                particle.ax = -dx / distance * 0.5
                particle.ay = -dy / distance * 0.5
            else:
                particle.ax = 0
                particle.ay = 0.1

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Particle Physics")

    def render(self, scene):
        self.screen.fill((0, 0, 0))
        for particle in scene.particles:
            pygame.draw.circle(self.screen, particle.color, (int(particle.x), int(particle.y)), particle.size)

        pygame.display.flip()

    def quit(self):
        pygame.quit()

def main():
    scene = Scene(800, 600, 100)
    renderer = Renderer(800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                scene.handle_mouse_motion(mouse_x, mouse_y)

        scene.update()
        renderer.render(scene)

    renderer.quit()

if __name__ == '__main__':
    main()