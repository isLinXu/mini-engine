import pygame
import random
import math

class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    def update(self, width, height):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.vx = -self.vx
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.vy = -self.vy

class Simulation:
    def __init__(self, width, height, num_balls):
        self.width = width
        self.height = height
        self.balls = [self.create_random_ball() for _ in range(num_balls)]

    def create_random_ball(self):
        x = random.randint(50, self.width - 50)
        y = random.randint(50, self.height - 50)
        radius = random.randint(10, 30)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        speed = random.uniform(1, 3)
        return Ball(x, y, radius, color, speed)

    def update(self):
        for ball in self.balls:
            ball.update(self.width, self.height)

        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                dx = ball1.x - ball2.x
                dy = ball1.y - ball2.y
                distance = math.sqrt(dx * dx + dy * dy)

                if distance < ball1.radius + ball2.radius:
                    ball1.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                    ball2.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ball Collision Simulation")

    def render(self, simulation):
        self.screen.fill((0, 0, 0))
        for ball in simulation.balls:
            pygame.draw.circle(self.screen, ball.color, (int(ball.x), int(ball.y)), ball.radius)

        pygame.display.flip()

    def quit(self):
        pygame.quit()

def main():
    simulation = Simulation(800, 600, 10)
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