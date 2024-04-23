from .Const import WIN_WIDTH
from .Enemy import Enemy
from .EnemyShot import EnemyShot
from .Entity import Entity
from .Player import Player
from .PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list) - 1):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list) - 1):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        # Considerar interações válidas
        valid_interaction = False

        if (isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)) or \
                (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)):
            valid_interaction = True
        elif (isinstance(ent1, Player) and isinstance(ent2, EnemyShot)) or \
                (isinstance(ent1, EnemyShot) and isinstance(ent2, Player)):
            valid_interaction = True

        if valid_interaction:
            if ent1.rect.right >= ent2.rect.left and \
                    ent1.rect.left <= ent2.rect.right and \
                    ent1.rect.bottom >= ent2.rect.top and \
                    ent1.rect.top <= ent2.rect.bottom:
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)

    @staticmethod
    def __give_score(enemy, entity_list: list[Entity]):
        if enemy.last_dmg == "Player1Shot":
            for ent in entity_list:
                if ent.name == "Player1":
                    ent.score += enemy.score

        elif enemy.last_dmg == "Player2Shot":
            for ent in entity_list:
                if ent.name == "Player2":
                    ent.score += enemy.score
