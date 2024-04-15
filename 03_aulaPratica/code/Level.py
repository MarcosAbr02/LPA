import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from .Entity import Entity
from .EntityFactory import EntityFactory
from .Const import COLOR, MENU_OPTION, EVENT_ENEMY, WIN_WIDTH, WIN_HEIGHT
from .EntityMediator import EntityMediator
from .Player import Player
from .Enemy import Enemy


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))

        pygame.time.set_timer(EVENT_ENEMY, 3000)

    def run(self):
        clock = pygame.time.Clock()

        print("Level iniciado")
        # Configuração da música do level
        pygame.mixer.music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.set_volume(0.07)
        pygame.mixer_music.play(-1, fade_ms=5000)

        speed = 60
        show_text_frames = 0
        while True:
            # Execuções por segundo
            clock.tick(speed)

            # DESENHAR ENTIDADES
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            # FPS na tela
            if clock.get_fps() >= 60:
                self.fps_text(10, f"fps: {clock.get_fps():.2f}", COLOR["YELLOW"], (10, 10))
            else:
                self.fps_text(10, f"fps: {clock.get_fps():.2f}", COLOR["WHITE"], (10, 10))

            self.fps_text(10, f"Entidades: {len(self.entity_list)}", COLOR["WHITE"], (10, 20))

            # TEXTO DO TURBO MODE
            if show_text_frames > 0:
                if speed == 120:
                    self.show_text(20, "TURBO MODE: ON", COLOR["YELLOW"], ((WIN_WIDTH / 2), WIN_HEIGHT - 30))
                    show_text_frames -= 1
                elif speed == 60:
                    self.show_text(20, "TURBO MODE: OFF", COLOR["WHITE"], ((WIN_WIDTH / 2), WIN_HEIGHT - 30))
                    show_text_frames -= 1
            pygame.display.flip()

            # VERIFICAR INTERAÇÃO DE ENTIDADES
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # CHECA EVENTOS
            for event in pygame.event.get():
                choice = random.choice(("Enemy1", "Enemy2"))
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    return 'exit'

                # Retorna ao menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        return 'menu'

                    if event.key == pygame.K_t:
                        if speed == 60:
                            print("Turbo mode: ON")
                            show_text_frames = 240
                            speed = 120
                        else:
                            print("Turbo mode: OFF")
                            show_text_frames = 120
                            speed = 60

    def fps_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def show_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
