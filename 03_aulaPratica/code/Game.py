import pygame
from .Menu import Menu
from .Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from .Level import Level


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.init()
        print("Game iniciado")

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            print("Menu encerrado")

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run()

                if level_return == "exit":
                    print("Level encerrado")
                    pygame.quit()
                    break
                elif level_return == "menu":
                    print("Level encerrado")
                    continue
            elif menu_return == "exit" or MENU_OPTION[3]:
                print("Game encerrado")
                pygame.quit()
                break
