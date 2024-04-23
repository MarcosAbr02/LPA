import random

from .Background import Background
from .Const import WIN_WIDTH, WIN_HEIGHT
from .Enemy import Enemy
from .Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):  # Número de sprites que compões o Bg
                    list_bg.append(Background(f"Level1Bg{i}", position))
                    # Espelho
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg

            case "Level2Bg":
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f"Level2Bg{i}", position))
                    # Espelho
                    list_bg.append(Background(f"Level2Bg{i}", (WIN_WIDTH, 0)))
                return list_bg

            case "Player1":
                return Player("Player1", (10, WIN_HEIGHT / 2))

            case "Player2":
                return Player("Player2", (20, WIN_HEIGHT / 2 + 40))

            case "Enemy1":
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 39)))

            case "Enemy2":
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 45)))
