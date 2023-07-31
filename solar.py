# import pygame
# import random
# import math
#
# class CelestialBody:
#     def __init__(self, x, y, size, mass, color):
#         self.x = x
#         self.y = y
#         self.vx = 0
#         self.vy = 0
#         self.ax = 0
#         self.ay = 0
#         self.size = size
#         self.mass = mass
#         self.color = color
#
#     def update(self):
#         self.vx += self.ax
#         self.vy += self.ay
#         self.x += self.vx
#         self.y += self.vy
#
# class SolarSystem:
#     def __init__(self, width, height, num_planets):
#         self.width = width
#         self.height = height
#         self.sun = CelestialBody(width // 2, height // 2, 30, 1000, (255, 255, 0))
#         self.planets = [self.create_random_planet() for _ in range(num_planets)]
#
#     def create_random_planet(self):
#         angle = random.uniform(0, 2 * math.pi)
#         distance = random.uniform(100, 250)
#         x = self.width // 2 + math.cos(angle) * distance
#         y = self.height // 2 + math.sin(angle) * distance
#         size = random.randint(5, 10)
#         mass = random.randint(10, 50)
#         color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
#         planet = CelestialBody(x, y, size, mass, color)
#         speed = math.sqrt(0.1 * self.sun.mass / distance)
#         planet.vx = -math.sin(angle) * speed
#         planet.vy = math.cos(angle) * speed
#         return planet
#
#     def update(self):
#         for planet in self.planets:
#             dx = self.sun.x - planet.x
#             dy = self.sun.y - planet.y
#             distance = (dx**2 + dy**2)**0.5
#             force = 0.1 * self.sun.mass * planet.mass / distance**2
#             ax = force * dx / distance / planet.mass
#             ay = force * dy / distance / planet.mass
#             planet.ax = ax
#             planet.ay = ay
#             planet.update()
#
# class Renderer:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         pygame.init()
#         self.screen = pygame.display.set_mode((width, height))
#         pygame.display.set_caption("Solar System Simulation")
#
#     def render(self, solar_system):
#         self.screen.fill((0, 0, 0))
#         pygame.draw.circle(self.screen, solar_system.sun.color, (int(solar_system.sun.x), int(solar_system.sun.y)), solar_system.sun.size)
#         for planet in solar_system.planets:
#             pygame.draw.circle(self.screen, planet.color, (int(planet.x), int(planet.y)), planet.size)
#
#         pygame.display.flip()
#
#     def quit(self):
#         pygame.quit()
#
# def main():
#     solar_system = SolarSystem(800, 600, 5)
#     renderer = Renderer(800, 600)
#
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         solar_system.update()
#         renderer.render(solar_system)
#
#     renderer.quit()
#
# if __name__ == '__main__':
#     main()

import pygame
import math

class CelestialBody:
    def __init__(self, x, y, size, mass, color):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.size = size
        self.mass = mass
        self.color = color

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

class SolarSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sun = CelestialBody(width // 2, height // 2, 30, 1000, (255, 255, 0))
        self.planets = [self.create_planet(i) for i in range(8)]

    def create_planet(self, index):
        planet_data = [
            # (distance, mass, size, color)
            (50, 10, 5, (200, 200, 200)),   # Mercury
            (80, 20, 6, (200, 150, 100)),  # Venus
            (110, 25, 6, (100, 150, 255)), # Earth
            (145, 15, 4, (255, 100, 100)), # Mars
            (250, 70, 15, (255, 200, 100)),# Jupiter
            (400, 50, 12, (200, 255, 200)),# Saturn
            (550, 30, 10, (100, 200, 255)),# Uranus
            (700, 25, 9, (100, 100, 255))  # Neptune
        ]
        distance, mass, size, color = planet_data[index]
        x = self.width // 2 + distance
        y = self.height // 2
        planet = CelestialBody(x, y, size, mass, color)
        speed = math.sqrt(0.1 * self.sun.mass / distance)
        planet.vx = 0
        planet.vy = speed
        return planet

    def update(self):
        for planet in self.planets:
            dx = self.sun.x - planet.x
            dy = self.sun.y - planet.y
            distance = (dx**2 + dy**2)**0.5
            force = 0.1 * self.sun.mass * planet.mass / distance**2
            ax = force * dx / distance / planet.mass
            ay = force * dy / distance / planet.mass
            planet.ax = ax
            planet.ay = ay
            planet.update()

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Solar System Simulation")

    def render(self, solar_system):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, solar_system.sun.color, (int(solar_system.sun.x), int(solar_system.sun.y)), solar_system.sun.size)
        for planet in solar_system.planets:
            pygame.draw.circle(self.screen, planet.color, (int(planet.x), int(planet.y)), planet.size)

        pygame.display.flip()

    def quit(self):
        pygame.quit()

def main():
    solar_system = SolarSystem(1920, 1080)
    renderer = Renderer(1920, 1080)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        solar_system.update()
        renderer.render(solar_system)

    renderer.quit()

if __name__ == '__main__':
    main()