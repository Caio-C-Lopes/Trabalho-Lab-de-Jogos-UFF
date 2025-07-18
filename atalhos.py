from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_1 import *
import pygame
framerate = 60
pygame.init()

def toca_musica(musica):
    musica.play(loops=-1)

def para_musica(musica):
    musica.stop()

def reseta_musica(musica):
    musica.play(loops=-1)

menu_musica = pygame.mixer.Sound("loop_menu.wav")
toca_musica(menu_musica)


def menu():
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    barulhin_menu = pygame.mixer.Sound("barulhin_menu.wav")

    # fundo 0
    bg0_1 = GameImage("fundo0.png")
    bg0_2 = GameImage("fundo0.png")
    bg0_1.x = 0
    bg0_2.x = 1000
    bg0_roll_speed = 20

    # fundo 1
    bg1_1 = GameImage("fundo1_menu.png")
    bg1_2 = GameImage("fundo1_menu.png")
    bg1_1.x = 0
    bg1_2.x = 1000
    bg1_roll_speed = 40

    # fundo 2
    bg2_1 = GameImage("fundo2.png")
    bg2_2 = GameImage("fundo2.png")
    bg2_1.x = 0
    bg2_2.x = 1000
    bg2_roll_speed = 60

    # fundo 3
    bg3_1 = GameImage("fundo3.png")
    bg3_2 = GameImage("fundo3.png")
    bg3_1.x = 0
    bg3_2.x = 1000
    bg3_roll_speed = 80

    # fundo 4
    bg4_1 = GameImage("fundo4.png")
    bg4_2 = GameImage("fundo4.png")
    bg4_1.x = 0
    bg4_2.x = 1000
    bg4_roll_speed = 100

    # fundo 5
    bg5_1 = GameImage("fundo5.png")
    bg5_2 = GameImage("fundo5.png")
    bg5_1.x = 0
    bg5_2.x = 1000
    bg5_roll_speed = 130

    # titulo
    titulo = Sprite("title3.png")
    titulo.set_position((janela.width/2 - titulo.width/2)-10, (janela.height/2 - titulo.height/2) - 150)

    # normais#
    start_game = GameImage("start_game2.png")
    start_game.set_position(janela.width/2 - start_game.width/2, (janela.height/2 - start_game.height/2)+40)

    controles = GameImage("controles.png")
    controles.set_position(janela.width / 2 - controles.width / 2, (janela.height / 2 - controles.height / 2) + 115)

    quit = GameImage("quit.png")
    quit.set_position(janela.width / 2 - quit.width / 2, (janela.height / 2 - quit.height / 2) + 200)

    # selecionados#
    start_game_selecionado = GameImage("start_game_selecionado.png")
    start_game_selecionado.set_position(start_game.x, start_game.y)
    controles_selecionado = GameImage("controles_selecionado.png")
    controles_selecionado.set_position(controles.x, controles.y)
    quit_selecionado = GameImage("quit_selecionado.png")
    quit_selecionado.set_position(quit.x, quit.y)

    # maozinha
    hand = GameImage("maozinha.png")

    # inputs#
    mouse = Window.get_mouse()

    while True:
        # Parallax do fundo
        scrolling(bg0_1, bg0_2, bg0_roll_speed, janela)
        scrolling(bg1_1, bg1_2, bg1_roll_speed, janela)
        scrolling(bg2_1, bg2_2, bg2_roll_speed, janela)
        scrolling(bg3_1, bg3_2, bg3_roll_speed, janela)
        scrolling(bg4_1, bg4_2, bg4_roll_speed, janela)
        scrolling(bg5_1, bg5_2, bg5_roll_speed, janela)

        start_game.draw()
        controles.draw()
        quit.draw()

        # start game#
        if mouse.is_over_object(start_game):
            start_game_selecionado.draw()
            hand.set_position(start_game.x - 60, start_game.y)
            hand.draw()
            if mouse.is_button_pressed(1):
                para_musica(menu_musica)
                jogar()

        #controles#
        if mouse.is_over_area([395, 387], [568, 431]):
            controles_selecionado.draw()
            hand.set_position(controles.x-55, controles.y)
            hand.draw()
            if mouse.is_button_pressed(1):
                barulhin_menu.play()
                controles_screen()

        #quit#
        if mouse.is_over_area([420, 498], [533, 541]):
            quit_selecionado.draw()
            hand.set_position(quit.x+25, quit.y)
            hand.draw()
            if mouse.is_button_pressed(1):
                barulhin_menu.play()
                janela.close()

        titulo.draw()
        janela.update()

def scrolling(bg_atras, bg_frente, roll_speed, janela):
    # Atualiza as posições dos fundos
    bg_atras.x -= roll_speed * janela.delta_time()
    bg_frente.x -= roll_speed * janela.delta_time()

    # Verifica se um dos fundos saiu completamente da tela e reinicializa
    if bg_atras.x <= -bg_atras.width:
        bg_atras.x = bg_frente.x + bg_frente.width
    if bg_frente.x <= -bg_frente.width:
        bg_frente.x = bg_atras.x + bg_atras.width

    # Desenha os fundos
    bg_atras.draw()
    bg_frente.draw()

def controles_screen():
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    bg_controles = GameImage("credits_fundo.png")
    barulhin = pygame.mixer.Sound("Retro8.wav")
    barulhin_menu = pygame.mixer.Sound("barulhin_menu.wav")

    # inputs#
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    tutorial_1 = Sprite("tutorial_1.png")
    tutorial_1_selecionado = Sprite("tutorial_1_selecionado.png")
    tutorial_2_selecionado = Sprite("tutorial_2_selecionado.png")
    tutorial_2 = Sprite("tutorial_2.png")

    tutorial_1_object = GameImage("tutorial_1_object.png")
    tutorial_2_object = GameImage("tutorial_2_object.png")

    tutorial_1_object.set_position((janela.width/2 - tutorial_1_object.width/2)-24, (janela.height/2 - tutorial_1_object.height/2)+177)
    tutorial_2_object.set_position((janela.width/2 - tutorial_2_object.width/2)+5, (janela.height/2 - tutorial_2_object.height/2)+177)

    tutorial_2.x -= 30
    tutorial_1.x -= 30
    tutorial_1_selecionado.x -= 30
    tutorial_2_selecionado.x -= 30

    tutorial2 = False
    delay_tutorial = 0

    while True:
        janela.update()
        bg_controles.draw()
        tutorial_1.draw()

        delay_tutorial += janela.delta_time()

        if tutorial2 == False:
            if mouse.is_over_object(tutorial_1_object):
                tutorial_1_selecionado.draw()
                if delay_tutorial > 0.5 and mouse.is_button_pressed(1):
                    barulhin.play()
                    tutorial2 = True
                    delay_tutorial = 0

        if tutorial2 == True:
            tutorial_2.draw()
            if mouse.is_over_object(tutorial_2_object):
                tutorial_2_selecionado.draw()
                if delay_tutorial > 0.5 and mouse.is_button_pressed(1):
                    barulhin.play()
                    tutorial2 = False
                    delay_tutorial = 0

        if teclado.key_pressed("esc"):
            barulhin_menu.play()
            menu()