from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from level_1_5 import *
from tiros_functions1 import *
import pygame
pygame.init()

framerate = 60
last_time = time.time()

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

def jogar():
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    musica_level_before_loop = pygame.mixer.Sound("musica_level_before_loop.ogg")
    musica_level_before_intro = pygame.mixer.Sound("musica_level_before_intro.ogg")
    musica_level_before_intro.set_volume(0.3)
    musica_level_before_loop.set_volume(0.3)

    impacto = pygame.mixer.Sound("impact.wav")
    bone_crack = pygame.mixer.Sound("bone_crack.wav")
    scorp_die = pygame.mixer.Sound("scorp_die.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    coin = pygame.mixer.Sound("coin.wav")
    heal = pygame.mixer.Sound("heal.wav")
    impacto.set_volume(0.5)
    hurt.set_volume(0.4)
    coin.set_volume(0.4)
    heal.set_volume(0.4)
    bone_crack.set_volume(0.6)
    scorp_die.set_volume(0.6)

    # Inimigos
    # escorpiao
    scorpion = Sprite("Walk.png", 3)
    scorpion.set_total_duration(1000)
    scorpion.x = 750 + 80
    scorpion.y = 300

    # esqueleto
    # andando pra direita
    skeleton_direita = Sprite("esqueleto_direita.png", 6)
    skeleton_direita.set_total_duration(1000)
    skeleton_direita.x = 480
    skeleton_direita.y = 100

    # andando pra esquerda
    skeleton_esquerda = Sprite("esqueleto_esquerda.png", 6)
    esqueleto_esquerda_backup = Sprite("esqueleto_esquerda.png", 6)
    esqueleto_esquerda_backup.set_total_duration(1000)
    skeleton_esquerda.set_total_duration(1000)
    skeleton_esquerda.x = skeleton_direita.x
    skeleton_esquerda.y = skeleton_direita.y

    # vida do escorpião
    vida = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida[0].x = vida[1].x = vida[2].x = vida[3].x = scorpion.x
    vida[0].y = vida[1].y = vida[2].y = vida[3].y = scorpion.y
    barra = 0

    # vida do esqueleto
    vida_e = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_e[0].x = vida_e[1].x = vida_e[2].x = vida_e[3].x = skeleton_esquerda.x
    vida_e[0].y = vida_e[1].y = vida_e[2].y = vida_e[3].y = skeleton_esquerda.y
    barra_e = 0

    # tiro
    lista_de_tiros_inimigo = []

    # personagem
    # movimentação
    # declarando e posicionando o personagem
    idle = Sprite("idle_direita.png", 4)
    idle.set_position((janela.width/2 - idle.width/2)-232,(janela.height/2 - idle.height/2)+101)

    # "máscara" para fazer as colisões do personagem ou dos monstros
    idle_object = Sprite("object.png")
    idle_object.set_position(idle.x, idle.y)

    skeleton_object = Sprite("esqueleto_object.png")
    skeleton_object.x = skeleton_esquerda.x
    skeleton_object.y = skeleton_esquerda.y

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
    barra_p = 0

    # levels#
    level1 = GameImage("fundo1.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358
    limite_superior = HEIGHT + 130
    vely = 200

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0
    colisao = 0

    # item dropável
    health_box = Sprite("vida_box.png")
    gold = Sprite("gold.png")
    box_visible = 1
    gold_visible = 1

    # money money
    coins = 0
    gold.x = scorpion.x - 50
    gold.y = scorpion.y + 50
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)

    # boneco no começo da fase
    boneco = Sprite("run_direita.png", 4)
    boneco.set_total_duration(1000)
    boneco.set_position(0, 210)
    boneco.x -= 300

    quest = False
    delay_loading = 0
    fundo_load = Sprite("fundo_load.png")
    loading = True
    load = Sprite("load.png", 12)
    load.set_total_duration(1000)
    load.x += 10
    load.y += 520

    toca_musica = False
    run_musica = True

    toca_musica_loop = False
    run_musica_loop = True

    conta_loop_before = False
    conta_loop = 0

    vel_per = 3
    last_time = time.time()

    barulhin_menu = pygame.mixer.Sound("barulhin_menu.wav")
    toca_barulhin = True
    roda_barulhin = True

    toca_risada = True
    run_risada = True
    risada = pygame.mixer.Sound("risada.wav")
    risada.set_volume(0.3)

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level1.draw()
        delay_loading += dt

        while toca_musica == True and run_musica == True:
            musica_level_before_intro.play(0)
            conta_loop_before = True
            run_musica = False
            break

        if conta_loop_before == True:
            conta_loop += dt

        if conta_loop >= 307:
            toca_musica_loop = True

        while toca_musica_loop == True and run_musica_loop == True:
            musica_level_before_loop.play(loops=-1)
            run_musica_loop = False
            break

        if loading == True:
            toca_barulhin = True
            fundo_load.draw()
            load.draw()
            load.update()
            if delay_loading > 800:
                loading = False
                toca_musica = True

        while toca_barulhin == True and roda_barulhin == True:
            barulhin_menu.play()
            roda_barulhin = False
            break

        if loading == False and quest == False:

            if delay_loading > 10:
                boneco.draw()
                boneco.update()
                if boneco.x < 55:
                    boneco.x += 100 * janela.delta_time()
                else:
                    boneco.pause()
                    quest = True

        elif loading == False and quest == True:
            # dinheiro
            bolso.draw()
            janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

            bolso.draw()

            scorpion.y += vely * janela.delta_time()
            skeleton_object.set_position(skeleton_esquerda.x+200, skeleton_esquerda.y+180)

            skeleton_direita.x = skeleton_esquerda.x
            skeleton_direita.y = skeleton_esquerda.y

            # vida do escorpião
            vida[0].x = vida[1].x = vida[2].x = vida[3].x = scorpion.x
            vida[0].y = vida[1].y = vida[2].y = vida[3].y = scorpion.y - 20

            # vida do esqueleto
            vida_e[0].x = vida_e[1].x = vida_e[2].x = vida_e[3].x = skeleton_esquerda.x + 166
            vida_e[0].y = vida_e[1].y = vida_e[2].y = vida_e[3].y = skeleton_esquerda.y + 150

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
                    if barra <= 3:
                        if d.collided(scorpion) and d in lista_de_tiros_direita:
                            if barra == 3:
                                scorp_die.play()
                            impacto.play()
                            barra += 1
                            lista_de_tiros_direita.remove(d)
                    if barra_e <= 3:
                        if d.collided(skeleton_object) and d in lista_de_tiros_direita:
                            if barra_e == 3:
                                bone_crack.play()
                            impacto.play()
                            barra_e += 1
                            lista_de_tiros_direita.remove(d)
                    if d in lista_de_tiros_direita:
                        d = limita_tiros_direita(d, lista_de_tiros_direita)

            if lista_de_tiros_esquerda != [] and esquerda: #esquerda
                for d in lista_de_tiros_esquerda:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    if barra <= 3:
                        if d.collided(scorpion) and d in lista_de_tiros_esquerda:
                            if barra == 3:
                                scorp_die.play()
                            impacto.play()
                            barra += 1
                            lista_de_tiros_esquerda.remove(d)
                    if barra_e <= 3:
                        if d.collided(skeleton_object) and d in lista_de_tiros_esquerda:
                            if barra_e == 3:
                                bone_crack.play()
                            impacto.play()
                            barra_e += 1
                            lista_de_tiros_esquerda.remove(d)
                    if d in lista_de_tiros_esquerda:
                        d = limita_tiros_esquerda(d, lista_de_tiros_esquerda)

            if lista_de_tiros_esquerda == []:
                esquerda = False

            if lista_de_tiros_direita == []:
                direita = False

            # Inimigos
            # desenhar o esqueleto e a barra de vida do escorpião e atualizá-la a cada acerto de tiro
            if barra_e <= 3:
                vida_e[barra_e].draw()
                skeleton_esquerda.draw()
                skeleton_esquerda.update()
                skeleton_direita.update()
                esqueleto_esquerda_backup.update()
                vida_e[0].x = vida_e[1].x = vida_e[2].x = vida_e[3].x = skeleton_esquerda.x + 166
                vida_e[0].y = vida_e[1].y = vida_e[2].y = vida_e[3].y = skeleton_direita.y + 147

            # desenhar o escorpião e a barra de vida do escorpião e atualizá-la a cada acerto de tiro
            if barra <= 3:
                vida[barra].draw()
                scorpion.draw()
                scorpion.update()
                vida[0].y = vida[1].y = vida[2].y = vida[3].y = scorpion.y - 20

            elif barra_e > 3 and barra > 3: # box de vida se pegar, recupera a vida total, escorpião morto

                if box_visible == 1:
                    health_box.draw()

                if gold_visible == 1:
                    gold.draw()

                if gold_visible == 1:
                    if idle_object.collided(gold):
                        gold_visible = 0
                        coins = 100
                        coin.play()

                # jogador coletar o loot
                if box_visible == 1:
                    if idle_object.collided(health_box):
                        barra_p = 0
                        box_visible = 0
                        heal.play()

                # proxima fase
                if idle.x >= janela.width - idle.width + 140:
                    jogar_1_5(coins, barra_p, musica_level_before_loop)

            # IA do escorpião
            if barra <= 3:
                recarga_inimigo += janela.delta_time()

                # limite superior
                if scorpion.y <= limite_superior:
                    scorpion.y = limite_superior
                    vely *= -1

                # limite inferior
                if scorpion.y >= janela.height - scorpion.height:
                    scorpion.y = janela.height - scorpion.height
                    vely *= -1

                # loot do escorpião
                health_box.x = scorpion.x
                health_box.y = scorpion.y

                # tiro do escorpião
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
                    lista_de_tiros_inimigo = pew_esquerda_inimigo(scorpion, lista_de_tiros_inimigo)
                    recarga_inimigo = 0

            recarga += janela.delta_time()

            # IA do esqueleto
            if barra_e <= 3:
                esqueleto_esquerda_backup.x = skeleton_esquerda.x
                esqueleto_esquerda_backup.y = skeleton_esquerda.y
                # deixar o esqueleto sempre virado pro personagem
                if idle_object.x > skeleton_object.x and idle_object.x - skeleton_object.x > 10:
                    skeleton_esquerda = skeleton_direita
                if idle_object.x < skeleton_object.x and skeleton_object.x - idle_object.x > 10:
                    skeleton_esquerda = esqueleto_esquerda_backup

                # perseguição do esqueleto pelo personagem
                # eixo x
                if idle_object.x < skeleton_object.x:
                    skeleton_esquerda.x -= 1 * dt
                elif idle_object.x > skeleton_object.x:
                    skeleton_esquerda.x += 1 * dt

                # eixo y
                if idle_object.y < skeleton_object.y:
                    skeleton_esquerda.y -= 1 * dt
                elif idle_object.y > skeleton_object.y:
                    skeleton_esquerda.y += 1 * dt

                # colisão do esqueleto com o personagem
                while colisao == 0:
                    if skeleton_object.collided(idle_object):
                        hurt.play()
                        barra_p += 2
                        colisao = 1
                        barra_e = 4
                    break
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
