import pygame.key

from .Entity import Entity
from .Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEYS


class Player(Entity):
    def __init__(self, name: str, position: tuple, ):
        super().__init__(name, position)

    def move(self):
        # Movimentação da nave
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEYS[self.name]["UP"]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEYS[self.name]["DOWN"]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEYS[self.name]["RIGHT"]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEYS[self.name]["LEFT"]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
