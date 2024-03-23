import pygame as pg
from pygame import Surface, Rect

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

# Inicializar o Módulo do PyGame
pg.init()

print("setup start")
# Criação de janela do pygame
window: Surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surface: Surface = pg.image.load('./asset/bg.png').convert_alpha()
player1_surf: Surface = pg.image.load('./asset/player1.png').convert_alpha()

# Obter retângulo das superfícies
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar na janela
window.blit(source=bg_surface, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pg.display.flip()

# Colocar um relógio no nosso jogo
clock = pg.time.Clock()

# Carregar som
pg.mixer_music.load("./asset/fase1.mp3")
pg.mixer_music.set_volume(0.1)
pg.mixer_music.play(-1, fade_ms=5000)

print("setup end")
# Loop de funcionamento do jogo
print("loop start")
running = True
while running:
    # Esse loop vai acontecer x vezes por segundo
    clock.tick(140)
    # print(f'{clock.get_fps():.0f}')

    # Atualização dos elementos na tela após cada loop
    window.blit(source=bg_surface, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pg.display.flip()

    # Evento para fechar a janela do pygame
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Movimentação do jogador
    pressed_key = pg.key.get_pressed()
    if pressed_key[pg.K_w]:
        player1_rect.centery -= 2
    if pressed_key[pg.K_s]:
        player1_rect.centery += 2
    pressed_key = pg.key.get_pressed()
    if pressed_key[pg.K_a]:
        player1_rect.centerx -= 2
    pressed_key = pg.key.get_pressed()
    if pressed_key[pg.K_d]:
        player1_rect.centerx += 2

print("loop end")
pg.quit()
