import pygame
import math

WIDTH = 800
HEIGHT = 600

class DoublePendulum:
    def __init__(self, x, y, l1, l2, m1, m2, a1, a2):
        self.x = x
        self.y = y
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.a1 = a1
        self.a2 = a2
        self.a1_v = 0
        self.a2_v = 0
        self.g = 1

    def update(self):
        num1 = -self.g * (2 * self.m1 + self.m2) * math.sin(self.a1)
        num2 = -self.m2 * self.g * math.sin(self.a1 - 2 * self.a2)
        num3 = -2 * math.sin(self.a1 - self.a2) * self.m2
        num4 = self.a2_v * self.a2_v * self.l2 + self.a1_v * self.a1_v * self.l1 * math.cos(self.a1 - self.a2)
        den = self.l1 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.a1 - 2 * self.a2))
        self.a1_a = (num1 + num2 + num3 * num4) / den

        num1 = 2 * math.sin(self.a1 - self.a2)
        num2 = self.a1_v * self.a1_v * self.l1 * (self.m1 + self.m2)
        num3 = self.g * (self.m1 + self.m2) * math.cos(self.a1)
        num4 = self.a2_v * self.a2_v * self.l2 * self.m2 * math.cos(self.a1 - self.a2)
        den = self.l2 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.a1 - 2 * self.a2))
        self.a2_a = (num1 * (num2 + num3 + num4)) / den

        self.a1_v += self.a1_a
        self.a2_v += self.a2_a
        self.a1 += self.a1_v
        self.a2 += self.a2_v

        self.x1 = self.x + self.l1 * math.sin(self.a1)
        self.y1 = self.y + self.l1 * math.cos(self.a1)
        self.x2 = self.x1 + self.l2 * math.sin(self.a2)
        self.y2 = self.y1 + self.l2 * math.cos(self.a2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Double Pendulum Simulation")

    pendulum = DoublePendulum(WIDTH // 2, 50, 150, 150, 10, 10, math.pi / 2, math.pi)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pendulum.update()

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (pendulum.x, pendulum.y), (pendulum.x1, pendulum.y1), 2)
        pygame.draw.circle(screen, (255, 0, 0), (int(pendulum.x1), int(pendulum.y1)), 10)
        pygame.draw.line(screen, (255, 255, 255), (pendulum.x1, pendulum.y1), (pendulum.x2, pendulum.y2), 2)
        pygame.draw.circle(screen, (0, 0, 255), (int(pendulum.x2), int(pendulum.y2)), 10)

        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()

if __name__ == '__main__':
    main()