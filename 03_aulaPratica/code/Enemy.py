import random

from .Entity import Entity
from .Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from .EnemyShot import EnemyShot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        # 1 Para ser escolhida uma direção logo no primeiro frame
        self.movement_delay = 1
        self.choice: str = "None"

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        self.movement_delay -= 1
        if self.movement_delay == 0:
            self.movement_delay = 60
            self.choice = random.choice(("up", "down"))

        if self.rect.top <= 0:
            self.rect.centery += ENTITY_SPEED[self.name]
            self.choice = "down"
            self.movement_delay = 60
        elif self.rect.bottom >= WIN_HEIGHT:
            self.rect.centery -= ENTITY_SPEED[self.name]
            self.choice = "up"
            self.movement_delay = 60
        elif self.choice == "up":
            self.rect.centery -= ENTITY_SPEED[self.name]
        elif self.choice == "down":
            self.rect.centery += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] + random.randint(0, 100)
            if self.name == "Enemy1":
                return EnemyShot(f"{self.name}Shot", (self.rect.left - 10, self.rect.centery))
            elif self.name == "Enemy2":
                return EnemyShot(f"{self.name}Shot", (self.rect.left, self.rect.centery))
