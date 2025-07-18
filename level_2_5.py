from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_2_8 import *
from tiros_functions2 import *

# Função para tocar a música em loop
def play_loop_music():
    pygame.mixer.music.play(-1)  # -1 indica loop infinito

def game_over_screen():
    from atalhos import menu
    from atalhos import reseta_musica
    from atalhos import menu_musica
    janela = Window(950, 594)
    janela.set_title("Before I Die")

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

    while True:
        janela.set_background_color("Black")

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

def jogar_2_5(coins, barra_per, dash_got, musica_level_before_loop, estrela):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    impacto = pygame.mixer.Sound("impact.wav")
    item_sfx = pygame.mixer.Sound("item_sfx.wav")
    golem_sfx = pygame.mixer.Sound("golem_sfx.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    coin = pygame.mixer.Sound("coin.wav")
    heal = pygame.mixer.Sound("heal.wav")
    golem_sfx.set_volume(0.5)
    impacto.set_volume(0.5)
    item_sfx.set_volume(0.4)
    hurt.set_volume(0.4)
    coin.set_volume(0.4)
    heal.set_volume(0.4)

    # personagem
    # movimentação
    # declarando e posicionando o personagem
    if dash_got == True:
        idle = Sprite("idle_direita_boot.png", 4)
    else:
        idle = Sprite("idle_direita.png", 4)
    idle.set_position((janela.width/2 - idle.width/2)-232,(janela.height/2 - idle.height/2)+101)

    # "máscara" para fazer as colisões do personagem ou dos monstros
    idle_object = Sprite("object.png")
    idle_object.set_position(idle.x, idle.y)

    # parado pra direita
    if dash_got == True:
        idle_direita = Sprite("idle_direita_boot.png", 4)
    else:
        idle_direita = Sprite("idle_direita.png", 4)
    idle_direita.set_total_duration(1000)

    # parado pra esquerda
    if dash_got == True:
        idle_esquerda = Sprite("idle_esquerda_boot.png", 4)
    else:
        idle_esquerda = Sprite("idle_esquerda.png", 4)
    idle_esquerda.set_total_duration(1000)

    # andando pra direita
    if dash_got == True:
        run_direita = Sprite("run_direita_boot.png", 4)
    else:
        run_direita = Sprite("run_direita.png", 4)
    run_direita.set_total_duration(1000)

    # andando pra esquerda
    if dash_got == True:
        run_esquerda = Sprite("run_esquerda_boot.png", 4)
    else:
        run_esquerda = Sprite("run_esquerda.png", 4)
    run_esquerda.set_total_duration(1000)

    # portrait
    portrait = Sprite("player.png")
    portrait.x += 8
    portrait.y += 4

    # vida
    vida_p = [Sprite("barra_cheia_p.png"), Sprite("barra_1p.png"), Sprite("barra_2p.png"), Sprite("barra_3p.png")]
    vida_p[0].x = vida_p[1].x = vida_p[2].x = vida_p[3].x = portrait.x + 105
    vida_p[0].y = vida_p[1].y = vida_p[2].y = vida_p[3].y = portrait.y + 23
    barra_p = barra_per
    # levels#
    level2_5 = GameImage("fundo2_5.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    colisao1 = 0
    colisao2 = 0

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)
    vel_per = 3
    last_time = time.time()

    toca_risada = True
    run_risada = True
    risada = pygame.mixer.Sound("risada.wav")
    risada.set_volume(0.3)

    # dash
    dash = False

    delay_dash = 0
    dash_recarga = 100

    dash_sheet = Sprite("dash_sheet.png", 5)
    dash_sheet.set_total_duration(2200)
    dash_sheet.set_position((janela.width/2 - dash_sheet.width/2)-410, (janela.height/2 - dash_sheet.height/2)-150)

    # dash sfx
    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(1)

    toca_dash = True
    run_toca_dash = False

    # golem 1 (na frente)
    # andando pra direita
    golem_direita1 = Sprite("golem_direita.png", 10)
    golem_direita1.set_total_duration(1000)
    golem_direita1.set_position((janela.width/2 - golem_direita1.width/2)+400, (janela.height/2 - golem_direita1.height/2)+50)

    # andando pra esquerda
    golem_esquerda1 = Sprite("golem_esquerda.png", 10)
    golem_esquerda_backup1 = Sprite("golem_esquerda.png", 10)
    golem_esquerda_backup1.set_total_duration(1000)
    golem_esquerda1.set_position(golem_direita1.x, golem_direita1.y)
    golem_esquerda1.set_total_duration(1000)

    # vida do golem 1 (começa na esquerda)
    vida1 = [Sprite("barra_cheia_blue.png"), Sprite("barra_1_blue.png"), Sprite("barra_2_blue.png"), Sprite("barra_3_blue.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = vida1[4].x = vida1[5].x = vida1[6].x = golem_esquerda1.x
    vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = vida1[4].y = vida1[5].y = vida1[6].y = golem_esquerda1.y
    barra_golem1 = 0

    # golem 2 (atrás)
    # andando pra direita
    golem_direita2 = Sprite("golem_direita.png", 10)
    golem_direita2.set_total_duration(1000)
    golem_direita2.set_position((janela.width/2 - golem_direita2.width/2)-400, (janela.height/2 - golem_direita2.height/2)+50)

    # andando pra esquerda
    golem_esquerda2 = Sprite("golem_esquerda.png", 10)
    golem_direita_backup2 = Sprite("golem_direita.png", 10)
    golem_direita_backup2.set_total_duration(1000)
    golem_esquerda2.set_position(golem_direita2.x, golem_direita2.y)
    golem_esquerda2.set_total_duration(1000)

    # vida do golem 2
    vida2 = [Sprite("barra_cheia_blue.png"), Sprite("barra_1_blue.png"), Sprite("barra_2_blue.png"), Sprite("barra_3_blue.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = golem_esquerda2.x
    vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = golem_esquerda2.y
    barra_golem2 = 0

    # máscaras dos golens
    golem_object1 = Sprite("golem_object.png")
    golem_object1.set_position(golem_esquerda1.x+110, golem_esquerda1.y+120)

    golem_object2 = Sprite("golem_object.png")
    golem_object2.set_position(golem_esquerda2.x+110, golem_esquerda2.y+120)

    # reset golem 
    reset_golem1 = 0
    reset_golem2 = 0

    # morte
    morreu_golem1 = 0
    morreu_golem2 = 0

    # golem 1 laranja
    # andando pra direita
    golem_direita_laranja1 = Sprite("golem_direita_laranja.png", 10)
    golem_direita_laranja1.set_total_duration(1000)
    golem_direita_laranja1.set_position((janela.width/2 - golem_direita_laranja1.width/2)+400, (janela.height/2 - golem_direita_laranja1.height/2)+50)

    # andando pra esquerda
    golem_esquerda_laranja1 = Sprite("golem_esquerda_laranja.png", 10)
    golem_esquerda_laranja_backup1 = Sprite("golem_esquerda_laranja.png", 10)
    golem_esquerda_laranja_backup1.set_total_duration(1000)
    golem_esquerda_laranja1.set_position(golem_direita1.x, golem_direita1.y)
    golem_esquerda_laranja1.set_total_duration(1000)

    # golem 2 laranja
    # andando pra direita
    golem_direita_laranja2 = Sprite("golem_direita_laranja.png", 10)
    golem_direita_laranja2.set_total_duration(1000)
    golem_direita_laranja2.set_position((janela.width/2 - golem_direita2.width/2)-400, (janela.height/2 - golem_direita2.height/2)+50)

    # andando pra esquerda
    golem_esquerda_laranja2 = Sprite("golem_esquerda_laranja.png", 10)
    golem_direita_laranja_backup2 = Sprite("golem_direita_laranja.png", 10)
    golem_direita_laranja_backup2.set_total_duration(1000)
    golem_esquerda_laranja2.set_position(golem_direita2.x, golem_direita2.y)
    golem_esquerda_laranja2.set_total_duration(1000)

    # vida golem 2 laranja
    vida_laranja2 = [Sprite("barra_cheia_laranja.png"), Sprite("barra_1_laranja.png"), Sprite("barra_2_laranja.png"), Sprite("barra_3_laranja.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_laranja2[0].x = vida_laranja2[1].x = vida_laranja2[2].x = vida_laranja2[3].x = vida_laranja2[4].x = vida_laranja2[5].x = vida_laranja2[6].x = golem_esquerda2.x
    vida_laranja2[0].y = vida_laranja2[1].y = vida_laranja2[2].y = vida_laranja2[3].y = vida_laranja2[4].y = vida_laranja2[5].y = vida_laranja2[6].y = golem_esquerda2.y
   
    # vida golem 1 laranja
    vida_laranja1 = [Sprite("barra_cheia_laranja.png"), Sprite("barra_1_laranja.png"), Sprite("barra_2_laranja.png"), Sprite("barra_3_laranja.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_laranja1[0].x = vida_laranja1[1].x = vida_laranja1[2].x = vida_laranja1[3].x = vida_laranja1[4].x = vida_laranja1[5].x = vida_laranja1[6].x = golem_esquerda1.x
    vida_laranja1[0].y = vida_laranja1[1].y = vida_laranja1[2].y = vida_laranja1[3].y = vida_laranja1[4].y = vida_laranja1[5].y = vida_laranja1[6].y = golem_esquerda1.y

    # stars
    stars = Sprite("stars.png", 4)
    stars.set_total_duration(1000)
    stars.y += 550
    stars.x += 820

    stars_object = Sprite("stars_object.png")
    stars_object.set_position(830, 555)
    stars_interagiu = 0

    star = estrela
    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)
    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level2_5.draw()
        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        # proxima fase
        if morreu_golem1 == 5 and morreu_golem2 == 5:
            # stars
            if stars_interagiu == 0:
                stars.draw()
                stars.update()
                if idle_object.collided(stars_object):
                    janela.draw_text("Press I to Inspect", stars_object.x-80, stars_object.y-62, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press I to Inspect", stars_object.x-77, stars_object.y-64, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("I"):
                        item_sfx.play()
                        stars_interagiu = 1
                        star += 1
            if idle.x >= janela.width - idle.width + 140:
                jogar_2_8(coins, barra_p, dash_got, musica_level_before_loop, star)
        
        # vida do golem 1
        if reset_golem1 == 0:
            vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = vida1[4].x = vida1[5].x = vida1[6].x = vida1[7].x = golem_esquerda1.x+98
            vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = vida1[4].y = vida1[5].y = vida1[6].y = vida1[7].y = golem_esquerda1.y+68
    
            vida_laranja1[0].x = vida_laranja1[1].x = vida_laranja1[2].x = vida_laranja1[3].x = vida_laranja1[4].x = vida_laranja1[5].x = vida_laranja1[6].x = vida_laranja1[7].x = golem_esquerda1.x+98
            vida_laranja1[0].y = vida_laranja1[1].y = vida_laranja1[2].y = vida_laranja1[3].y = vida_laranja1[4].y = vida_laranja1[5].y = vida_laranja1[6].y = vida_laranja1[7].y = golem_esquerda1.y+68


        elif reset_golem1 == 1:
            vida_laranja1[0].x = vida_laranja1[1].x = vida_laranja1[2].x = vida_laranja1[3].x = vida_laranja1[4].x = vida_laranja1[5].x = vida_laranja1[6].x = vida_laranja1[7].x = golem_esquerda_laranja1.x+98
            vida_laranja1[0].y = vida_laranja1[1].y = vida_laranja1[2].y = vida_laranja1[3].y = vida_laranja1[4].y = vida_laranja1[5].y = vida_laranja1[6].y = vida_laranja1[7].y = golem_esquerda_laranja1.y+68

        # vida do golem 2
        if reset_golem2 == 0:
            vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = vida2[7].x = golem_direita2.x+98
            vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = vida2[7].y = golem_direita2.y+68

            vida_laranja2[0].x = vida_laranja2[1].x = vida_laranja2[2].x = vida_laranja2[3].x = vida_laranja2[4].x = vida_laranja2[5].x = vida_laranja2[6].x = vida_laranja2[7].x = golem_direita2.x+98
            vida_laranja2[0].y = vida_laranja2[1].y = vida_laranja2[2].y = vida_laranja2[3].y = vida_laranja2[4].y = vida_laranja2[5].y = vida_laranja2[6].y = vida_laranja2[7].y = golem_direita2.y+68

        elif reset_golem2 == 1:
            vida_laranja2[0].x = vida_laranja2[1].x = vida_laranja2[2].x = vida_laranja2[3].x = vida_laranja2[4].x = vida_laranja2[5].x = vida_laranja2[6].x = vida_laranja2[7].x = golem_direita_laranja2.x+98
            vida_laranja2[0].y = vida_laranja2[1].y = vida_laranja2[2].y = vida_laranja2[3].y = vida_laranja2[4].y = vida_laranja2[5].y = vida_laranja2[6].y = vida_laranja2[7].y = golem_direita_laranja2.y+68

        # golens laranjas

        if reset_golem1 == 1: # golem1 laranja
            golem_direita1.hide()
            golem_esquerda1.hide()
            golem_direita_laranja1.x = golem_esquerda_laranja1.x
            golem_direita_laranja1.y = golem_esquerda_laranja1.y
        
        if reset_golem2 == 1: # golem2 laranja
            golem_direita2.hide()
            golem_esquerda2.hide()
            golem_esquerda_laranja2.x = golem_direita_laranja2.x
            golem_esquerda_laranja2.y = golem_direita_laranja2.y
 
        if reset_golem1 == 0: # golem azul

            # copiando posição
            golem_direita_laranja1.set_position(golem_direita1.x, golem_direita1.y)
            golem_esquerda_laranja1.set_position(golem_direita_laranja1.x, golem_direita_laranja1.y)


            # copiando os frames
            golem_direita_laranja1.set_curr_frame(golem_direita1.get_curr_frame())

        if reset_golem2 == 0: # golem azul

            # copiando posição
            golem_esquerda_laranja2.set_position(golem_esquerda2.x, golem_esquerda2.y)
            golem_direita_laranja2.set_position(golem_esquerda_laranja2.x, golem_esquerda_laranja2.y)


            # copiando os frames
            golem_direita_laranja2.set_curr_frame(golem_direita2.get_curr_frame())            

        # golens normais
        golem_direita1.x = golem_esquerda1.x
        golem_direita1.y = golem_esquerda1.y

        golem_esquerda2.x = golem_direita2.x
        golem_esquerda2.y = golem_direita2.y

        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

        idle.draw()
        run_direita.update()
        run_esquerda.update()
        idle_direita.update()
        idle_esquerda.update()

        if dash_got == True:
            dash_recarga += dt
            # dash
            if teclado.key_pressed("LEFT_SHIFT") and dash_recarga >= 100:
                dash = True
                dash_recarga = 0
                run_toca_dash = True
        
            while toca_dash == True and run_toca_dash == True:
                dash_sfx.play(0)
                run_toca_dash = False
                break
            
            if dash == True:
                delay_dash += dt
                vel_per = 8
                if delay_dash > 25:
                    delay_dash = 0
                    vel_per = 3
                    dash = False

            if dash_recarga < 100:
                dash_sheet.draw()
                dash_sheet.update()
            else:
                dash_sheet.set_curr_frame(4)
                dash_sheet.draw() 

        # portrait do personagem
        portrait.draw()

        # movimentação do player
        # esquerda
        if teclado.key_pressed("A"):
            moving = True
            virado_direita = False
            virado_esquerda = True

        # direita
        if teclado.key_pressed("D"):
            moving = True
            virado_direita = True
            virado_esquerda = False

        if moving == True:

            # andar para direita
            if teclado.key_pressed("D") and idle.x <= 720:
                idle = run_direita
                idle.x += vel_per * dt

            # andar para esquerda
            if teclado.key_pressed("A") and idle.x >= -150:
                idle = run_esquerda
                idle.x -= vel_per * dt

        # andar para cima virado para direita
        if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_direita:
            idle = run_direita
            idle.y -= vel_per * dt

        # andar para cima virado para esquerda
        if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_esquerda:
            idle = run_esquerda
            idle.y -= vel_per * dt

        # andar para baixo virado para direita
        if teclado.key_pressed("S") and idle.y <= WIDTH and virado_direita:
            idle = run_direita
            idle.y += vel_per * dt

        # andar para baixo virado para esquerda
        if teclado.key_pressed("S") and idle.y <= WIDTH and virado_esquerda:
            idle = run_esquerda
            idle.y += vel_per * dt

        # ficar parado virado para direita
        if not teclado.key_pressed("D") and not teclado.key_pressed("A") and virado_direita:
            idle = idle_direita

            # andar para cima virado para direita
            if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_direita:
                idle = run_direita
                idle.y -= vel_per * dt

            # andar para baixo virado para direita
            if teclado.key_pressed("S") and idle.y <= WIDTH and virado_direita:
                idle = run_direita
                idle.y += vel_per * dt

            moving = False

        # ficar parado virado para esquerda
        if not teclado.key_pressed("D") and not teclado.key_pressed("A") and virado_esquerda:
            idle = idle_esquerda

            # andar para cima virado para esquerda
            if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_esquerda:
                idle = run_esquerda
                idle.y -= vel_per * dt

            # andar para baixo virado para esquerda
            if teclado.key_pressed("S") and idle.y <= WIDTH and virado_esquerda:
                idle = run_esquerda
                idle.y += vel_per * dt

            moving = False

        idle_object.set_position(idle.x + 160, idle.y + 140)

        # tiro normal
        if teclado.key_pressed("space") and recarga >= 1:
            if virado_direita:
                direita = True
                lista_de_tiros_direita = pew_direita(idle, lista_de_tiros_direita)
                recarga = 0

            if virado_esquerda:
                esquerda = True
                lista_de_tiros_esquerda = pew_esquerda(idle, lista_de_tiros_esquerda)
                recarga = 0
        # tiro normal do personagem
        if lista_de_tiros_direita != [] and direita: # direita
            for d in lista_de_tiros_direita:
                d.draw()
                d.update()
                d.x += 200 * janela.delta_time()
                if barra_golem1 <= 7:
                    if d.collided(golem_object1) and d in lista_de_tiros_direita:
                        if barra_golem1 == 7 and reset_golem1 == 0:
                            golem_sfx.play()
                            if reset_golem1 == 0:
                                barra_golem1 = -2
                                reset_golem1 = 1
                        if barra_golem1 == 6 and reset_golem1 == 1:
                            golem_sfx.play()
                        impacto.play()
                        if reset_golem1 == 0:
                            barra_golem1 += 1
                        elif reset_golem1 == 1:
                            morreu_golem1 += 1
                            barra_golem1 += 2
                        lista_de_tiros_direita.remove(d)

                if barra_golem2 <=7:
                    if d.collided(golem_object2) and d in lista_de_tiros_direita:
                        if barra_golem2 == 7:
                            golem_sfx.play()
                            if reset_golem2 == 0:
                                barra_golem2 = -2
                                reset_golem2 = 1
                        if barra_golem2 == 6 and reset_golem2 == 1:
                            golem_sfx.play()                       
                        impacto.play()
                        if reset_golem2 == 0:                           
                            barra_golem2 += 1
                        elif reset_golem2 == 1:
                            morreu_golem2 += 1
                            barra_golem2 += 2
                        lista_de_tiros_direita.remove(d)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if barra_golem1 <= 7:
                    if d.collided(golem_object1) and d in lista_de_tiros_esquerda:
                        if barra_golem1 == 7:
                            golem_sfx.play()
                            if reset_golem1 == 0:
                                barra_golem1 = -2
                                reset_golem1 = 1
                        if barra_golem1 == 6 and reset_golem1 == 1:
                            golem_sfx.play()                                        
                        impacto.play()
                        if reset_golem1 == 0:
                            barra_golem1 += 1
                        elif reset_golem1 == 1:
                            morreu_golem1 += 1
                            barra_golem1 += 2
                        lista_de_tiros_esquerda.remove(d)
                
                if barra_golem2 <= 7:
                    if d.collided(golem_object2) and d in lista_de_tiros_esquerda:
                        if barra_golem2 == 7:
                            golem_sfx.play()
                            if reset_golem2 == 0:
                                barra_golem2 = -2
                                reset_golem2 = 1
                        if barra_golem2 == 6 and reset_golem2 == 1:
                            golem_sfx.play()                                
                        impacto.play()
                        if reset_golem2 == 0:                           
                            barra_golem2 += 1
                        elif reset_golem2 == 1:
                            morreu_golem2 += 1
                            barra_golem2 += 2
                        lista_de_tiros_esquerda.remove(d)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        recarga += janela.delta_time()
        # IA do golem 1 (frente)
        if barra_golem1 <= 7:
            if reset_golem1 == 0:
                vida1[barra_golem1].draw()
                golem_esquerda1.draw()
                golem_esquerda1.update()
                golem_direita1.update()
                golem_esquerda_backup1.x = golem_esquerda1.x
                golem_esquerda_backup1.y = golem_esquerda1.y
                golem_object1.set_position(golem_esquerda1.x+110, golem_esquerda1.y+120)

            elif reset_golem1 == 1:
                vida_laranja1[barra_golem1].draw()
                golem_esquerda_laranja1.draw()
                golem_esquerda_laranja1.update()
                golem_direita_laranja1.update()
                golem_esquerda_laranja_backup1.x = golem_esquerda_laranja1.x
                golem_esquerda_laranja_backup1.y = golem_esquerda_laranja1.y
                golem_object1.set_position(golem_esquerda_laranja1.x+110, golem_esquerda_laranja1.y+120)
            
            # deixar o golem sempre virado pro personagem
            if idle_object.x > golem_object1.x and idle_object.x - golem_object1.x > 10:
                if reset_golem1 == 0:
                    golem_esquerda1 = golem_direita1
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1 = golem_direita_laranja1
                    
            if idle_object.x < golem_object1.x and golem_object1.x - idle_object.x > 10:
                if reset_golem1 == 0:
                    golem_esquerda1 = golem_esquerda_backup1
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1 = golem_esquerda_laranja_backup1

            # perseguição do golem pelo personagem
            # eixo x
            if idle_object.x < golem_object1.x:
                if reset_golem1 == 0:
                    golem_esquerda1.x -= 0.5 * dt
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1.x -= 0.7 * dt

            elif idle_object.x > golem_object1.x:
                if reset_golem1 == 0:
                    golem_esquerda1.x += 0.5 * dt
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1.x += 0.7 * dt

            # eixo y
            if idle_object.y < golem_object1.y:
                if reset_golem1 == 0:
                    golem_esquerda1.y -= 0.5 * dt
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1.y -= 0.7 * dt
            
            elif idle_object.y > golem_object1.y:
                if reset_golem1 == 0:
                    golem_esquerda1.y += 0.5 * dt
                elif reset_golem1 == 1:
                    golem_esquerda_laranja1.y += 0.7 * dt
            
            # colisão do golem  com o personagem
            while colisao1 == 0:
                if golem_object1.collided(idle_object):
                    hurt.play()
                    if reset_golem1 == 0:
                        barra_p += 2
                    elif reset_golem1 == 1:
                        barra_p += 1
                    morreu_golem1 = 5
                    colisao1 = 1
                    barra_golem1 = 8
                break

        # IA do golem 2 (atrás)
        if barra_golem2 <= 7:
            if reset_golem2 == 0:
                vida2[barra_golem2].draw()
                golem_direita2.draw()
                golem_direita2.update()
                golem_esquerda2.update()
                golem_direita_backup2.x = golem_direita2.x
                golem_direita_backup2.y = golem_direita2.y
                golem_object2.set_position(golem_direita2.x+110, golem_direita2.y+120)
            
            elif reset_golem2 == 1:
                vida_laranja2[barra_golem2].draw()
                golem_direita_laranja2.draw()
                golem_direita_laranja2.update()
                golem_esquerda_laranja2.update()
                golem_direita_laranja_backup2.x = golem_direita_laranja2.x
                golem_direita_laranja_backup2.y = golem_direita_laranja2.y
                golem_object2.set_position(golem_direita_laranja2.x+110, golem_direita_laranja2.y+120)
            
            # deixar o golem sempre virado pro personagem
            if idle_object.x > golem_object2.x and idle_object.x - golem_object2.x > 10:
                if reset_golem2 == 0:
                    golem_direita2 = golem_direita_backup2
                elif reset_golem2 == 1:
                    golem_direita_laranja2 = golem_direita_laranja_backup2

            if idle_object.x < golem_object2.x and golem_object2.x - idle_object.x > 10:
                if reset_golem2 == 0:
                    golem_direita2 = golem_esquerda2
                if reset_golem2 == 1:
                    golem_direita_laranja2 = golem_esquerda_laranja2

            # perseguição do golem pelo personagem
            # eixo x
            if idle_object.x < golem_object2.x:
                if reset_golem2 == 0:
                    golem_direita2.x -= 0.7 * dt
                elif reset_golem2 == 1:
                    golem_direita_laranja2.x -= 0.7 * dt
                
            elif idle_object.x > golem_object2.x:
                if reset_golem2 == 0:
                    golem_direita2.x += 0.7 * dt
                elif reset_golem2 == 1:
                    golem_direita_laranja2.x += 0.7 * dt

            # eixo y
            if idle_object.y < golem_object2.y:
                if reset_golem2 == 0:
                    golem_direita2.y -= 0.7 * dt
                if reset_golem2 == 1:
                    golem_direita_laranja2.y -= 0.7 * dt

            elif idle_object.y > golem_object2.y:
                if reset_golem2 == 0:
                    golem_direita2.y += 0.7 * dt
                elif reset_golem2 == 1:
                    golem_direita_laranja2.y += 0.7 * dt

            # colisão do golem 2 com o personagem
            while colisao2 == 0:
                if golem_object2.collided(idle_object):
                    hurt.play()
                    if reset_golem2 == 0:
                        barra_p += 2
                    elif reset_golem2 == 1:
                        barra_p += 1
                    morreu_golem2 = 5
                    colisao2 = 1
                    barra_golem2 = 8
                break
        gema_verde_portrait.draw()
        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3:
            vida_p[barra_p].draw()
        else:
            musica_level_before_loop.stop()
            hurt.stop()
            while toca_risada == True and run_risada == True:
                risada.play()
                run_risada = False
                break
            janela.delay(2000)
            game_over_screen()

        janela.update()

