from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_3_5 import *
from tiros_functions4 import *

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

def jogar_3_1(coins, barra_per, dash_got, leve, pesado):
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    # audio
    musica_level_before_loop = pygame.mixer.Sound("musica_level_before_loop3.ogg")
    musica_level_before_intro = pygame.mixer.Sound("musica_level_before_intro3.ogg")
    musica_level_before_intro.set_volume(0.3)
    musica_level_before_loop.set_volume(0.3)

    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("zoio_bixo.wav")
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

    # gema azul portrait
    gema_azul_portrait = Sprite("gema_azul_icon.png")
    gema_azul_portrait.set_position((janela.width - gema_azul_portrait.width) - 92, 10)

    # levels#
    level3 = GameImage("fundo3_1.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358
    limite_superior = HEIGHT + 70
    vely = 280
    vely2 = 200

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0
    lista_de_tiros_inimigo = []
    lista_de_tiros_inimigo2 = []

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

    # demon_fly
    demon_fly = Sprite("demon_fly.png", 4)
    demon_fly.set_position((janela.width/2 - demon_fly.width/2)+300, (janela.height/2 - demon_fly.height/2)+60)
    demon_fly.set_total_duration(1000)
    demon_fly_object = Sprite("demon_fly_object.png")
    demon_fly_object.set_position(demon_fly.x+90, demon_fly.y+60)

    # demon fly vida
    vida = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = demon_fly.x
    vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = demon_fly.y
    barra_demon_fly = 0


    # demon_fly2
    demon_fly2 = Sprite("demon_fly.png", 4)
    demon_fly2.set_position((janela.width/2 - demon_fly2.width/2)+400, (janela.height/2 - demon_fly2.height/2)-50)
    demon_fly2.set_total_duration(1000)
    demon_fly2_object = Sprite("demon_fly_object.png")
    demon_fly2_object.set_position(demon_fly2.x+90, demon_fly2.y+60)

    # demon fly vida2
    vida2 = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = demon_fly2.x
    vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = demon_fly2.y
    barra_demon_fly2 = 0
    recarga_inimigo2 = 0
    

    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)


    # troca dos tiros
    tiro_tela = Sprite("tiro_tela.png")
    troca = 0

    normal_object = Sprite("normal_object.png")
    normal_object.set_position((janela.width/2-normal_object.width/2)+111, (janela.height/2-normal_object.height/2)-83)

    heavy_object = Sprite("normal_object.png")
    heavy_object.set_position(normal_object.x+1, normal_object.y+163)

    choose_light = Sprite("choose_light.png")
    choose_light.set_position((janela.width/2-choose_light.width/2)+111, (janela.height/2-choose_light.height/2)-84)

    choose_heavy = Sprite("choose_heavy.png")
    choose_heavy.set_position((janela.width/2-choose_heavy.width/2)+111, (janela.height/2-choose_heavy.height/2)+79)

    tiro_change_sfx = pygame.mixer.Sound("tiro_change_sfx.wav")
    tiro_change_sfx.set_volume(0.3)

    light = leve
    heavy = pesado
    mouse = janela.get_mouse()

    tela_tiro_sfx = pygame.mixer.Sound("tela_tiro_sfx.wav")
    tela_tiro_sfx.set_volume(0.6)
    toca_troca = False
    run_toca = True
    
    # dragao
    dragon = Sprite("dragon.png", 3)
    dragon.set_total_duration(800)
    dragon.set_position((janela.width/2 - dragon.width/2)+300, (janela.height/2 - dragon.height/2)+70)

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level3.draw()

        # musica
        while toca_musica == True and run_musica == True:
            musica_level_before_intro.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 410:
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
            gema_azul_portrait.draw()
            janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
            gema_verde_portrait.draw()
            # vida do demon_fly
            vida[0].x = vida[1].x = vida[2].x = vida[3].x = vida[4].x = vida[5].x = vida[6].x = vida[7].x = demon_fly.x+7
            vida[0].y = vida[1].y = vida[2].y = vida[3].y = vida[4].y = vida[5].y = vida[6].y = vida[7].y = demon_fly.y-15

            # IA do demon_fly (da frente)
            if barra_demon_fly <= 7:               
                vida[barra_demon_fly].draw()
                demon_fly.draw()
                demon_fly.update()
                demon_fly.y += vely * janela.delta_time()
                demon_fly_object.set_position(demon_fly.x+15, demon_fly.y+10)

                recarga_inimigo += janela.delta_time()

                # limite superior
                if demon_fly.y <= limite_superior:
                    demon_fly.y = limite_superior
                    vely *= -1

                # limite inferior
                if demon_fly.y >= janela.height - 130:
                    demon_fly.y = janela.height - 130
                    vely *= -1

                # tiro do demon_fly
                if lista_de_tiros_inimigo != []:
                    for d in lista_de_tiros_inimigo:
                        d.draw()
                        d.update()
                        d.x -= 200 * janela.delta_time()
                        if d.collided(idle_object) and d in lista_de_tiros_inimigo:
                            hurt.play()
                            barra_p += 1
                            lista_de_tiros_inimigo.remove(d)

                if recarga_inimigo >= 0.7:
                    lista_de_tiros_inimigo = pew_esquerda_inimigo(demon_fly, lista_de_tiros_inimigo)
                    recarga_inimigo = 0

            # vida do demon_fly2 (de tras)
            vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = vida2[7].x = demon_fly2.x+7
            vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = vida2[7].y =demon_fly2.y-15
            # IA do demon_fly2
            if barra_demon_fly2 <= 7:               
                vida2[barra_demon_fly2].draw()
                demon_fly2.draw()
                demon_fly2.update()
                demon_fly2.y += vely2 * janela.delta_time()
                demon_fly2_object.set_position(demon_fly2.x+15, demon_fly2.y+10)

                recarga_inimigo2 += janela.delta_time()

                # limite superior
                if demon_fly2.y <= limite_superior:
                    demon_fly2.y = limite_superior
                    vely2 *= -1

                # limite inferior
                if demon_fly2.y >= janela.height - 130:
                    demon_fly2.y = janela.height - 130
                    vely2 *= -1

                # tiro do demon_fly
                if lista_de_tiros_inimigo2 != []:
                    for d in lista_de_tiros_inimigo2:
                        d.draw()
                        d.update()
                        d.x -= 200 * janela.delta_time()
                        if d.collided(idle_object) and d in lista_de_tiros_inimigo2:
                            hurt.play()
                            barra_p += 1
                            lista_de_tiros_inimigo2.remove(d)

                if recarga_inimigo2 >= 1.5:
                    lista_de_tiros_inimigo2 = pew_esquerda_inimigo2(demon_fly2, lista_de_tiros_inimigo2)
                    recarga_inimigo2 = 0

            # proxima fase          
            else:
                if idle.x >= janela.width - idle.width + 140:
                    jogar_3_5(coins, barra_p, dash_got, light, heavy, musica_level_before_loop)
                       
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
            if teclado.key_pressed("space"):
                if light == 1 and heavy == 0 and recarga >= 1:
                    if virado_direita:
                        direita = True
                        lista_de_tiros_direita = pew_direita(idle, lista_de_tiros_direita, light, heavy)
                        recarga = 0

                    if virado_esquerda:
                        esquerda = True
                        lista_de_tiros_esquerda = pew_esquerda(idle, lista_de_tiros_esquerda, light, heavy)
                        recarga = 0
                
                if heavy == 1 and light == 0 and recarga >= 3:
                    if virado_direita:
                        direita = True
                        lista_de_tiros_direita = pew_direita(idle, lista_de_tiros_direita, light, heavy)
                        recarga = 0

                    if virado_esquerda:
                        esquerda = True
                        lista_de_tiros_esquerda = pew_esquerda(idle, lista_de_tiros_esquerda, light, heavy)
                        recarga = 0

            # tiro normal do personagem
            if lista_de_tiros_direita != [] and direita: # direita
                for d in lista_de_tiros_direita:
                    d.draw()
                    d.update()
                    d.x += 200 * janela.delta_time()
                    if barra_demon_fly <= 7:
                        if d.collided(demon_fly_object) and d in lista_de_tiros_direita:
                            if barra_demon_fly == 7:
                                soul_sfx.play()
                            impacto.play()
                            if light == 1 and heavy == 0:
                                barra_demon_fly += 1
                            elif light == 0 and heavy == 1:
                                barra_demon_fly += 2
                            lista_de_tiros_direita.remove(d)

                    if barra_demon_fly2 <= 7:
                        if d.collided(demon_fly2_object) and d in lista_de_tiros_direita:
                            if barra_demon_fly2 == 7:
                                soul_sfx.play()
                            impacto.play()
                            if light == 1 and heavy == 0:
                                barra_demon_fly2 += 1
                            elif light == 0 and heavy == 1:
                                barra_demon_fly2 += 2
                            lista_de_tiros_direita.remove(d)

            if lista_de_tiros_esquerda != [] and esquerda: #esquerda
                for d in lista_de_tiros_esquerda:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    if barra_demon_fly <= 7:
                        if d.collided(demon_fly_object) and d in lista_de_tiros_esquerda:
                            if barra_demon_fly == 7:
                                soul_sfx.play()
                            impacto.play()
                            if light == 1 and heavy == 0:
                                barra_demon_fly += 1
                            elif light == 0 and heavy == 1:
                                barra_demon_fly += 2
                            lista_de_tiros_esquerda.remove(d)

                    if barra_demon_fly2 <= 7:
                        if d.collided(demon_fly2_object) and d in lista_de_tiros_esquerda:
                            if barra_demon_fly2 == 7:
                                soul_sfx.play()
                            impacto.play()
                            if light == 1 and heavy == 0:
                                barra_demon_fly2 += 1
                            elif light == 0 and heavy == 1:
                                barra_demon_fly2 += 2
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

            # troca dos tiros
            if barra_demon_fly > 7 and barra_demon_fly2 > 7: # somente se todos os inimigos estiverem derrotados

                if teclado.key_pressed("R"):
                    troca = 1
                    toca_troca = True

                if troca == 1:
                    tiro_tela.draw()

                    if teclado.key_pressed("ESC"):
                        troca = 0
                        toca_troca = False
                        run_toca = True
                        tela_tiro_sfx.play()
                                        
                    if mouse.is_over_object(normal_object):
                        choose_light.draw()
                        if mouse.is_button_pressed(1):
                            tiro_change_sfx.play()
                            toca_troca = False
                            run_toca = True
                            troca = 0
                            light = 1
                            heavy = 0
                        
                    if mouse.is_over_object(heavy_object):
                        choose_heavy.draw()
                        if mouse.is_button_pressed(1):
                            tiro_change_sfx.play()
                            toca_troca = False
                            run_toca = True
                            troca = 0
                            light = 0
                            heavy = 1
        
                while toca_troca == True and run_toca == True :
                    tela_tiro_sfx.play()
                    run_toca = False
                    break
        janela.update()
