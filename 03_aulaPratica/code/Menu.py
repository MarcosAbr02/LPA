import pygame
from pygame import Surface, Rect
from pygame.font import Font
from .Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        print("Menu iniciado")

        # Configuração da música do menu
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1, fade_ms=5000)

        menu_option = 0
        running = True
        while running:

            # Exibir surface de background
            self.window.blit(source=self.surf, dest=self.rect)

            # Exibir textos do menu
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # Exibir opções do Menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()

            # Checa todos os eventos
            for event in pygame.event.get():
                # Verificar se o jogo foi fechado
                if event.type == pygame.QUIT:
                    print("Janela Fechada")
                    running = False

                # Se alguma tecla for pressionada
                if event.type == pygame.KEYDOWN:
                    # Se for s ou seta para baixo
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    # Se for w ou seta para cima
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    # Se for enter
                    if event.key == pygame.K_RETURN:
                        print("Opção selecionada: " + MENU_OPTION[menu_option])
                        # Parando música do menu
                        pygame.mixer.music.stop()
                        return MENU_OPTION[menu_option]

                    if event.key == pygame.K_ESCAPE:
                        print("Esc pressionado")
                        running = False

    # Configurações do texto do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
