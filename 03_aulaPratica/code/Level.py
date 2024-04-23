import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from .Const import COLOR, MENU_OPTION, EVENT_ENEMY, WIN_WIDTH, WIN_HEIGHT, EVENT_TIMEOUT
from .Enemy import Enemy
from .Entity import Entity
from .EntityFactory import EntityFactory
from .EntityMediator import EntityMediator
from .Player import Player


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
        pygame.time.set_timer(EVENT_TIMEOUT, 30000)  # 30 Segundos

    def run(self):
        clock = pygame.time.Clock()

        print("Level iniciado")
        # Configuração da música do level
        pygame.mixer.music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.set_volume(0.07)
        pygame.mixer_music.play(-1, fade_ms=5000)

        speed = 60  # fps
        text_frames = 0
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

                # Exibir atributo health do(s) player(s)
                if isinstance(ent, Player):
                    self.show_status(ent)

            # FPS na tela
            self.show_fps(clock)

            # Turbo Mode
            text_frames = self.turbo_mode_text(text_frames, speed)

            pygame.display.flip()

            # VERIFICAR INTERAÇÃO DE ENTIDADES
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # CHECA EVENTOS
            for event in pygame.event.get():
                choice = random.choice(("Enemy1", "Enemy2"))
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    return True

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
                            text_frames = 240
                            speed = 120
                        else:
                            print("Turbo mode: OFF")
                            text_frames = 120
                            speed = 60

    def show_centered_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Nesta função a orientação do texto é centralizada. O que pode não ser a melhor das escolhas em alguns casos
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def show_left_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Nesta a orientação é à esquerda do texto
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def show_status(self, ent: Entity):
        position = 10
        if ent.name == "Player2":
            position = 20
        # Desenhar vida e pontuação na tela
        if ent.health == 300:
            color = COLOR["CYAN"]
        elif 300 > ent.health >= 200:
            color = COLOR["GREEN"]
        elif 200 > ent.health >= 100:
            color = COLOR["YELLOW"]
        else:
            color = COLOR["ORANGE"]

        self.show_left_text(10, f"{ent.name}: {ent.health} | Score: {ent.score}", color, ((WIN_WIDTH - 170), position))

    def show_fps(self, clock):
        if clock.get_fps() >= 60:
            self.show_left_text(10, f"fps: {clock.get_fps():.2f}", COLOR["YELLOW"], (20, 10))
        else:
            self.show_left_text(10, f"fps: {clock.get_fps():.2f}", COLOR["WHITE"], (20, 10))

        self.show_left_text(10, f"Entidades: {len(self.entity_list)}", COLOR["WHITE"], (20, 20))

    def turbo_mode_text(self, frames: int, speed: int):
        if frames > 0:
            if speed == 120:
                self.show_centered_text(20, "TURBO MODE: ON", COLOR["YELLOW"], ((WIN_WIDTH / 2), WIN_HEIGHT - 30))
            elif speed == 60:
                self.show_centered_text(20, "TURBO MODE: OFF", COLOR["WHITE"], ((WIN_WIDTH / 2), WIN_HEIGHT - 30))
            return frames - 1
        else:
            return 0
