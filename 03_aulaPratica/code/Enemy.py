import random

from .Const import ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from .EnemyShot import EnemyShot
from .Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Atirar um pouco após entrar em tela
        self.shot_delay = 10
        # 1 Para ser escolhida uma direção logo no primeiro frame
        self.movement_delay = 1
        self.choice: str = "None"

    def move(self):
        self.rect.centerx -= self.speed

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        self.movement_delay -= 1

        # Nave encostou na parte superior da tela
        if self.rect.top <= 0:
            self.rect.centery += self.speed
            self.choice = "down"
            self.movement_delay = 60

        # Nave encostou na parte inferior da tela
        elif self.rect.bottom >= WIN_HEIGHT:
            self.rect.centery -= self.speed
            self.choice = "up"
            self.movement_delay = 60

        # Delay chegou a 0
        elif self.movement_delay == 0:
            # Recarrega o delay
            self.movement_delay = 60
            self.choice = random.choice(("up", "down"))

        # Continua se movendo enquanto a escolha não for alterada
        if self.choice == "up":
            self.rect.centery -= self.speed

        else:
            self.rect.centery += self.speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] + random.randint(0, 30)
            if self.name == "Enemy1":
                return EnemyShot(f"{self.name}Shot", (self.rect.left - 10, self.rect.centery))
            elif self.name == "Enemy2":
                return EnemyShot(f"{self.name}Shot", (self.rect.left, self.rect.centery))
