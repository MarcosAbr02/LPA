import pygame
from .Menu import Menu
from .Const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        print("Game iniciado")

        while True:
            menu = Menu(self.window)
            menu.run()
            print("Game encerrado")
            pygame.quit()
            break
