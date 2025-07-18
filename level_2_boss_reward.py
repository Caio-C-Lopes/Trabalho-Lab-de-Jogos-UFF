from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_3_1 import *
from tiros_functions4 import *

def jogar_2_boss_reward(coins, barra_per, dash_got):
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    # baú
    chest = Sprite("chest_2.png", 12)
    chest.set_total_duration(1000)
    chest.set_loop(False)
    chest_object = Sprite("chest_object.png")
    chest.set_position((janela.width / 2 - chest.width / 2)+120, (janela.height / 2 - chest.height / 2))
    chest_object.set_position(chest.x + 6, chest.y + 21)
    interagiu = 0
    chest_animation = 0

    # baú 2
    chest_tiro = Sprite("chest_tiro.png", 12)
    chest_tiro.set_total_duration(1000)
    chest_tiro.set_loop(False)
    chest_tiro_object = Sprite("chest_object.png")
    chest_tiro.set_position((janela.width / 2 - chest_tiro.width / 2)-95, (janela.height / 2 - chest_tiro.height / 2))
    chest_tiro_object.set_position(chest_tiro.x + 6, chest_tiro.y + 21)

    # gema
    gema_azul = Sprite("gem_azul.png", 7)
    gema_azul.set_total_duration(1000)
    gema_azul.set_position(chest.x + 14, chest.y - 97)
    gema_delay = 0

    # gema azul portrait
    gema_azul_portrait = Sprite("gema_azul_icon.png")
    gema_azul_portrait.set_position((janela.width - gema_azul_portrait.width) - 92, 10)

    # luz
    luz = Sprite("luz_azul.png", 15)
    luz.set_total_duration(900)
    luz.x += 430
    luz.y -= 10

    # luz da arma
    luz_tiro = Sprite("luz_tiro.png", 15)
    luz_tiro.set_total_duration(900)
    luz_tiro.x += 212
    luz_tiro.y -= 10

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3

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
    level2_boss_reward = GameImage("fundo_2_boss_reward.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 150
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

    # dash sfx
    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(1)

    toca_dash = True
    run_toca_dash = False

    touch2 = pygame.mixer.Sound("Modern5.wav")
    touch2.set_volume(1)
    
    # chest com reliquia
    fim_relic = 0
    interagiu = 0
    chest_animation = 0

    treasure = pygame.mixer.Sound("treasure.wav")
    treasure.set_volume(0.4)
    toca_treasure = False
    run_treasure = True
    treasure_delay = 0

    relic_sfx = pygame.mixer.Sound("relic_sfx.wav")
    relic_sfx.set_volume(0.5)

    # chest com novo tiro
    fim_relic_tiro = 0
    interagiu_tiro = 0
    chest_animation_tiro = 0

    treasure_tiro = pygame.mixer.Sound("treasure.wav")
    treasure_tiro.set_volume(0.4)
    toca_treasure_tiro = False
    run_treasure_tiro = True
    treasure_delay_tiro = 0

    relic_sfx_tiro = pygame.mixer.Sound("relic_sfx.wav")
    relic_sfx_tiro.set_volume(0.5)
    gun_delay = 0


    # novo tiro
    boss_tiro_reward = Sprite("boss_tiro_reward.png", 6)
    boss_tiro_reward.set_total_duration(1000)
    boss_tiro_reward.set_position(chest_tiro.x-27, chest_tiro.y-110)


    # musica
    boss_music_after_intro = pygame.mixer.Sound("boss_music_after_intro.ogg")
    boss_music_after_loop = pygame.mixer.Sound("boss_music_after_loop.ogg")
    boss_music_after_intro.set_volume(0.2)
    boss_music_after_loop.set_volume(0.2)

    # musica
    toca_musica = True
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    conta_loop = 0

    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)

    tiro_text = Sprite("tiro_text.png")
    tiro_text2 = Sprite("tiro_text2.png")
    tiro = 0
    tiro_delay = 0

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

    light = 1
    heavy = 0
    mouse = janela.get_mouse()

    tela_tiro_sfx = pygame.mixer.Sound("tela_tiro_sfx.wav")
    tela_tiro_sfx.set_volume(0.6)
    toca_troca = False
    run_toca = True

    # orb
    orb = Sprite("orb.png", 22)
    orb.set_total_duration(1000)
    orb.set_position((janela.width - orb.width) - 60, (janela.height / 2 - orb.height / 2) + 110)
    orb_delay = 0

    orb_object = Sprite("orb_object.png")
    orb_object.set_position(orb.x + 22, orb.y + 22)

    # ask
    fundo_ask_fase_1 = Sprite("fundo_ask_fase_1.png")
    ask = 0

    # mapa
    mapa = Sprite("map.png")
    boneco = Sprite("run_esquerda.png", 4)
    boneco.set_total_duration(1000)
    boneco.set_position((janela.width / 2 - boneco.width / 2) + 255, (janela.height / 2 - boneco.height / 2) +93)

    boneco_dash = Sprite("run_esquerda_boot.png", 4)
    boneco_dash.set_total_duration(1000)
    boneco_dash.set_position(boneco.x, boneco.y)
    boneco_dash.set_curr_frame(1)
    boneco.set_curr_frame(1)
    desenha_mapa = 0
    mapa_anda_delay = 0
    x = Sprite("x.png")
    x.set_position((janela.width / 2 - x.width / 2) + 120, (janela.height / 2 - x.height / 2) - 40)
    entrar_delay = 0
    
    x2 = Sprite("x.png")
    x2.set_position((janela.width / 2 - x2.width / 2)+270, (janela.height / 2 - x2.height / 2) +105)

    touch = pygame.mixer.Sound("Retro7.wav")
    touch.set_volume(1)

    fundo_load_3 = Sprite("fundo_load_3.png")
    load = Sprite("load_terras_devastadas.png", 12)
    load.set_total_duration(1000)
    load.x += 10
    load.y += 520
    pegou = 0

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level2_boss_reward.draw()
        # musica
        while toca_musica == True and run_musica == True:
            boss_music_after_intro.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 255:
            toca_musica_loop = True

        while toca_musica_loop == True and run_musica_loop == True:
            boss_music_after_loop.play(loops=-1)
            run_musica_loop = False
            break

        chest.draw()
        chest_tiro.draw()

        # chest com reliquia
        if idle_object.collided(chest_object) and fim_relic == 0:
            if interagiu == 0:
                janela.draw_text("Press E to Interact", chest.x - 41, chest.y - 16, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", chest.x - 44, chest.y - 18, size=27, color=(0, 255, 255), font_name="Arial", bold=True, italic=False)
            if teclado.key_pressed("E"):
                touch2.play()
                toca_treasure = True
                interagiu = 1
                chest_animation = 1
                fim_relic = 1

        if toca_treasure == True:
            treasure_delay += janela.delta_time()

        while toca_treasure == True and run_treasure == True and treasure_delay > 0.6:
            treasure.play()
            toca_treasure = False
            break

        if interagiu == 1:
            gema_delay += janela.delta_time()
            if gema_delay > 1:
                luz.draw()
                luz.update()
                gema_azul.draw()
                gema_azul.update()
                if idle_object.collided(chest_object):
                    janela.draw_text("Press C to Collect the Relic", chest.x - 80, chest.y - 124, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press C to Collect the Relic", chest.x - 83, chest.y - 126, size=27, color=(0, 255, 255), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("C"):
                        relic_sfx.play()
                        treasure.stop()
                        interagiu = 2
                        pegou += 1
        
        if interagiu == 2:
            gema_azul_portrait.draw()        

        if chest_animation == 1:
            chest.update()

        # chest com novo tiro
        if idle_object.collided(chest_tiro_object) and fim_relic_tiro == 0:
            if interagiu_tiro == 0:
                janela.draw_text("Press E to Interact", chest_tiro.x - 41, chest_tiro.y - 16, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", chest_tiro.x - 44, chest_tiro.y - 18, size=27, color=(210, 4, 45), font_name="Arial", bold=True, italic=False)
            if teclado.key_pressed("E"):
                touch2.play()
                toca_treasure_tiro = True
                interagiu_tiro = 1
                chest_animation_tiro = 1
                fim_relic_tiro = 1

        if toca_treasure_tiro == True:
            treasure_delay_tiro += janela.delta_time()

        if interagiu_tiro == 1:
            gun_delay += janela.delta_time()
            if gun_delay > 1:
                luz_tiro.draw()
                luz_tiro.update()
                boss_tiro_reward.draw()
                boss_tiro_reward.update()
                if idle_object.collided(chest_tiro_object):
                    janela.draw_text("Press C to Collect the Shot", chest_tiro.x - 80, chest_tiro.y - 124, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press C to Collect the Shot", chest_tiro.x - 83, chest_tiro.y - 126, size=27, color=(210, 4, 45), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("C"):
                        relic_sfx_tiro.play()
                        treasure_tiro.stop()
                        interagiu_tiro = 2  
                        tiro = 1
                        pegou += 1

        while toca_treasure_tiro == True and run_treasure_tiro == True and treasure_delay_tiro > 0.6:
            treasure_tiro.play()
            toca_treasure_tiro = False
            break

        if chest_animation_tiro == 1:
            chest_tiro.update()
        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

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
        if tiro == 0 and troca == 0:
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

            if lista_de_tiros_esquerda != [] and esquerda: #esquerda
                for d in lista_de_tiros_esquerda:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()

            if lista_de_tiros_esquerda == []:
                esquerda = False

            if lista_de_tiros_direita == []:
                direita = False

            recarga += janela.delta_time()

        # vida
        vida_p = [Sprite("barra_cheia_p.png"), Sprite("barra_1p.png"), Sprite("barra_2p.png"), Sprite("barra_3p.png")]
        vida_p[0].x = vida_p[1].x = vida_p[2].x = vida_p[3].x = portrait.x + 105
        vida_p[0].y = vida_p[1].y = vida_p[2].y = vida_p[3].y = portrait.y + 23
        vida_p[barra_p].draw()
        gema_verde_portrait.draw()

        if tiro == 1:
            tiro_text.draw()
            tiro_delay += janela.delta_time()
            if tiro_delay > 3:
                tiro_text2.draw()
                if teclado.key_pressed("ENTER"):
                    touch.play()
                    tiro = 0

        # troca entre os tiros
        if interagiu_tiro == 2 and tiro == 0 and pegou == 2:

            # orb
            orb_delay += janela.delta_time()
            if orb_delay > 0.3:
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
                fundo_ask_fase_1.draw()
                if teclado.key_pressed("S"):
                    touch.play()
                    desenha_mapa = 1
                    ask = 0

                if teclado.key_pressed("N"):
                    touch.play()
                    ask = 0

            if desenha_mapa == 1:
                if dash_got == True:
                    boneco = boneco_dash
            
                mapa_anda_delay += janela.delta_time()
                mapa.draw()
                boneco.draw()
                x.draw()

                if mapa_anda_delay > 1 and mapa_anda_delay < 5.5:
                    boneco.update()
                    boneco.x -= 0.95 * dt
                    boneco.y -= 0.18 * dt
                if mapa_anda_delay > 6:
                    x2.draw()
                    boneco.set_curr_frame(1)
                    entrar_delay += janela.delta_time()
                if entrar_delay > 3:
                    boss_music_after_intro.stop()
                    boss_music_after_loop.stop()
                    fundo_load_3.draw()
                    load.draw()
                    load.update()
                if entrar_delay > 13:
                    jogar_3_1(coins, barra_p, dash_got, light, heavy)
                    desenha_mapa = 0

        # troca dos tiros
        if ask == 0 and interagiu_tiro == 2:
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
                        heavy = 1
                        light = 0
    
            while toca_troca == True and run_toca == True :
                tela_tiro_sfx.play()
                run_toca = False
                break


        janela.update()