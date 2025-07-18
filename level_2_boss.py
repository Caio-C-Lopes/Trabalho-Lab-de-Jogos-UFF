from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_2_9 import *
from level_2_boss_reward import *

framerate = 60
last_time = time.time()

def pew_direita(player, lista):
    tiro = Sprite("tiro_direita.png", 5)
    tiro.set_sequence_time(0, 4, 100, True)

    tiro.x = player.x + 240
    tiro.y = player.y + 160

    lista.append(tiro)

    return lista

def pew_esquerda(player, lista):
    tiro = Sprite("tiro_esquerda.png", 5)
    tiro.set_sequence_time(0, 4, 100, True)

    tiro.x = player.x + 55
    tiro.y = player.y + 160

    lista.append(tiro)

    return lista

def pew_boss(inimigo, lista):
    tiro = Sprite("boss_tiro.png", 6)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x+20
    tiro.y = inimigo.y+170

    lista.append(tiro)

    return lista

def limita_tiros_direita(tiro, lista_de_tiros):
    if tiro in lista_de_tiros:
        if tiro.x >= 880:
            lista_de_tiros.remove(tiro)

def limita_tiros_esquerda(tiro, lista_de_tiros):
    if tiro in lista_de_tiros:
        if tiro.x <= 0:
            lista_de_tiros.remove(tiro)

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

def jogar_2_boss(coins, barra_per, dash_got):
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    boss_music_intro = pygame.mixer.Sound("boss_music_intro2.ogg")
    boss_music_loop = pygame.mixer.Sound("boss_music_loop2.ogg")

    wind = pygame.mixer.Sound("wind.wav")
    wind.play(loops=-1)
    wind.set_volume(0.1)

    # audio
    impacto = pygame.mixer.Sound("impact.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    stone = pygame.mixer.Sound("stone.wav")
    touch = pygame.mixer.Sound("Retro7.wav")
    touch2 = pygame.mixer.Sound("Modern5.wav")
    boss_music_intro.set_volume(0.3)
    boss_music_loop.set_volume(0.3)
    impacto.set_volume(0.5)
    stone.set_volume(0.5)
    hurt.set_volume(0.4)
    touch.set_volume(0.3)

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
    level2_boss = GameImage("fundo2_boss.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 160
    WIDTH = 358
    vely = 320

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_boss = 0
    lista_de_tiros_boss = []

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

    # obelisco no começo (Boss summon)
    summon = Sprite("pedra_boss.png", 14)
    summon.set_total_duration(1500)
    summon.set_loop(False)
    summon.set_position((janela.width/2 - summon.width/2), (janela.height/2 - summon.height/2)-155)
    summon_sfx = pygame.mixer.Sound("summon_sfx.wav")
    summon_sfx.set_volume(0.5)
    invocado = 0

    pedra_boss_object = Sprite("pedra_boss_object.png")
    pedra_boss_object.set_position(summon.x+50, summon.y+270)
    ask_boss = Sprite("ask_boss.png")
    ask = 0
    animation = 0
    conta_animation = 0

    # mecha boss
    boss = Sprite("mecha2.png", 12)
    boss.set_sequence_time(0, 3, 300, True)

    boss_block = Sprite("block.png", 12)
    boss_block.set_sequence_time(0, 11, 300, True)

    boss_block_volta = Sprite("block_volta.png", 12)
    boss_block_volta.set_sequence_time(0, 11, 300, False)

    # vida do mecha boss
    boss_vida = []
    for i in range(11):
        vida = Sprite(f"boss_vida_fase2_{i}.png")
        vida.set_position((janela.width/2 - vida.width/2) + 10, 440)
        boss_vida.append(vida)
    barra_boss = 11
    barra_boss_cont = 0

    boss.set_position((janela.width/2 - boss.width/2)+340, (janela.height/2 - boss.height/2)+50)
    boss_block.set_position(boss.x, boss.y)
    boss_block_volta.set_position(boss.x, boss.y)

    fala1 = Sprite("fala_1.png")
    fala2 = Sprite("fala_2.png")
    fala1.set_position((janela.width/2 - fala1.width/2),(janela.height/2 - fala1.height/2)+250)
    fala2.set_position((janela.width/2 - fala2.width/2),(janela.height/2 - fala2.height/2)+250)
    fala = 0
    fala_delay = 0
    fala2_delay = 0
    normal = 0

    # golemzinhos

    # golem 1
    # andando pra direita
    golem_direita1 = Sprite("golemzinho_direita.png", 4)
    golem_direita1.set_total_duration(1000)
    golem_direita1.set_position((janela.width/2 - golem_direita1.width/2)+160, (janela.height/2 - golem_direita1.height/2))

    # andando pra esquerda
    golem_esquerda1 = Sprite("golemzinho_esquerda.png", 4)
    golem_esquerda_backup1 = Sprite("golemzinho_esquerda.png", 4)
    golem_esquerda_backup1.set_total_duration(1000)
    golem_esquerda1.set_position(golem_direita1.x, golem_direita1.y)
    golem_esquerda1.set_total_duration(1000)

    # golem 2
    # andando pra direita
    golem_direita2 = Sprite("golemzinho_direita.png", 4)
    golem_direita2.set_total_duration(1000)
    golem_direita2.set_position((janela.width/2 - golem_direita2.width/2)+160, (janela.height/2 - golem_direita2.height/2)+235)

    # andando pra esquerda
    golem_esquerda2 = Sprite("golemzinho_esquerda.png", 4)
    golem_esquerda_backup2 = Sprite("golemzinho_esquerda.png", 4)
    golem_esquerda_backup2.set_total_duration(1000)
    golem_esquerda2.set_position(golem_direita2.x, golem_direita2.y)
    golem_esquerda2.set_total_duration(1000)

    # vida dos golemzinhos
    vida1 = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = golem_esquerda1.x+50
    vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = golem_esquerda1.y+35
    barra_golem1 = 4

    vida2 = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = golem_esquerda2.x+50
    vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = golem_esquerda2.y+35
    barra_golem2 = 4

    tiro_boss_object = Sprite("tiro_boss_object.png")
    boss_object = Sprite("boss_object.png")
    golem_object1 = Sprite("golem_object1.png")
    golem_object2 = Sprite("golem_object2.png")

    colisao1 = 0
    colisao2 = 0

    block_cont = 0
    block_volta = 0
    volta = 0
    bloqueio = 0
    block_volta_cont = 0
    conta_golem = 0
    draw_vida = 0

    # musica
    toca_musica = True
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    executa_musica = False
    conta_loop = 0

    final = 0

    # explosion
    puff = Sprite("puff.png", 59)
    puff.set_loop(False)
    puff.set_total_duration(1500)
    puff.set_position(janela.width/2 - puff.width/2, (janela.height/2 - puff.height/2))

    kaboom = Sprite("kaboom.png", 60)
    kaboom.set_loop(False)
    kaboom.set_total_duration(1500)
    kaboom.set_position((janela.width/2 - kaboom.width/2)+45, (janela.height/2 - kaboom.height/2)-20)

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

    stage_clear = Sprite("stage_clear.png")
    stage_clear.set_position(janela.width/2 - stage_clear.width/2, (janela.height/2 - stage_clear.height/2)+40)

    # portal
    portal = Sprite("portal.png", 6)
    portal.set_total_duration(1000)
    portal.set_position((janela.width/2 - portal.width/2), (janela.height/2 - portal.height/2)+170)
    portal_object = Sprite("portal_object.png")
    portal_object.set_position(portal.x+35, portal.y+3)
    portal_delay = 0
    portal_sound = pygame.mixer.Sound("portal_sound.wav")
    portal_sound.set_volume(0.3)
    toca_portal = False
    portal_boolean = True
    # gema verde portrait
    gema_verde_portrait = Sprite("gema_verde_icon.png")
    gema_verde_portrait.set_position((janela.width - gema_verde_portrait.width) - 10, 10)
    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level2_boss.draw()
        if conta_animation < 1.5:
            summon.draw()
        else:
            if conta_animation > 1.5 and conta_animation < 2:
                executa_musica = True
                barra_boss = 0
        
        if executa_musica == True:
            # musica
            while toca_musica == True and run_musica == True:
                boss_music_intro.play(0)
                conta_loop_before = True
                run_musica = False
                break

            if conta_loop_before == True:
                conta_loop += janela.delta_time()

            if conta_loop >= 6.2:
                toca_musica_loop = True

            while toca_musica_loop == True and run_musica_loop == True:
                boss_music_loop.play(loops=-1)
                run_musica_loop = False
                break
        
        if invocado == 0:
            if idle_object.collided(pedra_boss_object):
                janela.draw_text("Press E to Interact", summon.x-6, summon.y+130, size=28, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                janela.draw_text("Press E to Interact", summon.x-8, summon.y+128, size=28, color=(0, 255, 255), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    ask = 1
                    invocado = 1
                    touch2.play()

        if explosao == 2:
            portal_delay += janela.delta_time()
            if portal_delay > 0.7:
                toca_portal = True
                portal.draw()
                portal.update()
                # proxima fase (entrar no portal)
                if idle_object.collided(portal_object):
                    janela.draw_text("Press E to Interact", portal.x - 27, portal.y - 30, size=27, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
                    janela.draw_text("Press E to Interact", portal.x - 30, portal.y - 32, size=27, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                    if teclado.key_pressed("E"):
                        portal_sound.stop()
                        jogar_2_boss_reward(coins, barra_p, dash_got)
            stage_clear.draw()
        
        while toca_portal == True and portal_boolean == True:
            portal_sound.play(loops=-1)
            toca_portal = False
            portal_boolean = False
            break

        # dinheiro
        bolso.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

        # golemzinhos
        golem_direita1.x = golem_esquerda1.x
        golem_direita1.y = golem_esquerda1.y

        golem_direita2.x = golem_esquerda2.x
        golem_direita2.y = golem_esquerda2.y

        # vida do golem 1
        vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = golem_esquerda1.x+45
        vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = golem_esquerda1.y+43

        # vida do golem 2
        vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = golem_esquerda2.x+45
        vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = golem_esquerda2.y+43

        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3 or idle_object.collided(boss_object):
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
        if ask == 0:
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
                if barra_boss < 10:
                    if teclado.key_pressed("D") and idle.x <= 480:
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

            if invocado == 0:
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
            
            if invocado == 1:
                # andar para cima virado para direita
                if teclado.key_pressed("W") and idle.y >= HEIGHT-60 and virado_direita:
                    idle = run_direita
                    idle.y -= vel_per * dt

                # andar para cima virado para esquerda
                if teclado.key_pressed("W") and idle.y >= HEIGHT-60 and virado_esquerda:
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

                if invocado == 0:
                    # andar para cima virado para direita
                    if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_direita:
                        idle = run_direita
                        idle.y -= vel_per * dt

                    # andar para baixo virado para direita
                    if teclado.key_pressed("S") and idle.y <= WIDTH and virado_direita:
                        idle = run_direita
                        idle.y += vel_per * dt
                    
                if invocado == 1:
                    # andar para cima virado para direita
                    if teclado.key_pressed("W") and idle.y >= HEIGHT-50 and virado_direita:
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
                if invocado == 0:
                    # andar para cima virado para esquerda
                    if teclado.key_pressed("W") and idle.y >= HEIGHT and virado_esquerda:
                        idle = run_esquerda
                        idle.y -= vel_per * dt

                    # andar para baixo virado para esquerda
                    if teclado.key_pressed("S") and idle.y <= WIDTH and virado_esquerda:
                        idle = run_esquerda
                        idle.y += vel_per * dt
                if invocado == 1:
                    # andar para cima virado para esquerda
                    if teclado.key_pressed("W") and idle.y >= HEIGHT-50 and virado_esquerda:
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
            
        if barra_boss_cont == 3:
            if barra_boss == 9:
                final = 1
            barra_boss += 1
            barra_boss_cont = 0

        # tiro normal do personagem
        if lista_de_tiros_direita != [] and direita: # direita
            for d in lista_de_tiros_direita:
                d.draw()
                d.update()
                d.x += 200 * janela.delta_time()
                if barra_boss < 10:
                    if d.collided(boss_object) and d in lista_de_tiros_direita:
                        if barra_boss == 9:
                            pass
                            #scorp_die.play()   
                        if bloqueio == 0:
                            impacto.play()
                            barra_boss_cont += 1
                        else:
                            stone.play()
                        lista_de_tiros_direita.remove(d)

                # golem 1
                if barra_golem1 <= 3:
                    if d.collided(golem_object1) and d in lista_de_tiros_direita:
                        if barra_golem1 == 3:
                            pass
                            #scorp_die.play()
                        impacto.play()
                        barra_golem1 += 2
                        lista_de_tiros_direita.remove(d)

                # golem 2
                if barra_golem2 <= 3:
                    if d.collided(golem_object2) and d in lista_de_tiros_direita:
                        if barra_golem2 == 3:
                            pass
                            #scorp_die.play()
                        impacto.play()
                        barra_golem2 += 2
                        lista_de_tiros_direita.remove(d)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()

                # golem 1
                if barra_golem1 <= 3:
                    if d.collided(golem_object1) and d in lista_de_tiros_esquerda:
                        if barra_golem1 == 3:
                            pass
                            #scorp_die.play()
                        impacto.play()
                        barra_golem1 += 2
                        lista_de_tiros_esquerda.remove(d)

                # golem 2
                if barra_golem2 <= 3:
                    if d.collided(golem_object2) and d in lista_de_tiros_esquerda:
                        if barra_golem2 == 3:
                            pass
                            #scorp_die.play()
                        impacto.play()
                        barra_golem2 += 2
                        lista_de_tiros_esquerda.remove(d)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        recarga += janela.delta_time()
        recarga_boss += janela.delta_time()

        # proxima fase

        # deseja invocar    
        if ask == 1:
            ask_boss.draw()
            if teclado.key_pressed("S"):
                wind.stop()
                touch.play()
                summon_sfx.play()
                animation = 1
                ask = 0
            
            if teclado.key_pressed("N"):
                ask = 0
                invocado = 0
                touch.play()
        
        # roda animação da pedra
        if animation == 1:
            conta_animation += janela.delta_time()
            summon.update()

        if barra_boss < 10:
            fala = 1
            boss.y += vely * janela.delta_time()
            boss_block.set_position(boss.x, boss.y)
            boss_block_volta.set_position(boss.x, boss.y)

            puff.set_position(boss.x+135, boss.y+100)
            kaboom.set_position(boss.x+135, boss.y+100)

            if draw_vida == 1:
                boss_vida[barra_boss].draw()

            # tiro do boss
            if lista_de_tiros_boss != []:
                for d in lista_de_tiros_boss:
                    d.draw()
                    d.update()
                    tiro_boss_object.set_position(d.x+30, d.y+35)
                    d.x -= 220 * janela.delta_time()
                    if tiro_boss_object.collided(idle_object) and d in lista_de_tiros_boss:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_boss.remove(d)

            if recarga_boss >= 0.7:
                lista_de_tiros_boss = pew_boss(boss, lista_de_tiros_boss)
                recarga_boss = 0
            
            # limite superior
            if boss.y <= -20:
                boss.y = -20
                vely *= -1

            # limite inferior
            if boss.y >= (janela.height - boss.height)+150:
                boss.y = (janela.height - boss.height)+150
                vely *= -1
            
            # object
            boss_object.set_position(boss.x+150, boss.y+140)
            frame_block_stop = boss_block.get_curr_frame()

            # block
            if block_cont > 10:
                if not boss_block.is_playing():
                    boss_block.play()
                bloqueio = 1
                normal = 1

            if frame_block_stop == 10:
                boss_block.pause()

            if block_volta > 10:
                boss_block.stop()
                volta = 1
                bloqueio = 0

            if bloqueio == 1:
                block_volta += janela.delta_time()
                conta_golem += janela.delta_time()
                boss_block.draw()
                boss_block.update()
            
            if conta_golem > 1 and conta_golem < 1.5:
                colisao1 = 0
                colisao2 = 0
                barra_golem1 = 0
                barra_golem2 = 0
            
            if bloqueio == 0 and barra_golem1 > 3:
                golem_esquerda1.set_position((janela.width/2 - golem_esquerda1.width/2)+160, (janela.height/2 - golem_esquerda1.height/2))

            if bloqueio == 0 and barra_golem2 > 3:
                golem_esquerda2.set_position((janela.width/2 - golem_esquerda2.width/2)+160, (janela.height/2 - golem_esquerda2.height/2)+235)
            
            if normal == 0:
                block_cont += janela.delta_time()
                boss.draw()
                boss.update()

            if volta == 1:
                block_volta_cont += janela.delta_time()
                if not boss_block_volta.is_playing():
                    boss_block_volta.play()
                boss_block_volta.draw()
                boss_block_volta.update()
                if block_volta_cont > 3:
                    boss_block_volta.stop()
                    block_cont = 0
                    block_volta = 0
                    normal = 0
                    volta = 0
                    block_volta_cont = 0
                    conta_golem = 0

            # IA do golem 1
            if barra_golem1 <= 3:
                vida1[barra_golem1].draw()
                golem_esquerda1.draw()
                golem_esquerda1.update()
                golem_direita1.update()
                golem_esquerda_backup1.x = golem_esquerda1.x
                golem_esquerda_backup1.y = golem_esquerda1.y
                golem_object1.set_position(golem_esquerda1.x+65, golem_esquerda1.y+70)

                # deixar o golem sempre virado pro personagem
                if idle_object.x > golem_object1.x and idle_object.x - golem_object1.x > 10:
                    golem_esquerda1 = golem_direita1             
                elif idle_object.x < golem_object1.x and golem_object1.x - idle_object.x > 10:
                    golem_esquerda1 = golem_esquerda_backup1

                # perseguição do golem pelo personagem
                # eixo x
                if idle_object.x < golem_object1.x:
                    golem_esquerda1.x -= 0.6 * dt
                elif idle_object.x > golem_object1.x:
                    golem_esquerda1.x += 0.6 * dt

                # eixo y
                if idle_object.y < golem_object1.y:
                    golem_esquerda1.y -= 0.6 * dt
                elif idle_object.y > golem_object1.y:
                    golem_esquerda1.y += 0.6 * dt

                #colisão do golem 1 com o personagem
                    while colisao1 == 0:
                        if golem_object1.collided(idle_object):
                            hurt.play()
                            barra_p += 2
                            colisao1 = 1
                            barra_golem1 = 4
                        break
            else:
                golem_esquerda1.x = 535

            # IA do golem 2
            if barra_golem2 <= 3:
                vida2[barra_golem2].draw()
                golem_esquerda2.draw()
                golem_esquerda2.update()
                golem_direita2.update()
                golem_esquerda_backup2.x = golem_esquerda2.x
                golem_esquerda_backup2.y = golem_esquerda2.y
                golem_object2.set_position(golem_esquerda2.x+65, golem_esquerda2.y+70)

                # deixar o golem sempre virado pro personagem
                if idle_object.x > golem_object2.x and idle_object.x - golem_object2.x > 10:
                    golem_esquerda2 = golem_direita2            
                elif idle_object.x < golem_object2.x and golem_object2.x - idle_object.x > 10:
                    golem_esquerda2 = golem_esquerda_backup2

                # perseguição do golem pelo personagem
                # eixo x
                if idle_object.x < golem_object2.x:
                    golem_esquerda2.x -= 0.6 * dt
                elif idle_object.x > golem_object2.x:
                    golem_esquerda2.x += 0.6 * dt

                # eixo y
                if idle_object.y < golem_object2.y:
                    golem_esquerda2.y -= 0.6 * dt
                elif idle_object.y > golem_object2.y:
                    golem_esquerda2.y += 0.6 * dt

                #colisão do golem 2 com o personagem
                    while colisao2 == 0:
                        if golem_object2.collided(idle_object):
                            hurt.play()
                            barra_p += 2
                            colisao2 = 1
                            barra_golem2 = 4
                        break

        else:
            boss_music_intro.stop()
            boss_music_loop.stop()
            
        if final == 1:
            boss.draw()
            boss.stop()
            toca_delay += janela.delta_time()
            explosao_delay += janela.delta_time()
            if explosao_delay > 3 and explosao_delay < 3.1:
                explosao = 1

            if toca_delay > 2:
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

            while toca_explosao == True and explosao_boolean == True:
                explosion.play()
                explosao_boolean = False
                break
    
        gema_verde_portrait.draw()
        # fala do guardião
        if fala == 1:
            fala_delay += janela.delta_time()
            if fala_delay < 3:
                fala1.draw()
            else:
                fala2_delay += janela.delta_time()
                if fala2_delay < 3:
                    fala2.draw()
                else:
                    fala = 0
                    draw_vida = 1
        
        janela.update()