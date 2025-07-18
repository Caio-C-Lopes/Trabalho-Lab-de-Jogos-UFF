from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_3_boss import*

def jogar_3_95(coins, barra_per, dash_got, leve, pesado):
    janela = Window(950, 594)
    janela.set_title("Before I Die")    

    # audio
    musica_level_before_loop_final = pygame.mixer.Sound("musica_level_before_loop4.ogg")
    musica_level_before_intro_final = pygame.mixer.Sound("musica_level_before_intro4.ogg")
    musica_level_before_intro_final.set_volume(0.3)
    musica_level_before_loop_final.set_volume(0.3)

    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("soul_sfx.wav")
    fusao_sfx = pygame.mixer.Sound("fusao_sfx.wav")
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
    idle.x = 50
    idle.y = 210

    # "máscara" para fazer as colisões do personagem ou dos monstros
    idle_object = Sprite("object.png")
    idle_object.x = 210
    idle_object.y = 350

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
    level3_95 = GameImage("fundo3_95.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 130
    WIDTH = 358

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)
    vel_per = 3
    last_time = time.time()

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

    barra = 4
    
    # fusão das reliquias
    reliquia_fusion = 0
    fusao = 0
    reliquia_timer = 0

    text_reliquia1 = Sprite("text_reliquia1.png")
    text_reliquia2 = Sprite("text_reliquia2.png")

    pretin = Sprite("pretin.png")

    gema_verde_fusion = Sprite("gema_verde_fusion.png")
    gema_azul_fusion = Sprite("gema_azul_fusion.png")
    gema_final_fusion = Sprite("gema_final_icon.png")

    gema_verde_fusion.set_position((janela.width/2 - gema_verde_fusion.width/2)+290, (janela.height/2 - gema_verde_fusion.height/2))
    gema_azul_fusion.set_position((janela.width/2 - gema_azul_fusion.width/2)-290, (janela.height/2 - gema_azul_fusion.height/2))

    fusao = 0
    fusao_timer = 0


    # gema final
    gema_final = False

    delay_gema_final = 0
    gema_final_recarga = 1000

    gema_final_sheet = Sprite("gema_final_sheet.png", 5)
    gema_final_sheet.set_total_duration(2200)
    gema_final_sheet.set_position((janela.width/2 - gema_final_sheet.width/2)-340, (janela.height/2 - gema_final_sheet.height/2)-150)


    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(1)

    toca_gema_final = True
    run_toca_gema_final = False
    fundiu = False

    # orb
    orb = Sprite("orb.png", 22)
    orb.set_total_duration(1000)
    orb.set_position((janela.width - orb.width) - 60, (janela.height / 2 - orb.height / 2) + 110)

    orb_object = Sprite("orb_object.png")
    orb_object.set_position(orb.x + 22, orb.y + 22)

    # ask
    fundo_ask_final = Sprite("ask_final.png")
    ask = 0

    touch = pygame.mixer.Sound("Retro7.wav")
    touch.set_volume(1)
    touch2 = pygame.mixer.Sound("Modern5.wav")
    touch2.set_volume(1)

    # musica
    toca_musica = True
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    conta_loop = 0

    # sfx fusao
    toca_fusao = True
    run_fusao = True

    gema_final_text = Sprite("text_reliquia3.png")

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level3_95.draw()
        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

        # musica
        while toca_musica == True and run_musica == True:
            musica_level_before_intro_final.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 1150:
            toca_musica_loop = True

        while toca_musica_loop == True and run_musica_loop == True:
            musica_level_before_loop_final.play(loops=-1)
            run_musica_loop = False
            break

        if fundiu == False:
            gema_verde_portrait.draw()
            gema_azul_portrait.draw()

        # junção das relíquias
        if idle.x >= 500 and fusao_timer < 9:
            reliquia_fusion = 1
        else:
            reliquia_fusion = 0
        
                    
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

        # gema final
        if fundiu == True:
            gema_final_recarga += dt
            gema_final_sheet.draw()
            if teclado.key_pressed("J") and gema_final_recarga >= 1000:
                gema_final = True
                gema_final_recarga = 0
                run_toca_gema_final = True
        
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

        # portrait do personagem
        portrait.draw()
        
        if reliquia_fusion == 0 and fusao == 0 and ask == 0:
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

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3:
            vida_p[barra_p].draw()

        # fusao das reliquias
        if reliquia_fusion == 1 and reliquia_timer < 12:
            idle.stop()
            reliquia_timer += janela.delta_time()
            if reliquia_timer < 6:
                text_reliquia1.draw()

            if reliquia_timer > 6 and reliquia_timer < 12:
                text_reliquia2.draw()
                
            if reliquia_timer > 12:
                fusao = 1          

        if fusao == 1:
            idle.stop()
            pretin.draw()
            gema_verde_fusion.draw()
            gema_azul_fusion.draw()
            gema_azul_portrait.hide()
            gema_verde_portrait.hide()
            fusao_timer += janela.delta_time()
            if fusao_timer > 2:
                gema_final_fusion.set_position(gema_azul_fusion.x, gema_azul_fusion.y)
                if gema_azul_fusion.x <= 410:
                    gema_azul_fusion.x += 200 * janela.delta_time()
                    gema_verde_fusion.x -= 200 * janela.delta_time()
                else:
                    gema_verde_fusion.hide()
                    gema_azul_fusion.hide()
                    gema_final_fusion.draw()
                    while toca_fusao == True and run_fusao == True:
                        fusao_sfx.play()
                        run_fusao = False
                        break

            if fusao_timer > 8:
                gema_final_fusion.hide()

            if fusao_timer > 9:
                gema_final_text.draw()

            if fusao_timer > 15:
                fusao = 0
                pretin.hide()
                reliquia_fusion = 0
                fundiu = True

        if fusao == 0 and reliquia_fusion == 0:
            idle.play()

        if fundiu == True:
            # orb
            orb.draw()
            orb.update()
            if idle_object.collided(orb_object):
                janela.draw_text("Press E to Interact", orb.x -40, orb.y - 28, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", orb.x -43, orb.y - 30, size=27, color=(0, 255, 255), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    if ask == 0:
                        touch2.play()
                    ask = 1
            if ask == 1:
                fundo_ask_final.draw()
                if teclado.key_pressed("S"):
                    ask = 0
                    jogar_3_boss(barra_per, dash_got, light, heavy, musica_level_before_loop_final)

                if teclado.key_pressed("N"):
                    touch.play()
                    ask = 0

        # troca dos tiros
        if barra > 3 and reliquia_fusion == 0 and fusao == 0: # somente se todos os inimigos estiverem derrotados

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
