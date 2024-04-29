import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from .Const import COLOR, MENU_OPTION, EVENT_ENEMY, WIN_WIDTH, EVENT_TIMEOUT, WIN_HEIGHT
from .Enemy import Enemy
from .Entity import Entity
from .EntityFactory import EntityFactory
from .EntityMediator import EntityMediator
from .Player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.mode = menu_option  # modo de jogo

        # Criação de entidades
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(f"{self.name}Bg"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))

        # Recuperando Scores
        for ent in self.entity_list:
            if ent.name == "Player1":
                ent.score = player_score[0]
            elif ent.name == "Player2":
                ent.score = player_score[1]

        # Mensagem de Gamer Over
        self.game_over_txt = 240  # 4 segundos
        self.game_over = False

        # Spawn de inimigos
        if self.name == "Level1":
            if menu_option == MENU_OPTION[0]:  # Um jogador
                pygame.time.set_timer(EVENT_ENEMY, 2800)
            else:  # Dois jogadores
                pygame.time.set_timer(EVENT_ENEMY, 2000)
        elif self.name == "Level2":
            if menu_option == MENU_OPTION[0]:  # Um jogador
                pygame.time.set_timer(EVENT_ENEMY, 2500)
            else:  # Dois jogadores
                pygame.time.set_timer(EVENT_ENEMY, 1800)

        # Tempo de fase
        self.timeout = 60000
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # 100ms

        # Botão "i" para exibir informações
        self.info = False

    def run(self, player_score: list[int]):
        clock = pygame.time.Clock()

        print(f"{self.name} iniciado")

        # Configuração da música do level
        pygame.mixer.music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.set_volume(0.07)
        pygame.mixer_music.play(-1, fade_ms=5000)

        while True:
            # Execuções por segundo
            clock.tick(60)

            # DESENHAR ENTIDADES
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                # Exibir atributos do(s) player(s)
                if isinstance(ent, Player):
                    self.show_player_status(ent)

            # info na tela
            if self.info:
                self.show_level_info(clock)

            # Checa se houve derrota
            if self.game_over:
                self.show_centered_text(30, "GAME OVER", COLOR["WHITE"], ((WIN_WIDTH / 2), (WIN_HEIGHT / 2)))
                self.game_over_txt -= 1
                if self.game_over_txt == 0:
                    return "menu"
            else:
                if self.game_over_check():
                    self.game_over = True

            pygame.display.flip()

            # VERIFICAR INTERAÇÃO DE ENTIDADES
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # CHECA EVENTOS
            for event in pygame.event.get():

                # Evento de criação de inimigo
                choice = random.choice(("Enemy1", "Enemy2"))
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Evento de vitória
                if event.type == EVENT_TIMEOUT:
                    # Relógio para se todos os jogadores morrerem
                    if not self.game_over:
                        self.timeout -= 100
                    if self.timeout <= 0:
                        for ent in self.entity_list:
                            # Modificando lista do escopo de Game
                            if isinstance(ent, Player) and ent.name == "Player1":
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == "Player2":
                                player_score[1] = ent.score
                                break

                        print(f"{self.name} encerrado (TIME OUT)")
                        return True

                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    return 'exit'

                # Retorna ao menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        return "menu"

                    # Torna visível as informações na tela
                    if event.key == pygame.K_i:
                        if self.info:
                            self.info = False
                        else:
                            self.info = True

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

    def show_player_status(self, ent: Entity):
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

    def game_over_check(self):
        for ent in self.entity_list:
            if isinstance(ent, Player):
                return False
        return True

    def show_level_info(self, clock):
        if clock.get_fps() >= 60:
            self.show_left_text(10, f"fps: {clock.get_fps():.2f}", COLOR["YELLOW"], (20, 10))
        else:
            self.show_left_text(10, f"fps: {clock.get_fps():.2f}", COLOR["WHITE"], (20, 10))

        self.show_left_text(10, f"Entidades: {len(self.entity_list)}", COLOR["WHITE"], (20, 20))
        self.show_left_text(10, f"{self.name} - Timeout {self.timeout / 1000:.1f}s", COLOR["WHITE"], (20, 30))
