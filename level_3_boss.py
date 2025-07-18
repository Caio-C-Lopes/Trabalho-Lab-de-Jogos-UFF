from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from tiros_functions5 import *

# Função para tocar a música em loop
def play_loop_music():
    pygame.mixer.music.play(-1)  # -1 indica loop infinito

def fim_screen():
    from atalhos import menu
    from atalhos import reseta_musica
    from atalhos import menu_musica
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    fundo = Sprite("branco.png")
    red_eye = Sprite("red_eye.png", 24)
    red_eye.set_total_duration(5200)
    red_eye.set_position((janela.width/2 - red_eye.width/2),(janela.height/2 - red_eye.height/2))
    red_eye.set_loop(False)
    return_nor = Sprite("fundo_final.png")
    return_selec = Sprite("fundo_final_selec.png")
    timer_eye = 0
    return_object = Sprite("object_final.png")
    return_object.set_position((janela.width/2 - return_object.width/2)-270,(janela.height/2 - return_object.height/2)+260)
    mouse = janela.get_mouse()
    para = 0

    while True:
        fundo.draw()
        red_eye.draw()
        red_eye.update()

        if red_eye.curr_frame == 11:
            para = 1

        if para == 1:
            red_eye.pause()
            timer_eye += janela.delta_time()
        
        if timer_eye > 6:
            red_eye.play()
        
        if timer_eye > 9:
            return_nor.draw()
            if mouse.is_over_object(return_object):
                return_selec.draw()
                if mouse.is_button_pressed(1):
                    reseta_musica(menu_musica)
                    menu()
        
        janela.update()

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

def jogar_3_boss(barra_per, dash_got, leve, pesado, musica):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    musica.stop()

    # audio
    musica_level_before_loop_dragon = pygame.mixer.Sound("musica_level_before_loop_dragon.ogg")
    musica_level_before_intro_dragon= pygame.mixer.Sound("musica_level_before_intro_dragon.ogg")
    musica_level_before_intro_dragon.set_volume(0.3)
    musica_level_before_loop_dragon.set_volume(0.3)

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

    # gema azul portrait
    gema_azul_portrait = Sprite("gema_azul_icon.png")
    gema_azul_portrait.set_position((janela.width - gema_azul_portrait.width) - 92, 10)

    # levels#
    level3_boss = GameImage("fundo3_boss.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 135
    WIDTH = 358

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    lista_de_tiros_inimigo = []
    lista_de_tiros_inimigo_esquerda1 = []
    lista_de_tiros_inimigo_esquerda2 = []

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

    gem_sfx = pygame.mixer.Sound("gem_sfx.wav")
    gem_sfx.set_volume(0.5)


    toca_dash = True
    run_toca_dash = False


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

    # gema final
    gema_final = False

    delay_gema_final = 0
    gema_final_recarga = 1000

    gema_final_sheet = Sprite("gema_final_sheet.png", 5)
    gema_final_sheet.set_total_duration(2200)
    gema_final_sheet.set_position((janela.width/2 - gema_final_sheet.width/2)-340, (janela.height/2 - gema_final_sheet.height/2)-150)

    toca_gema_final = True
    run_toca_gema_final = False

    # dragao
    dragon = Sprite("dragon.png", 3)
    dragon.set_total_duration(800)
    dragon.set_position((janela.width/2 - dragon.width/2)+340, (janela.height/2 - dragon.height/2)+70)
    recarga_dragon = 0

    # vida do mecha boss
    boss_vida = []
    for i in range(20):
        vida = Sprite(f"boss_vida_fase3_{i}.png")
        vida.set_position((janela.width/2 - vida.width/2), (janela.height/2 - vida.height/2)-150)
        boss_vida.append(vida)
    barra_dragon = 0
    barra_dragon_cont = 0

    # obeliscos
    obelisco1 = Sprite("obelisk_fly.png", 13)
    obelisco1.set_total_duration(1000)
    obelisco1.set_position((janela.width/2 - obelisco1.width/2)+380, (janela.height/2 - obelisco1.height/2)-70)

    # vida obelisco 1
    vida = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png")]
    vida[0].x = vida[1].x = vida[2].x = vida[3].x = obelisco1.x + 53
    vida[0].y = vida[1].y = vida[2].y = vida[3].y = obelisco1.y + 38
    barra_obelisco1 = 0
    barra_obelisco1_cont = 0

    obelisco2 = Sprite("obelisk_fly.png", 13)
    obelisco2.set_total_duration(1000)
    obelisco2.set_position((janela.width/2 - obelisco2.width/2)+380, (janela.height/2 - obelisco2.height/2)+100)

    # vida obelisco 2
    vida2 = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png")]
    vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = obelisco2.x + 53
    vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = obelisco2.y + 60
    barra_obelisco2 = 0
    barra_obelisco2_cont = 0

    dragon_object = Sprite("dragon_object.png")
    dragon_object.set_position(dragon.x+30, dragon.y+124)

    obelisco1_object = Sprite("obelisk_object.png")
    obelisco2_object = Sprite("obelisk_object.png")
    obelisco1_object.set_position(obelisco1.x+75, obelisco1.y+260)
    obelisco2_object.set_position(obelisco2.x+75, obelisco2.y+290)

    recarga_obelisco1 = 0
    recarga_obelisco2 = 0

    shield = Sprite("dragon_shield.png", 15)
    shield.set_total_duration(1000)
    shield.set_position(dragon.x-120, dragon.y+10)

    shield_timer = 0
    shield_delay = False

    shield_object = Sprite("shield_object.png")
    shield_object.set_position(dragon.x-80, dragon.y+110)

    tiro_obelisk_object1 = Sprite("tiro_obelisk_object.png")
    tiro_obelisk_object2 = Sprite("tiro_obelisk_object.png")
    tiro_dragon_object = Sprite("tiro_dragon_object.png")
    timer = 0

    reset_1 = 0
    reset_2 = 0

    final = 0
    timerzinho = 0

    # explosion
    puff = Sprite("puff.png", 59)
    puff.set_loop(False)
    puff.set_total_duration(1500)
    puff.set_position((janela.width/2 - puff.width/2)+300, (janela.height/2 - puff.height/2)+60)

    kaboom = Sprite("kaboom.png", 60)
    kaboom.set_loop(False)
    kaboom.set_total_duration(1500)
    kaboom.set_position((janela.width/2 - kaboom.width/2)+345, (janela.height/2 - kaboom.height/2)+40)

    explosao = 0
    explosao_delay = 0
    finish = pygame.mixer.Sound("finish.wav")
    explosion = pygame.mixer.Sound("explosion.wav")
    explosion.set_volume(0.6)
    finish.set_volume(0.6)
    toca_delay = 0
    toca_finish = True
    run = True
    explosao_boolean = True
    toca_explosao = False

    # orb
    orb = Sprite("orb_final.png", 20)
    orb.set_total_duration(1000)
    orb.set_position((janela.width - orb.width) - 60, (janela.height / 2 - orb.height / 2) + 110)

    orb_object = Sprite("orb_object.png")
    orb_object.set_position(orb.x + 60, orb.y + 50)

    acabou = 0
    pretin = Sprite("pretin.png")
    frase_fim = Sprite("text_fim.png")
    frase_fim2 = Sprite("text_fim2.png")
    frase_timer = 0
    fim = 0

    dragon_voice = pygame.mixer.Sound("dragon_voice.wav")
    dragon_voice.set_volume(2)
    toca_voice = True
    run_voice = True

    # musica
    toca_musica = True
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    conta_loop = 0

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level3_boss.draw()

        # musica
        while toca_musica == True and run_musica == True:
            musica_level_before_intro_dragon.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 696:
            toca_musica_loop = True

        while toca_musica_loop == True and run_musica_loop == True:
            musica_level_before_loop_dragon.play(loops=-1)
            run_musica_loop = False
            break

        # gema final
        gema_final_recarga += dt
        gema_final_sheet.draw()
        if teclado.key_pressed("J") and gema_final_recarga >= 1000:
            gema_final = True
            gema_final_recarga = 0
            run_toca_gema_final = True
            shield_delay = True
    
        while toca_gema_final == True and run_toca_gema_final == True:
            gem_sfx.play(0)
            run_toca_gema_final = False
            break
        
        if gema_final == True:
            delay_gema_final += dt
            if delay_gema_final > 25:
                delay_gema_final = 0
                gema_final = False

        if gema_final_recarga < 250 and gema_final_recarga:
            gema_final_sheet.set_curr_frame(0)
        
        elif gema_final_recarga > 250 and gema_final_recarga < 500:
            gema_final_sheet.set_curr_frame(1)

        elif gema_final_recarga > 500 and gema_final_recarga < 750:
            gema_final_sheet.set_curr_frame(2)
        
        elif gema_final_recarga > 750 and gema_final_recarga < 1000:
            gema_final_sheet.set_curr_frame(3)
            
        else:
            gema_final_sheet.set_curr_frame(4)

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
            if barra_dragon <= 19:
                if teclado.key_pressed("D") and idle.x <= 400:
                    idle = run_direita
                    idle.x += vel_per * dt
            else:
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
                if barra_dragon <= 19 and shield_delay == True:
                    if d.collided(dragon_object) and d in lista_de_tiros_direita:
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_dragon_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_dragon_cont += 2
                        lista_de_tiros_direita.remove(d)

                if shield_delay == False:     
                    if d.collided(shield_object) and d in lista_de_tiros_direita:
                        impacto.play()
                        lista_de_tiros_direita.remove(d)
                
                if barra_obelisco1 <= 3:
                    if d.collided(obelisco1_object) and d in lista_de_tiros_direita:
                        if barra_obelisco1 == 3 and light == 1 and heavy == 0 and barra_obelisco1_cont == 1:
                            soul_sfx.play()
                        elif barra_obelisco1 == 3 and light == 0 and heavy == 1:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_obelisco1_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_obelisco1_cont += 2
                        lista_de_tiros_direita.remove(d)

                if barra_obelisco2 <= 3:
                    if d.collided(obelisco2_object) and d in lista_de_tiros_direita:
                        if barra_obelisco2 == 3 and light == 1 and heavy == 0 and barra_obelisco2_cont == 1:
                            soul_sfx.play()
                        elif barra_obelisco2 == 3 and light == 0 and heavy == 1:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_obelisco2_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_obelisco2_cont += 2
                        lista_de_tiros_direita.remove(d)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if barra_dragon <= 19:
                    if d.collided(dragon_object) and d in lista_de_tiros_esquerda:
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_dragon_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_dragon_cont += 2
                        lista_de_tiros_esquerda.remove(d)

                if barra_obelisco1 <= 3:
                    if d.collided(obelisco1_object) and d in lista_de_tiros_esquerda:
                        if barra_obelisco1 == 3 and light == 1 and heavy == 0 and barra_obelisco1_cont == 1:
                            soul_sfx.play()
                        elif barra_obelisco1 == 3 and light == 0 and heavy == 1:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_obelisco1_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_obelisco1_cont += 2
                        lista_de_tiros_esquerda.remove(d)

                if barra_obelisco2 <= 3:
                    if d.collided(obelisco2_object) and d in lista_de_tiros_esquerda:
                        if barra_obelisco2 == 3 and light == 1 and heavy == 0 and barra_obelisco2_cont == 1:
                            soul_sfx.play()
                        elif barra_obelisco2 == 3 and light == 0 and heavy == 1:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_obelisco2_cont += 1
                        elif light == 0 and heavy == 1:
                            barra_obelisco2_cont += 2
                        lista_de_tiros_esquerda.remove(d)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        recarga += janela.delta_time()

        if barra_dragon_cont == 2:
            if barra_dragon == 19:
                musica_level_before_loop_dragon.stop()
                final = 1
            barra_dragon += 1
            barra_dragon_cont = 0

        if barra_obelisco1_cont == 2:
            barra_obelisco1 += 1
            barra_obelisco1_cont = 0
        
        if barra_obelisco2_cont == 2:
            barra_obelisco2 += 1
            barra_obelisco2_cont = 0

        # vida e tiro do dragao
        if barra_dragon <= 19:
            recarga_dragon += janela.delta_time()
            timer += janela.delta_time()
            boss_vida[barra_dragon].draw()
            dragon.draw()
            dragon.update()

            if lista_de_tiros_inimigo != []:
                for d in lista_de_tiros_inimigo:
                    d.draw()
                    d.update()
                    d.x -= 410 * janela.delta_time()

                    tiro_dragon_object.set_position(d.x+12, d.y+14)
                    if tiro_dragon_object.collided(idle_object) and d in lista_de_tiros_inimigo:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo.remove(d)
            
            if recarga_dragon >= 1:
                if timer < 4:
                    lista_de_tiros_inimigo = pew_esquerda_inimigo(dragon, lista_de_tiros_inimigo)
                    recarga_dragon = 0
                else:
                    lista_de_tiros_inimigo = pew_esquerda_inimigo2(dragon, lista_de_tiros_inimigo)
                    timer = 0
                    recarga_dragon = 0

        obelisco1.draw()
        obelisco1.update()

        obelisco2.draw()
        obelisco2.update()

        # tiros do obelisco 1
        if barra_obelisco1 <= 3 and barra_dragon <= 19:
            vida[barra_obelisco1].draw()
            recarga_obelisco1 += janela.delta_time()

            if lista_de_tiros_inimigo_esquerda1 != []:
                for d in lista_de_tiros_inimigo_esquerda1:
                    d.draw()
                    d.update()
                    d.x -= 250 * janela.delta_time()
                    tiro_obelisk_object1.set_position(d.x+20, d.y+13)
                    if tiro_obelisk_object1.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda1:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda1.remove(d)

            if recarga_obelisco1 >= 2:
                lista_de_tiros_inimigo_esquerda1 = pew_obelisco1(obelisco1, lista_de_tiros_inimigo_esquerda1)
                recarga_obelisco1 = 0


        # tiros do obelisco 2
        if barra_obelisco2 <= 3 and barra_dragon <= 19:
            recarga_obelisco2 += janela.delta_time()
            vida2[barra_obelisco2].draw()

            if lista_de_tiros_inimigo_esquerda2 != []:
                for d in lista_de_tiros_inimigo_esquerda2:
                    d.draw()
                    d.update()
                    d.x -= 250 * janela.delta_time()
                    tiro_obelisk_object2.set_position(d.x+20, d.y+13)
                    if tiro_obelisk_object2.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda2:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda2.remove(d)

            if recarga_obelisco2 >= 2:
                lista_de_tiros_inimigo_esquerda2 = pew_obelisco2(obelisco2, lista_de_tiros_inimigo_esquerda2)
                recarga_obelisco2 = 0 

        if barra_obelisco1 > 3 and barra_dragon <= 19:
            reset_1 += janela.delta_time()
            if reset_1 > 12:
                barra_obelisco1 = 0
                reset_1 = 0
                lista_de_tiros_inimigo_esquerda1 = []
        
        if barra_obelisco2 > 3 and barra_dragon <= 19:
            reset_2 += janela.delta_time()
            if reset_2 > 12:
                barra_obelisco2 = 0
                reset_2 = 0
                lista_de_tiros_inimigo_esquerda2 = []

        if barra_dragon > 19:
            obelisco1.hide()
            obelisco2.hide()

        if shield_delay == True:
            shield_timer += janela.delta_time()
            if shield_timer > 13:
                shield_delay = False
                shield_timer = 0
        elif shield_delay == False and barra_dragon <= 19:
            shield.draw()
            shield.update()

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3:
            vida_p[barra_p].draw()
        else:
            musica_level_before_intro_dragon.stop()
            musica_level_before_loop_dragon.stop()
            hurt.stop()
            while toca_risada == True and run_risada == True:
                risada.play()
                run_risada = False
                break
            janela.delay(2000)
            game_over_screen()

        if final == 1:
            dragon.draw()
            dragon.stop()
            timerzinho += janela.delta_time()
            if timerzinho > 1:
                while toca_voice == True and run_voice == True:
                    dragon_voice.play()
                    run_voice = False
                    break
            toca_delay += janela.delta_time()
            explosao_delay += janela.delta_time()
            if explosao_delay > 6 and explosao_delay < 6.1:
                explosao = 1

            if toca_delay > 5:
                while toca_finish == True and run == True:
                    finish.play()
                    run = False
                    break
            
            if explosao == 1:
                toca_explosao = True
                puff.draw()
                puff.update()
                kaboom.draw()
                kaboom.update()
                if not puff.is_playing():
                    final = 0
                    explosao = 2
                    puff.hide()
                    kaboom.hide()
                    acabou = 1

            while toca_explosao == True and explosao_boolean == True:
                explosion.play()
                explosao_boolean = False
                break

        if acabou == 1:
            orb.draw()
            orb.update()

            if idle_object.collided(orb_object):
                janela.draw_text("Press E to Interact", orb.x -7, orb.y - 10, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", orb.x -10, orb.y - 12, size=27, color=(255, 0, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    fim = 1
                    acabou = 0

        if fim == 1:
            pretin.draw()
            frase_timer += janela.delta_time()
            if frase_timer > 2 and frase_timer < 6:
                frase_fim.draw()
            if frase_timer > 8:
                frase_fim2.draw()
            if frase_timer > 13:
                fim = 0
                fim_screen()

        # troca dos tiros
        if barra_dragon > 19: # somente se todos os inimigos estiverem derrotados

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