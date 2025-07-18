from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_2 import *

def jogar_1_boss_reward(coins, barra_per, key):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    chave = key

    # personagem
    # movimentação
    # declarando e posicionando o personagem
    idle = Sprite("idle_direita.png", 4)
    idle.set_position((janela.width/2 - idle.width/2)-315, (janela.height/2 - idle.height/2)+115)

    # "máscara" para fazer as colisões do personagem ou dos monstros
    idle_object = Sprite("object.png")
    idle_object.set_position(idle.x, idle.y)

    # parado pra direita
    idle_direita = Sprite("idle_direita.png", 4)
    idle_direita.set_total_duration(1000)

    # parado pra esquerda
    idle_esquerda = Sprite("idle_esquerda.png", 4)
    idle_esquerda.set_total_duration(1000)

    # andando pra direita
    run_direita = Sprite("run_direita.png", 4)
    run_direita.set_total_duration(1000)

    # andando pra esquerda
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
    fundo_1_boss_reward = GameImage("fundo_1_boss_reward.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 200
    WIDTH = 245

    recarga = 3

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)

    # baú
    chest = Sprite("chest.png", 12)
    chest.set_total_duration(1000)
    chest.set_loop(False)
    chest_object = Sprite("chest_object.png")
    chest.set_position(janela.width / 2 - chest.width / 2, (janela.height / 2 - chest.height / 2)+50)
    chest_object.set_position(chest.x + 6, chest.y + 21)
    interagiu = 0
    chest_animation = 0

    # gema
    gema_verde = Sprite("gem_verde.png", 7)
    gema_verde.set_total_duration(1000)
    gema_verde.set_position(chest.x + 14, chest.y - 90)
    gema_delay = 0

    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)

    # luz
    luz = Sprite("luz.png", 15)
    luz.set_total_duration(900)
    luz.x += 308
    luz.y += 40

    # stars
    stars = Sprite("stars.png", 4)
    stars.set_total_duration(1000)
    stars.y += 300

    stars_object = Sprite("stars_object.png")
    stars_object.set_position(stars.x, stars.y+50)

    stars_text_1 = Sprite("stars_text_1.png")
    stars_interagiu = 0

    fundo_preto = Sprite("fundo_preto.png")
    preto = 0
    preto_cont = 0
    chave_cont = 0
    chave_cont2 = 0
    chave_cont3 = 0
    chave_boolean = False
    texto = 0

    # bau 2
    chest_common = Sprite("chest_common.png", 12)
    chest_common.set_total_duration(1000)
    chest_common.set_position(janela.width / 2 - chest_common.width / 2, janela.height / 2 - chest_common.height / 2)
    chest_common.set_loop(False)

    chave_text = Sprite("chave_text.png")
    chave_text_sem_chave = Sprite("chave_text_sem_chave.png")
    chave_text_com_chave = Sprite("chave_text_com_chave.png")

    # loots
    coin_grande = Sprite("coin_grande.png", 9)
    coin_grande.set_total_duration(1000)
    coin_grande.set_loop(True)
    coin_grande.set_position(janela.width / 2 - coin_grande.width / 2,
                             janela.height / 2 - (coin_grande.height / 2) - 40)

    boots = Sprite("boots.png")
    boots.set_position((janela.width / 2 - boots.width / 2) + 5, (janela.height / 2 - boots.height / 2) - 40)

    # luz comum
    luz_common = Sprite("luz_common.png", 15)
    luz_common.set_total_duration(1000)
    luz_common.set_position(janela.width / 2 - luz_common.width / 2, (janela.height / 2 - luz_common.height / 2) - 65)

    # fim da interação com stars e bau de reliquia
    fim = 0
    fim_relic = 0

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
    boneco = Sprite("run_direita.png", 4)
    boneco.set_total_duration(1000)
    boneco.set_position((janela.width / 2 - boneco.width / 2) + 120, (janela.height / 2 - boneco.height / 2) - 60)

    boneco_dash = Sprite("run_direita_boot.png", 4)
    boneco_dash.set_total_duration(1000)
    boneco_dash.set_position(boneco.x, boneco.y)
    boneco_dash.set_curr_frame(0)
    boneco.set_curr_frame(0)

    desenha_mapa = 0
    mapa_anda_delay = 0
    x = Sprite("x.png")
    x.set_position((janela.width / 2 - x.width / 2) + 120, (janela.height / 2 - x.height / 2) - 40)
    entrar_delay = 0

    fundo_load_2 = Sprite("fundo_load_2.png")
    load = Sprite("load_ruinas2.png", 12)
    load.set_total_duration(1000)
    load.x += 10
    load.y += 520

    # musica
    boss_music_after = pygame.mixer.Sound("boss_music_after.ogg")
    boss_music_after.set_volume(0.2)
    boss_music_after.play(loops=-1)

    treasure = pygame.mixer.Sound("treasure.wav")
    treasure.set_volume(0.4)
    toca_treasure = False
    run_treasure = True
    treasure_delay = 0

    relic_sfx = pygame.mixer.Sound("relic_sfx.wav")
    relic_sfx.set_volume(0.5)

    toca_treasure_chave_coin = False
    coin_delay = 0
    run_coin = True

    boots_sfx = pygame.mixer.Sound("boots_sfx.wav")
    boots_sfx.set_volume(0.5)
    toca_boots = False
    run_boots = True

    touch = pygame.mixer.Sound("Retro7.wav")
    touch.set_volume(1)

    touch2 = pygame.mixer.Sound("Modern5.wav")
    touch2.set_volume(1)

    vel_per = 3
    last_time = time.time()

    # dash
    dash = False

    delay_dash = 0
    dash_recarga = 100

    dash_sheet = Sprite("dash_sheet.png", 5)
    dash_sheet.set_total_duration(2200)
    dash_sheet.set_position((janela.width/2 - dash_sheet.width/2)-410, (janela.height/2 - dash_sheet.height/2)-150)

    # press shift to dash
    dash_text = True

    dash_got = False

    # botinha do dash
    idle_direita_boot = Sprite("idle_direita_boot.png", 4)
    idle_esquerda_boot = Sprite("idle_esquerda_boot.png", 4)
    run_direita_boot = Sprite("run_direita_boot.png", 4)
    run_esquerda_boot = Sprite("run_esquerda_boot.png", 4)

    idle_direita_boot.set_total_duration(1000)
    idle_esquerda_boot.set_total_duration(1000)
    run_direita_boot.set_total_duration(1000)
    run_esquerda_boot.set_total_duration(1000)

    dash_sfx = pygame.mixer.Sound("dash_sfx.wav")
    dash_sfx.set_volume(0.5)

    toca_dash = True
    run_toca_dash = False

    while True:

        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        fundo_1_boss_reward.draw()
        bolso.draw()
        chest.draw()

        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        dash_recarga += dt

        # dash
        if chave_cont2 > 8 and preto == 2:
            idle_direita = idle_direita_boot
            idle_esquerda = idle_esquerda_boot
            run_direita = run_direita_boot
            run_esquerda = run_esquerda_boot
            
            if dash_text == True:
                janela.draw_text("Press SHIFT to Dash", idle.x+86, idle.y+107, size=27, color=(8, 24, 168), font_name="Arial", bold=True, italic=False)

            if teclado.key_pressed("LEFT_SHIFT") and dash_recarga >= 100:
                dash_text = False
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

        if idle_object.collided(chest_object) and fim_relic == 0:
            if interagiu == 0:
                janela.draw_text("Press E to Interact", chest.x - 41, chest.y - 16, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", chest.x - 44, chest.y - 18, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
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

        if chest_animation == 1:
            chest.update()
            
        if interagiu == 1:
            gema_delay += janela.delta_time()
            if gema_delay > 1:
                luz.draw()
                luz.update()
                gema_verde.draw()
                gema_verde.update()
                if idle_object.collided(chest_object):
                    janela.draw_text("Press C to Collect the Relic", chest.x - 80, chest.y - 124, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press C to Collect the Relic", chest.x - 83, chest.y - 126, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("C"):
                        relic_sfx.play()
                        treasure.stop()
                        interagiu = 2
        if interagiu == 2:
            gema_verde_portrait.draw()

        if fim == 0:
            stars.draw()
            stars.update()
            if idle_object.collided(stars_object):
                if stars_interagiu == 0:
                    janela.draw_text("Press I to Inspect", stars_object.x+2, stars_object.y-75, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press I to Inspect", stars_object.x+5, stars_object.y-77, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("I"):
                    if stars_interagiu == 0:
                        touch2.play()
                    stars_interagiu = 1
                    texto = 1
                if stars_interagiu == 1:
                    if texto == 1:
                        stars_text_1.draw()
                    preto = 1

        run_direita_boot.x = run_esquerda_boot.x = run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle_direita_boot.x = idle_esquerda_boot.x = idle.x
        run_direita_boot.y = run_esquerda_boot.y = run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle_direita_boot.y = idle_esquerda_boot.y = idle.y

        idle.draw()
        run_direita.update()
        run_esquerda.update()
        idle_direita.update()
        idle_esquerda.update()

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3:
            vida_p[barra_p].draw()
        else:
            janela.close()

        # portrait do personagem
        portrait.draw()
        # movimentação do player
        # esquerda
        if (preto == 0 and ask == 0) or (preto == 2 and ask == 0):
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

        # proxima fase
        if interagiu == 2:
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
                    idle.pause()
            if ask == 1:
                fundo_ask_fase_1.draw()
                if teclado.key_pressed("S"):
                    touch.play()
                    desenha_mapa = 1
                    ask = 0

                if teclado.key_pressed("N"):
                    touch.play()
                    ask = 0
                    idle.play()

            if desenha_mapa == 1:
                if dash_got == True:
                    boneco = boneco_dash
                mapa_anda_delay += janela.delta_time()
                mapa.draw()
                boneco.draw()
                if mapa_anda_delay > 1 and mapa_anda_delay < 4.6:
                    boneco.update()
                    boneco.x += 0.72 * dt
                    boneco.y += 0.72 * dt
                if mapa_anda_delay > 5.5:
                    x.draw()
                    boneco.set_curr_frame(0)
                    entrar_delay += janela.delta_time()
                if entrar_delay > 3:
                    boss_music_after.stop()
                    fundo_load_2.draw()
                    load.draw()
                    load.update()
                if entrar_delay > 13:
                    barra_p = 0
                    jogar_2(coins, barra_p, dash_got)
                    desenha_mapa = 0

        recarga += janela.delta_time()

        if preto == 1:
            preto_cont += janela.delta_time()

        if preto == 1:
            idle.pause()
            if preto_cont > 3:
                texto = 0
                fundo_preto.draw()
                chest_common.draw()

            if preto_cont > 3.5 and chave_boolean == False:
                chave_text.draw()

            if preto_cont > 7:
                chave_boolean = True

            if chave_boolean == True and chave == 0:
                chave_text_sem_chave.draw()
                chave_cont += janela.delta_time()
                if chave_cont > 4:
                    preto = 0
                    stars_interagiu = 0
                    fim = 1

            elif chave_boolean == True and chave == 1:
                chave_text_com_chave.draw()
                chave_cont += janela.delta_time()
                chest_common.update()
                coins = 1500
                toca_treasure_chave = True
                dash_got = True

                if chave_cont > 1.3:
                    chave_cont2 += janela.delta_time()

                    if chave_cont2 < 4:
                        luz_common.draw()
                        luz_common.update()
                        coin_grande.draw()
                        coin_grande.update()
                    if chave_cont2 > 4.7:
                        toca_boots = True
                        chave_cont3 += janela.delta_time()
                        luz_common.draw()
                        luz_common.update()
                        boots.draw()
                        if chave_cont3 > 4:
                            preto = 2
                            stars_interagiu = 0
                            fim = 1

                while toca_boots == True and run_boots == True:
                    boots_sfx.play()
                    run_boots = False
                    break

                if toca_treasure_chave == True:
                    coin_delay += janela.delta_time()

                if coin_delay > 0.6:
                    toca_treasure_chave_coin = True

                while toca_treasure_chave_coin == True and run_coin == True:
                    treasure.play()
                    run_coin = False
                    break
        janela.update()