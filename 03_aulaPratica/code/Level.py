import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from .Entity import Entity
from .EntityFactory import EntityFactory
from .Const import COLOR, MENU_OPTION


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

    def run(self):
        clock = pygame.time.Clock()

        print("Level iniciado")
        # Configuração da música do level
        pygame.mixer.music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.set_volume(0.07)
        pygame.mixer_music.play(-1, fade_ms=5000)

        while True:
            # Execuções por segundo
            clock.tick(60)

            # Desenhar entidades e fazê-las se mover
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # FPS na tela
            if clock.get_fps() >= 60:
                self.fps_text(20, f"fps: {clock.get_fps():.2f}", COLOR["YELLOW"], (10, 10))
            else:
                self.fps_text(20, f"fps:{clock.get_fps():.2f}", COLOR["WHITE"], (10, 10))
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

    def fps_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
