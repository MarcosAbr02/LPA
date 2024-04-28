import pygame
from pygame import Surface, Rect
from pygame.font import Font
from .DBProxy import DBProxy

from .Const import COLOR, SCORE_POS, MENU_OPTION


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect: Rect = self.surf.get_rect(left=0, top=0)
        self.window.blit(source=self.surf, dest=self.rect)

    def save_score(self, menu_option: str, player_score: list[int]):
        db_proxy = DBProxy('DBScore')

        if menu_option == MENU_OPTION[0]:
            score = player_score[0]
            text = "Player 1 enter with your name (4 caracteres):"

        elif menu_option == MENU_OPTION[1]:
            score = (player_score[0] + player_score[1])/2
            text = "Enter with team's name (4 caracteres)"

        elif menu_option == MENU_OPTION[2]:
            if player_score[0] >= player_score[1]:
                score = player_score[0]
                text = "Player 1 enter with your name (4 caracteres)"
            else:
                score = player_score[1]
                text = "Player 2 enter with your name (4 caracteres)"
        return self.show()

    def show(self):
        print("SCORE iniciado")

        pygame.mixer.music.load("./asset/Score.mp3")
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1, fade_ms=5000)

        # Exibir surface de background

        while True:

            self.show_centered_text(30, "SCORES", COLOR["YELLOW"], SCORE_POS["TITLE"])
            pygame.display.flip()

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
