import pygame
from pygame import Surface, Rect
from pygame.font import Font
from .Const import WIN_WIDTH


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

        running = True
        while running:

            # Exibir surface de background
            self.window.blit(source=self.surf, dest=self.rect)

            # Exibir textos do menu
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", (255, 128, 0), ((WIN_WIDTH / 2), 120))
            pygame.display.flip()

            # Verificar se o jogo foi fechado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Menu encerrado")

    # Configurações do texto do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
