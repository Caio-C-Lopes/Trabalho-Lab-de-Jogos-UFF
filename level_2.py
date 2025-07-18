from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_2_5 import*
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

def jogar_2(coins, barra_per, dash_got):
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    # audio
    musica_level_before_loop = pygame.mixer.Sound("musica_level_before_loop2.ogg")
    musica_level_before_intro = pygame.mixer.Sound("musica_level_before_intro2.ogg")
    musica_level_before_intro.set_volume(0.3)
    musica_level_before_loop.set_volume(0.3)

    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("soul_sfx.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    item_sfx = pygame.mixer.Sound("item_sfx.wav")
    pygame.mixer.music.set_volume(0.23)
    item_sfx.set_volume(0.4)
    soul_sfx.set_volume(0.5)
    impacto.set_volume(0.5)
    hurt.set_volume(0.4)

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
    level2 = GameImage("fundo2_1.png")

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
    lista_de_tiros_inimigo = []
    colisao = 0

    health_box = Sprite("vida_box.png")

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

    # boneco no começo da fase
    if dash_got == True:
        boneco = Sprite("run_direita_boot.png", 4)
    else:
        boneco = Sprite("run_direita.png", 4)
    boneco.set_total_duration(1000)
    boneco.set_position(0, 210)
    boneco.x -= 300
    delay = 0
    quest = False

    # musica
    toca_musica = True
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    conta_loop = 0

    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(1)

    toca_dash = True
    run_toca_dash = False

    # alma
    soul = Sprite("soul.png", 8)
    soul.set_position((janela.width/2 - soul.width/2)+400, (janela.height/2 - soul.height/2)+60)
    soul.set_total_duration(1000)
    soul_object = Sprite("soul_object.png")
    soul_object.set_position(soul.x+90, soul.y+60)

    # alma vida
    vida = [Sprite("barra_cheia_blue.png"), Sprite("barra_1_blue.png"), Sprite("barra_2_blue.png"), Sprite("barra_3_blue.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = soul.x
    vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = soul.y
    barra_soul = 0

    # stars
    stars = Sprite("stars.png", 4)
    stars.set_total_duration(1000)
    stars.y += 280
    stars.x += 300

    stars_object = Sprite("stars_object.png")
    stars_object.set_position(stars.x+10, stars.y-30)
    stars_interagiu = 0

    estrela = 0

    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level2.draw()

        # musica
        while toca_musica == True and run_musica == True:
            musica_level_before_intro.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 745:
            toca_musica_loop = True

        while toca_musica_loop == True and run_musica_loop == True:
            musica_level_before_loop.play(loops=-1)
            run_musica_loop = False
            break

        # boneco aparecendo
        delay += dt
        if delay > 10:
            boneco.draw()
            boneco.update()
            if boneco.x < 55:
                boneco.x += 100 * janela.delta_time()
            else:
                boneco.pause()
                boneco.hide()
                quest = True

        if quest == True:
            # dinheiro
            bolso.draw()
            janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
            gema_verde_portrait.draw()
            vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = vida[7].x = soul.x+60
            vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = vida[7].y = soul.y+32

            # IA da alma
            if barra_soul <= 7:               
                vida[barra_soul].draw()
                soul.draw()
                soul.update()
                soul.y += vely * janela.delta_time()
                soul_object.set_position(soul.x+90, soul.y+60)

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
                if lista_de_tiros_inimigo != []:
                    for d in lista_de_tiros_inimigo:
                        d.draw()
                        d.update()
                        d.x -= 200 * janela.delta_time()
                        if d.collided(idle_object) and d in lista_de_tiros_inimigo:
                            hurt.play()
                            barra_p += 1
                            lista_de_tiros_inimigo.remove(d)

                if recarga_inimigo >= 1:
                    lista_de_tiros_inimigo = pew_esquerda_inimigo(soul, lista_de_tiros_inimigo)
                    recarga_inimigo = 0
            # proxima fase          
            else:
                # stars
                if stars_interagiu == 0:
                    stars.draw()
                    stars.update()
                    if idle_object.collided(stars_object):
                        janela.draw_text("Press I to Inspect", stars_object.x-68, stars_object.y-30, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                        janela.draw_text("Press I to Inspect", stars_object.x-65, stars_object.y-32, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                        if teclado.key_pressed("I"):
                            item_sfx.play()
                            stars_interagiu = 1
                            estrela += 1
                if idle.x >= janela.width - idle.width + 140:
                    janela.clear
                    jogar_2_5(coins, barra_p, dash_got, musica_level_before_loop, estrela)
                       
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

            if lista_de_tiros_esquerda == []:
                esquerda = False

            if lista_de_tiros_direita == []:
                direita = False

            recarga += janela.delta_time()

            # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
            if barra_p <= 3:
                vida_p[barra_p].draw()
            else:
                musica_level_before_intro.stop()
                musica_level_before_loop.stop()
                hurt.stop()
                while toca_risada == True and run_risada == True:
                    risada.play()
                    run_risada = False
                    break
                janela.delay(2000)
                game_over_screen()

        janela.update()

