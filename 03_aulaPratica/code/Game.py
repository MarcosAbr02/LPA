import pygame

from .Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from .Level import Level
from .Menu import Menu
from .Score import Score


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.init()
        print("Game iniciado")

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            print("MENU encerrado")

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, "Level1", menu_return, player_score)

                # É possível alterar os valores de player_score no escopo de run()
                level_return = level.run(player_score)

                if level_return == "exit":
                    print("LEVEL encerrado")
                    pygame.quit()
                    break

                elif level_return == "menu":
                    print("LEVEL encerrado")
                    continue

                elif level_return:
                    level2 = Level(self.window, "Level2", menu_return, player_score)
                    level_return = level2.run(player_score)

                    if level_return == "menu":
                        print("LEVEL2 Encerrado")
                        continue

                    elif level_return == "exit":
                        print("LEVEL2 Encerrado")
                        pygame.quit()
                        break

                    elif level_return:
                        if Score(self.window).save_score(menu_return, player_score) == "menu":
                            continue
                        else:
                            pygame.quit()
                            break

            elif menu_return == MENU_OPTION[3]:
                if Score(self.window).show() == "menu":
                    print("SCORE fechado")
                    continue
                else:
                    pygame.quit()
                    break

            else:
                print("Game encerrado")
                pygame.quit()
                break
