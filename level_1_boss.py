from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_1_boss_reward import *
from tiros_functions1 import *

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

def jogar_1_boss(coins, barra_per, key):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    chave = key

    pygame.mixer_music.unload()

    impacto = pygame.mixer.Sound("impact.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    boss_music_intro = pygame.mixer.Sound("boss_music_intro.ogg")
    boss_music_loop = pygame.mixer.Sound("boss_music_loop.ogg")
    wind = pygame.mixer.Sound("wind.wav")
    wind.play(loops=-1)

    wind.set_volume(0.1)
    boss_music_intro.set_volume(0.2)
    boss_music_loop.set_volume(0.2)
    impacto.set_volume(0.5)
    hurt.set_volume(0.4)

    # Inimigos
    # slime
    slime = Sprite("slime.png", 4)
    slime.set_total_duration(1000)
    slime.set_position(janela.width/2 - slime.width/2, janela.height/2 - slime.height/2)

    # vidinha do slimezinho
    vida_s = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_s[0].x = vida_s[1].x = vida_s[2].x = vida_s[3].x = slime.x
    vida_s[0].y = vida_s[1].y = vida_s[2].y = vida_s[3].y = slime.y - 8
    barra_s = 0

    # red slime chefe
    slime_vermelho = Sprite("slime_vermelho.png", 4)
    slime_vermelho.set_total_duration(1000)
    slime_vermelho.set_position(slime.x, slime.y)

    # red slime pequeno da direita
    slime_vermelho_pequeno = Sprite("slime_pequeno_red.png", 4)
    slime_vermelho_pequeno.set_total_duration(500)
    slime_vermelho_pequeno.set_position((janela.width - slime_vermelho_pequeno.width)+20, slime.y)

    slime_vermelho_pequeno_object = Sprite("slime_pequeno_red_object.png")
    slime_vermelho_pequeno_object.set_position(slime_vermelho_pequeno.x, slime_vermelho_pequeno.y)

    # vidinha do slimezinho pequeno vermelho da direita
    vida_v = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_v[0].x = vida_v[1].x = vida_v[2].x = vida_v[3].x = slime_vermelho_pequeno.x
    vida_v[0].y = vida_v[1].y = vida_v[2].y = vida_v[3].y = slime_vermelho_pequeno.y - 8
    barra_v = 0

    # red slime pequeno da esquerda
    slime_vermelho_pequeno2 = Sprite("slime_pequeno_red2.png", 4)
    slime_vermelho_pequeno2.set_total_duration(500)
    slime_vermelho_pequeno2.set_position(20, slime.y)

    slime_vermelho_pequeno2_object = Sprite("slime_pequeno_red_object.png")
    slime_vermelho_pequeno2_object.set_position(slime_vermelho_pequeno2.x, slime_vermelho_pequeno2.y)

    # vidinha do slimezinho pequeno vermelho da esquerda
    vida_v2 = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_v2[0].x = vida_v2[1].x = vida_v2[2].x = vida_v2[3].x = slime_vermelho_pequeno2.x
    vida_v2[0].y = vida_v2[1].y = vida_v2[2].y = vida_v2[3].y = slime_vermelho_pequeno2.y - 8
    barra_v2 = 4

    # vida do slime vermelho chefe
    boss_vida = []
    for i in range(11):
        vida = Sprite(f"boss_vida_{i}.png")
        vida.set_position((janela.width/2 - vida.width/2) + 10, 440)
        boss_vida.append(vida)
    barra_b = 0
    barra_b_cont = 0

    # personagem
    # movimentação
    # declarando e posicionando o personagem
    idle = Sprite("idle_direita.png", 4)
    idle.set_position((janela.width/2 - idle.width/2)-232,(janela.height/2 - idle.height/2)+101)

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
    level1_boss = GameImage("fundo1_boss.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = -65
    WIDTH = 358
    limite_superior = HEIGHT + 130
    slime_vermelho_pequeno_vely = 100
    slime_vermelho_pequeno2_vely = 100

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0
    recarga_inimigo_pequeno = 0
    recarga_inimigo_pequeno2 = 0
    red = False
    lista_de_tiros_inimigo_esquerda = []
    lista_de_tiros_inimigo_direita = []

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)

    pisca_timer = 0
    lista_de_tiros_inimigo_pequeno_esquerda = []
    lista_de_tiros_inimigo_pequeno_direita = []
    check = 0
    direito_vivo = True
    esquerda_vivo = False
    vel = 0
    toca = 1
    conta_toca = 0
    toca_loop = True

    # portal
    portal = Sprite("portal.png", 6)
    portal.set_total_duration(1000)
    portal.set_position((janela.width/2 - portal.width/2), (janela.height/2 - portal.height/2))
    portal_object = Sprite("portal_object.png")
    portal_object.set_position(portal.x+35, portal.y+3)

    #stage clear
    stage_clear = Sprite("stage_clear.png")
    stage_clear.set_position(janela.width/2 - stage_clear.width/2, (janela.height/2 - stage_clear.height/2)-120)

    # explosion
    puff = Sprite("puff.png", 59)
    puff.set_loop(False)
    puff.set_total_duration(1500)
    puff.set_position(janela.width/2 - puff.width/2, (janela.height/2 - puff.height/2))

    kaboom = Sprite("kaboom.png", 60)
    kaboom.set_loop(False)
    kaboom.set_total_duration(1500)
    kaboom.set_position((janela.width/2 - kaboom.width/2)+45, (janela.height/2 - kaboom.height/2)-20)

    slime_vermelho_puff = Sprite("slime_vermelho_morto.png", 4)
    slime_vermelho_puff.set_total_duration(1000)
    slime_vermelho_puff.set_position(slime_vermelho.x, slime_vermelho.y)
    puff_draw = True

    explosao = 0
    explosao_delay = 0
    portal_delay = 0

    finish = pygame.mixer.Sound("finish.wav")
    explosion = pygame.mixer.Sound("explosion.wav")
    explosion.set_volume(0.6)
    finish.set_volume(0.6)
    toca_delay = 0
    toca_finish = False
    toca_explosao = False
    explosao_boolean = True
    run = True

    portal_sound = pygame.mixer.Sound("portal_sound.wav")
    portal_sound.set_volume(0.3)
    toca_portal = False
    portal_boolean = True

    vel_per = 3
    last_time = time.time()

    toca_risada = True
    run_risada = True
    risada = pygame.mixer.Sound("risada.wav")
    risada.set_volume(0.3)

    tiro_object_esquerda = Sprite("tiro_object.png")
    tiro_object_direita = Sprite("tiro_object.png")
    tiro_object_esquerda_pequeno = Sprite("tiro_object.png")
    tiro_object_direita_pequeno = Sprite("tiro_object.png")

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level1_boss.draw()
        bolso.draw()
        slime_vermelho_puff.set_curr_frame(slime_vermelho.get_curr_frame())

        # dinheiro
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        if barra_b == 10:
            toca_delay += janela.delta_time()
            toca_finish = True
            explosao_delay += janela.delta_time()
            if explosao_delay > 3 and explosao_delay < 3.1:
                explosao = 1
            if puff_draw == True:
                slime_vermelho_puff.draw()
            boss_music_loop.stop()
            if explosao == 2:
                portal_delay += janela.delta_time()
                if portal_delay > 0.7:
                    toca_portal = True
                    portal.draw()
                    portal.update()

        if toca_delay > 2:
            while toca_finish == True and run == True:
                finish.play()
                run = False
                break

        while toca_portal == True and portal_boolean == True:
            portal_sound.play(loops=-1)
            toca_portal = False
            portal_boolean = False
            break

        if explosao == 1:
            toca_explosao = True
            puff.draw()
            puff.update()
            kaboom.draw()
            kaboom.update()
            if not puff.is_playing():
                puff_draw = False
                explosao = 2
                puff.hide()
                kaboom.hide()

        while toca_explosao == True and explosao_boolean == True:
            explosion.play()
            explosao_boolean = False
            break

        if explosao == 2:
            stage_clear.draw()

        pisca_timer += janela.delta_time()
        slime_vermelho_pequeno.y += slime_vermelho_pequeno_vely * janela.delta_time()
        slime_vermelho_pequeno2.y += slime_vermelho_pequeno2_vely * janela.delta_time()

        slime_vermelho_pequeno_object.set_position(slime_vermelho_pequeno.x+40, slime_vermelho_pequeno.y+45)
        slime_vermelho_pequeno2_object.set_position(slime_vermelho_pequeno2.x + 40, slime_vermelho_pequeno2.y + 45)

        # vida do slimezinho pequeno vermelho da direita
        vida_v[0].y = vida_v[1].y = vida_v[2].y = vida_v[3].y = slime_vermelho_pequeno.y - 8

        # vida do slimezinho pequeno vermelho da esquerda
        vida_v2[0].y = vida_v2[1].y = vida_v2[2].y = vida_v2[3].y = slime_vermelho_pequeno2.y - 8

        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

        idle.draw()
        run_direita.update()
        run_esquerda.update()
        idle_direita.update()
        idle_esquerda.update()

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

        # tiro normal do personage
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
                if red:
                    if barra_b <= 10:
                        if d.collided(slime_vermelho) and d in lista_de_tiros_direita:
                            impacto.play()
                            barra_b_cont += 1
                            lista_de_tiros_direita.remove(d)
                    if barra_v <= 3:
                        if d.collided(slime_vermelho_pequeno_object) and d in lista_de_tiros_direita:
                            impacto.play()
                            barra_v += 1
                            lista_de_tiros_direita.remove(d)
                if barra_s <= 3:
                    if d.collided(slime) and d in lista_de_tiros_direita:
                        impacto.play()
                        barra_s += 1
                        lista_de_tiros_direita.remove(d)
                if d in lista_de_tiros_direita:
                    d = limita_tiros_direita(d, lista_de_tiros_direita)
        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if red:
                    if barra_b <= 10:
                        if d.collided(slime_vermelho) and d in lista_de_tiros_esquerda:
                            impacto.play()
                            barra_b_cont += 4
                            lista_de_tiros_esquerda.remove(d)
                    if barra_v2 <= 3:
                        if d.collided(slime_vermelho_pequeno2_object) and d in lista_de_tiros_esquerda:
                            impacto.play()
                            barra_v2 += 1
                            lista_de_tiros_esquerda.remove(d)
                if barra_s <= 3:
                    if d.collided(slime) and d in lista_de_tiros_esquerda:
                        impacto.play()
                        barra_s += 1
                        lista_de_tiros_esquerda.remove(d)
                if d in lista_de_tiros_esquerda:
                    d = limita_tiros_esquerda(d, lista_de_tiros_esquerda)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        # Inimigos
        # desenhar o slime e a barra de vida e atualizá-la a cada acerto de tiro
        if barra_s == 4 or barra_s == 5 or barra_s == 6:
            while toca == 1:
                boss_music_intro.play()
                break
            barra_s = 7
        if conta_toca > 3 and toca_loop == True:
            while toca == 1:
                boss_music_loop.play(loops=-1)
                break
            toca_loop = False
        if barra_s <= 3:
            vida_s[barra_s].draw()
            slime.draw()
            slime.update()
        else:
            conta_toca += janela.delta_time()
            wind.stop()
            if barra_b < 10:
                red = True
            else:
                boss_music_loop.stop()
                red = False
                # proxima fase (entrar no portal)
                if idle_object.collided(portal_object) and explosao == 2:
                    janela.draw_text("Press E to Interact", portal.x - 27, portal.y - 30, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press E to Interact", portal.x - 30, portal.y - 32, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("E"):
                        wind.stop()
                        portal_sound.stop()
                        jogar_1_boss_reward(coins, barra_p, chave)

        if red:
            slime_vermelho.draw()
            slime_vermelho.update()
            if barra_b_cont == 4 or barra_b_cont == 5:
                barra_b += 1
                barra_b_cont = 0
            if barra_b == 10:
                red = False
            boss_vida[barra_b].draw()

            # alternancia entre os slimes
            if barra_b < 9:
                if direito_vivo and not esquerda_vivo:
                    if barra_v > 3:
                        direito_vivo = False
                        esquerda_vivo = True
                        barra_v2 = 0
                        barra_b += 1
                        vel += 0.1
                        lista_de_tiros_inimigo_pequeno_direita = []
                        lista_de_tiros_inimigo_pequeno_esquerda = []
                elif esquerda_vivo and not direito_vivo:
                    if barra_v2 > 3:
                        direito_vivo = True
                        esquerda_vivo = False
                        barra_v = 0
                        barra_b += 1
                        vel += 0.1
                        lista_de_tiros_inimigo_pequeno_direita = []
                        lista_de_tiros_inimigo_pequeno_esquerda = []
            else:
                while check == 0:
                    barra_v = 0
                    barra_v2 = 0
                    check = 1
                if barra_v == 4 and barra_v2 == 4:
                    barra_b += 1

            # slime pequeno na direita
            if barra_v <= 3:
                vida_v[barra_v].draw()
                slime_vermelho_pequeno.draw()
                slime_vermelho_pequeno.update()
                vida_v[0].y = vida_v[1].y = vida_v[2].y = vida_v[3].y = slime_vermelho_pequeno.y - 8

                # tiro e movimentação do slime pequeno na direita
                recarga_inimigo_pequeno += janela.delta_time()
                if lista_de_tiros_inimigo_pequeno_esquerda != []:
                    for d in lista_de_tiros_inimigo_pequeno_esquerda:
                        d.draw()
                        d.update()
                        d.x -= 200 * janela.delta_time()
                        tiro_object_esquerda_pequeno.set_position(d.x+10, d.y)
                        if tiro_object_esquerda_pequeno.collided(idle_object) and d in lista_de_tiros_inimigo_pequeno_esquerda:
                            hurt.play()
                            barra_p += 1
                            lista_de_tiros_inimigo_pequeno_esquerda.remove(d)

                if recarga_inimigo_pequeno >= 1:
                    lista_de_tiros_inimigo_pequeno_esquerda = pew_esquerda_inimigo_pequeno(slime_vermelho_pequeno, lista_de_tiros_inimigo_pequeno_esquerda)
                    recarga_inimigo_pequeno = 0

                # limite superior
                if slime_vermelho_pequeno.y <= limite_superior:
                    slime_vermelho_pequeno.y = limite_superior
                    slime_vermelho_pequeno_vely *= -1

                # limite inferior
                if slime_vermelho_pequeno.y >= janela.height - slime_vermelho_pequeno.height:
                    slime_vermelho_pequeno.y = janela.height - slime_vermelho_pequeno.height
                    slime_vermelho_pequeno_vely *= -1

            # slime pequeno na esquerda
            if barra_v2 <= 3:
                vida_v2[barra_v2].draw()
                slime_vermelho_pequeno2.draw()
                slime_vermelho_pequeno2.update()
                vida_v2[0].y = vida_v2[1].y = vida_v2[2].y = vida_v2[3].y = slime_vermelho_pequeno2.y - 8

                # tiro e movimentação do slime pequeno da esquerda
                recarga_inimigo_pequeno2 += janela.delta_time()
                if lista_de_tiros_inimigo_pequeno_direita != []:
                    for d in lista_de_tiros_inimigo_pequeno_direita:
                        d.draw()
                        d.update()
                        d.x += 200 * janela.delta_time()
                        tiro_object_direita_pequeno.set_position(d.x+33, d.y)
                        if tiro_object_direita_pequeno.collided(idle_object) and d in lista_de_tiros_inimigo_pequeno_direita:
                            hurt.play()
                            barra_p += 1
                            lista_de_tiros_inimigo_pequeno_direita.remove(d)

                if recarga_inimigo_pequeno2 >= 1:
                    lista_de_tiros_inimigo_pequeno_direita = pew_direita_inimigo_pequeno(slime_vermelho_pequeno2, lista_de_tiros_inimigo_pequeno_direita)
                    recarga_inimigo_pequeno2 = 0

                # limite superior
                if slime_vermelho_pequeno2.y <= limite_superior:
                    slime_vermelho_pequeno2.y = limite_superior
                    slime_vermelho_pequeno2_vely *= -1

                # limite inferior
                if slime_vermelho_pequeno2.y >= janela.height - slime_vermelho_pequeno2.height:
                    slime_vermelho_pequeno2.y = janela.height - slime_vermelho_pequeno2.height
                    slime_vermelho_pequeno2_vely *= -1

            recarga_inimigo += janela.delta_time()

            # tiro do slime chefe
            # esquerda e direita ao mesmo tempo
            if lista_de_tiros_inimigo_esquerda != [] and lista_de_tiros_inimigo_direita != []:
                for d in lista_de_tiros_inimigo_esquerda:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    tiro_object_esquerda.set_position(d.x+10, d.y)                   
                    if tiro_object_esquerda.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda.remove(d)

                for d in lista_de_tiros_inimigo_direita:
                    d.draw()
                    d.update()
                    d.x += 200 * janela.delta_time()
                    tiro_object_direita.set_position(d.x+33, d.y)
                    if tiro_object_direita.collided(idle_object) and d in lista_de_tiros_inimigo_direita:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_direita.remove(d)

            if recarga_inimigo >= 2 - vel:
                lista_de_tiros_inimigo_esquerda = pew_esquerda_inimigo(slime_vermelho, lista_de_tiros_inimigo_esquerda)
                lista_de_tiros_inimigo_direita = pew_direita_inimigo(slime_vermelho, lista_de_tiros_inimigo_direita)
                recarga_inimigo = 0

        recarga += janela.delta_time()

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3 or idle_object.collided(slime_vermelho):
            vida_p[barra_p].draw()
        else:
            boss_music_intro.stop()
            boss_music_loop.stop()
            hurt.stop()
            while toca_risada == True and run_risada == True:
                risada.play()
                run_risada = False
                break
            janela.delay(2000)
            game_over_screen()

        janela.update()