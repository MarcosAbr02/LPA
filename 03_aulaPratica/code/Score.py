from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from .Const import COLOR, SCORE_POS, MENU_OPTION
from .DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect: Rect = self.surf.get_rect(left=0, top=0)
        self.window.blit(source=self.surf, dest=self.rect)
        self.name = ""

        pygame.mixer.music.load("./asset/Score.mp3")
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1, fade_ms=5000)

    def save_score(self, menu_option: str, player_score: list[int]):
        print("SAVE SCORE iniciado")

        db_proxy = DBProxy('DBScore')
        text = ""
        score = 0
        name = self.name

        if menu_option == MENU_OPTION[0]:  # 1 Player
            score = player_score[0]
            text = "Player 1 enter with your name (4 caracteres):"

        elif menu_option == MENU_OPTION[1]:  # 2 Players Cooperativo
            score = (player_score[0] + player_score[1]) / 2
            text = "Enter with team's name (4 caracteres):"

        elif menu_option == MENU_OPTION[2]:  # 2 Players Competitivo
            if player_score[0] >= player_score[1]:
                score = player_score[0]
                text = "Player 1 enter with your name (4 caracteres):"
            else:
                score = player_score[1]
                text = "Player 2 enter with your name (4 caracteres)"

        while True:
            # É necessário redesenhar o background
            self.window.blit(source=self.surf, dest=self.rect)

            self.show_centered_text(50, "YOU WIN!", COLOR["YELLOW"], SCORE_POS["TITLE"])
            self.show_centered_text(20, text, COLOR["WHITE"], SCORE_POS["ENTER_NAME"])
            self.show_centered_text(20, name, COLOR["WHITE"], SCORE_POS["NAME"])
            pygame.display.flip()

            # CHECA EVENTOS
            for event in pygame.event.get():
                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    return

                # Se alguma tecla for pressionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        return "menu"

                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({"name": name, "score": score, 'date': self.get_formatted_date()})
                        db_proxy.close()
                        return self.show()

                    elif event.key == pygame.K_BACKSPACE:
                        if len(name) > 0:  # Verifica se há caracteres para excluir
                            name = name[:-1]  # Remove o último caractere do nome

                    elif event.unicode.isalnum() and len(name) < 4:
                        name += event.unicode  # Adiciona o caractere ao nome

    def show(self):
        print("SCORE iniciado")

        # É necessário redesenhar o background
        self.window.blit(source=self.surf, dest=self.rect)

        self.show_centered_text(30, "TOP 10 SCORES", COLOR["YELLOW"], SCORE_POS["TITLE"])
        self.show_centered_text(30, "NAME      SCORE       DATE   ", COLOR["ORANGE"],
                                SCORE_POS["LABEL"])

        # Acessando banco
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            code, name, score, date = player_score
            self.show_centered_text(20, f' {name}            {score:05d}       {date}', COLOR["WHITE"],
                                    SCORE_POS[list_score.index(player_score)])

        pygame.display.flip()

        while True:

            # CHECA EVENTOS
            for event in pygame.event.get():
                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    return None

                # Se alguma tecla for pressionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        return "menu"

    def show_centered_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Nesta função a orientação do texto é centralizada. O que pode não ser a melhor das escolhas em alguns casos
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    @staticmethod
    def get_formatted_date():
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")
        current_date = current_datetime.strftime("%d/%m/%y")
        return f"{current_date} - {current_time}"
