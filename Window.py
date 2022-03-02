import pygame
from Color import Color
from Object import Object


class Window:
    def __init__(self) -> None:
        pygame.init()
        self.FONT = pygame.font.SysFont("comicsans", 16)
        WIDTH, HEIGHT = 800, 800
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Planet Simulation")
    
    def close(self) -> None:
        pygame.quit()

    def update(self) -> None:
        pygame.display.update()

    def run(self) -> None:
        run = True
        clock = pygame.time.Clock()

        sun = Object(0, 0, 30, Color.yellow, 1.98892 * 10**30, 0, "Sun")
        sun.star = True

        earth = Object(-1 * Object.AU, 0, 16, Color.blue, 5.9742 * 10**24, 29.783 * 1000, "Earth")

        mars = Object(-1.524 * Object.AU, 0, 12, Color.red, 6.39 * 10**23, 24.077 * 1000, "Mars")

        mercury = Object(-0.387 * Object.AU, 0, 8, Color.dark_grey, 0.330 * 10**24, 47.4 * 1000, "Mercury")

        venus = Object(0.723 * Object.AU, 0, 14, Color.white, 4.8685 * 10**24, -35.02 * 1000, "Venus")
        objects = [sun, earth, mars, mercury, venus]
        while run:
            clock.tick(60)
            self.WIN.fill(Color.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            for obj in objects:
                obj.update_position(objects)
                obj.draw(self.WIN, self.FONT, pygame)
            self.update()
            
        self.close()
