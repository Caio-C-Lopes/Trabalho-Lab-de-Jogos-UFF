from PPlay.window import *
from PPlay.sprite import *
import pygame
pygame.init()

def game_over_screen(musica_level_before_loop, hurt):
    framerate = 60
    last_time = time.time()
    from atalhos import reseta_musica
    from atalhos import menu_musica
    from atalhos import menu
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    musica_level_before_loop.stop()
    hurt.stop()

    game_over_intro = pygame.mixer.Sound("game_over_intro.ogg")
    game_over_intro.set_volume(0.3)
    game_over_loop = pygame.mixer.Sound("game_over_loop.ogg")
    game_over_loop.set_volume(0.3)

    game_over = Sprite("game_over.png")
    retry = Sprite("retry.png")
    retry.set_position(163, 360)
    return_to_title = Sprite("return_to_title.png")
    return_to_title.set_position(163, 443)
    retry_selecionado = Sprite("retry_selecionado.png")
    return_to_title_selecionado = Sprite("return_to_title_selecionado.png")

    toca_loop = True
    toca_loop_boolean = True

    retry_selecionado.set_position(retry.x, retry.y)
    return_to_title_selecionado.set_position(return_to_title.x, return_to_title.y)

    toca_intro = True
    toca_intro_boolean = True
    contador_loop = 0

    mouse = janela.get_mouse()

    delay = 0

    toca_risada = True
    run_risada = True
    risada = pygame.mixer.Sound("risada.wav")
    risada.set_volume(0.3)

    
    reset = True
    reset_boolean = True

    while True:

        janela.set_background_color("Black")

        while reset == True and reset_boolean == True:
            delay = 0
            reset_boolean = False
        
        if reset_boolean == False:
            dt = time.time() - last_time
            dt *= 60
            last_time = time.time()
            delay += dt

        print(delay)
        while toca_risada == True and run_risada == True:
            risada.play()
            run_risada = False
            break

        if dt > 6:
            while toca_intro == True and toca_intro_boolean == True:
                game_over_intro.play(0)
                toca_intro_boolean = False
                break

            game_over.draw()
            return_to_title.draw()

            contador_loop += janela.delta_time()

            if contador_loop >= 19:
                while toca_loop == True and toca_loop_boolean == True:
                    game_over_loop.play(loops=-1)
                    toca_loop_boolean = False
                    break

            if mouse.is_over_object(return_to_title):
                return_to_title_selecionado.draw()
                if mouse.is_button_pressed(1):
                    game_over_intro.stop()
                    game_over_loop.stop()
                    reseta_musica(menu_musica)
                    menu()

        janela.update()