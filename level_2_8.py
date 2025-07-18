from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_2_9 import *
from tiros_functions3 import *

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

def jogar_2_8(coins, barra_per, dash_got, musica_level_before_loop, estrela):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("soul_sfx.wav")
    torre_sfx = pygame.mixer.Sound("torre_sfx.wav")
    item_sfx = pygame.mixer.Sound("item_sfx.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    coin = pygame.mixer.Sound("coin.wav")
    item_sfx.set_volume(0.5)
    soul_sfx.set_volume(0.5)
    torre_sfx.set_volume(0.5)
    impacto.set_volume(0.5)
    hurt.set_volume(0.4)
    coin.set_volume(0.4)

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
    level2_8 = GameImage("fundo2_8.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358
    limite_superior = HEIGHT + 5
    vely = 250

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0
    recarga_torre1 = 0
    recarga_torre2 = 0
    lista_de_tiros_inimigo_direita = []
    lista_de_tiros_inimigo_esquerda1 = []
    lista_de_tiros_inimigo_esquerda2 = []

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

    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(1)

    toca_dash = True
    run_toca_dash = False

    # alma
    soul = Sprite("soul_esquerda.png", 8)
    soul.set_position((janela.width/2 - soul.width/2)-400, (janela.height/2 - soul.height/2)+60)
    soul.set_total_duration(1000)
    soul_object = Sprite("soul_object.png")
    soul_object.set_position(soul.x+90, soul.y+60)

    # alma vida
    vida = [Sprite("barra_cheia_blue.png"), Sprite("barra_1_blue.png"), Sprite("barra_2_blue.png"), Sprite("barra_3_blue.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = soul.x
    vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = soul.y
    barra_soul = 0

    # torre 1
    torre1 = Sprite("torre.png", 11)
    torre1.set_position((janela.width/2 - torre1.width/2)+400, (janela.height/2 - torre1.height/2)-70)
    torre1.set_total_duration(1000)
    torre_object1 = Sprite("torre_object.png")
    torre_object1.set_position(torre1.x+45, torre1.y+80)

    # vida da torre 1
    vidat1 = [Sprite("barra_torre_cheia.png"), Sprite("barra_torre_1.png"), Sprite("barra_torre_2.png"), Sprite("barra_torre_3.png")]
    vidat1[0].x = vidat1[1].x = vidat1[2].x = vidat1[3].x = torre1.x
    vidat1[0].y = vidat1[1].y = vidat1[2].y = vidat1[3].y = torre1.y
    barra_torre1 = 0

    torre_vazia1 = Sprite("torre_vazia.png", 11)
    torre_vazia1.set_total_duration(1000)
    torre_vazia1.set_position(torre1.x, torre1.y)

    # torre 2
    torre2 = Sprite("torre.png", 11)
    torre2.set_position((janela.width/2 - torre2.width/2)+400, (janela.height/2 - torre2.height/2)+183)
    torre2.set_total_duration(1000)
    torre_object2 = Sprite("torre_object.png")
    torre_object2.set_position(torre2.x+45, torre2.y+80)

    # vida da torre 2
    vidat2 = [Sprite("barra_torre_cheia.png"), Sprite("barra_torre_1.png"), Sprite("barra_torre_2.png"), Sprite("barra_torre_3.png")]
    vidat2[0].x = vidat2[1].x = vidat2[2].x = vidat2[3].x = torre2.x
    vidat2[0].y = vidat2[1].y = vidat2[2].y = vidat2[3].y = torre2.y
    barra_torre2 = 0

    torre_vazia2 = Sprite("torre_vazia.png", 11)
    torre_vazia2.set_total_duration(1000)
    torre_vazia2.set_position(torre2.x, torre2.y)


    # stars
    stars = Sprite("stars.png", 4)
    stars.set_total_duration(1000)
    stars.y += 250
    stars.x += 800

    stars_object = Sprite("stars_object.png")
    stars_object.set_position(stars.x+10, stars.y-30)
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
        level2_8.draw()
        soul_object.set_position(soul.x+90, soul.y+60)

        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        soul.y += vely * janela.delta_time()

        if barra_torre1 <= 3:
            torre1.draw()
            torre1.update()
        else:
            torre_vazia1.set_curr_frame(5)
            torre_vazia1.draw()

        if barra_torre2 <= 3:
            torre2.draw()
            torre2.update()
        else:
            torre_vazia2.set_curr_frame(5)
            torre_vazia2.draw()

        # vida da alma
        vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = vida[7].x = soul.x+110
        vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = vida[7].y = soul.y+32

        # proxima fase     
        if barra_soul > 7 and barra_torre1 > 3 and barra_torre2 > 3:
            # stars
            if stars_interagiu == 0:
                stars.draw()
                stars.update()
                if idle_object.collided(stars_object):
                    janela.draw_text("Press I to Inspect", stars_object.x-90, stars_object.y-20, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press I to Inspect", stars_object.x-87, stars_object.y-22, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("I"):
                        item_sfx.play()
                        stars_interagiu = 1
                        star += 1
            if idle.x >= janela.width - idle.width + 140:
                jogar_2_9(coins, barra_p, dash_got, musica_level_before_loop, star)
        
        # vida das torres
        # torre 1
        if barra_torre1 < 3:
            vidat1[0].x = vidat1[1].x = vidat1[2].x = vidat1[3].x = torre1.x+34
            vidat1[0].y = vidat1[1].y = vidat1[2].y = vidat1[3].y = torre1.y+51

        # torre 2
        if barra_torre2 < 3:
            vidat2[0].x = vidat2[1].x = vidat2[2].x = vidat2[3].x = torre2.x+34
            vidat2[0].y = vidat2[1].y = vidat2[2].y = vidat2[3].y = torre2.y+51

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
                if barra_soul <= 7:
                    if d.collided(soul_object) and d in lista_de_tiros_direita:
                        if barra_soul == 7:
                            soul_sfx.play()
                        impacto.play()
                        barra_soul += 1
                        lista_de_tiros_direita.remove(d)
                
                if barra_torre1 <= 3:
                    if d.collided(torre_object1) and d in lista_de_tiros_direita:
                        if barra_torre1 == 3:
                            torre_sfx.play()
                        impacto.play()
                        barra_torre1 += 1
                        lista_de_tiros_direita.remove(d)
                
                if barra_torre2 <= 3:
                    if d.collided(torre_object2) and d in lista_de_tiros_direita:
                        if barra_torre2 == 3:
                            torre_sfx.play()
                        impacto.play()
                        barra_torre2 += 1
                        lista_de_tiros_direita.remove(d)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if barra_soul <= 7:
                    if d.collided(soul_object) and d in lista_de_tiros_esquerda:
                        if barra_soul == 7:
                            soul_sfx.play()
                        impacto.play()
                        barra_soul += 1
                        lista_de_tiros_esquerda.remove(d)
                
                if barra_torre1 <= 3:
                    if d.collided(torre_object1) and d in lista_de_tiros_esquerda:
                        if barra_torre1 == 3:
                            torre_sfx.play()
                        impacto.play()
                        barra_torre1 += 1
                        lista_de_tiros_esquerda.remove(d)

                if barra_torre2 <= 3:
                    if d.collided(torre_object2) and d in lista_de_tiros_esquerda:
                        if barra_torre2 == 3:
                            torre_sfx.play()
                        impacto.play()
                        barra_torre2 += 1
                        lista_de_tiros_esquerda.remove(d)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        recarga += janela.delta_time()

        # IA da alma
        if barra_soul <= 7:
            vida[barra_soul].draw()
            soul.draw()
            soul.update()

            recarga_inimigo += janela.delta_time()

            # limite superior
            if soul.y <= limite_superior:
                soul.y = limite_superior
                vely *= -1

            # limite inferior
            if soul.y >= janela.height - 210:
                soul.y = janela.height - 210
                vely *= -1

            # tiro da alma
            if lista_de_tiros_inimigo_direita != []:
                for d in lista_de_tiros_inimigo_direita:
                    d.draw()
                    d.update()
                    d.x += 200 * janela.delta_time()
                    if d.collided(idle_object) and d in lista_de_tiros_inimigo_direita:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_direita.remove(d)

            if recarga_inimigo >= 2:
                lista_de_tiros_inimigo_direita = pew_direita_alma(soul, lista_de_tiros_inimigo_direita)
                recarga_inimigo = 0
        
        # tiros da torre 1
        if barra_torre1 <= 3:
            recarga_torre1 += janela.delta_time()
            vidat1[barra_torre1].draw()

            if lista_de_tiros_inimigo_esquerda1 != []:
                for d in lista_de_tiros_inimigo_esquerda1:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    if d.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda1:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda1.remove(d)

            if recarga_torre1 >= 2:
                lista_de_tiros_inimigo_esquerda1 = pew_esquerda_inimigo(torre1, lista_de_tiros_inimigo_esquerda1)
                recarga_torre1 = 0
        
        # tiros da torre 2
        if barra_torre2 <= 3:
            recarga_torre2 += janela.delta_time()
            vidat2[barra_torre2].draw()

            if lista_de_tiros_inimigo_esquerda2 != []:
                for d in lista_de_tiros_inimigo_esquerda2:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    if d.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda2:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda2.remove(d)

            if recarga_torre2 >= 2:
                lista_de_tiros_inimigo_esquerda2 = pew_esquerda_inimigo(torre2, lista_de_tiros_inimigo_esquerda2)
                recarga_torre2 = 0        
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

