from .Const import WIN_WIDTH
from .Enemy import Enemy
from .EnemyShot import EnemyShot
from .Entity import Entity
from .PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right <= 0:
                print(f"Entidade {ent.name} destruída por colisão de tela")
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                print(f"Entidade {ent.name} destruída por colisão de tela")
                ent.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
