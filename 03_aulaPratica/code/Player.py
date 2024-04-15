import pygame.key

from .Entity import Entity
from .Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEYS, ENTITY_SHOT_DELAY
from .PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple, ):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

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

    def shoot(self):
        # Delay de tiro
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEYS[self.name]["SHOOT"]]:
                print(f"Disparo por {self.name}")
                if self.name == "Player1":
                    return PlayerShot(f"{self.name}Shot", (self.rect.centerx, self.rect.centery))
                elif self.name == "Player2":
                    return PlayerShot(f"{self.name}Shot", (self.rect.right, self.rect.centery-6))
