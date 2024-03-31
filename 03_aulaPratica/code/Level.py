import pygame.display
from pygame import Surface

from .Entity import Entity
from .EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        print("Level iniciado")
        # Configuração da música do level
        pygame.mixer.music.load('./asset/Level1.mp3')
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1, fade_ms=5000)

        running = True
        while running:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()

            # Checa todos os eventos
            for event in pygame.event.get():
                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    return 'exit'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        return 'menu'
