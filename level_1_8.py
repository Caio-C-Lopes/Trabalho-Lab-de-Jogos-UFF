from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_1_9 import *

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

def jogar_1_8(coins, barra_per, musica_level_before_loop):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    impacto = pygame.mixer.Sound("impact.wav")
    bat_die = pygame.mixer.Sound("bat_die.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    coin2 = pygame.mixer.Sound("coin2.wav")
    coin2.set_volume(0.5)
    impacto.set_volume(0.5)
    bat_die.set_volume(0.25)
    hurt.set_volume(0.4)

    # Inimigos
    # morcegos
    # morcego 1 andando
    bat = Sprite("bat_esquerda.png", 4)
    bat.set_position(janela.width - bat.width, 210)
    bat.set_total_duration(1000)

    # vida do morcego 1
    vida_m = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_m[0].x = vida_m[1].x = vida_m[2].x = vida_m[3].x = bat.x
    vida_m[0].y = vida_m[1].y = vida_m[2].y = vida_m[3].y = bat.y
    barra_m = 0

    # morcego 2 andando
    bat2 = Sprite("bat_direita.png", 4)
    bat2.set_position(-2, 300)
    bat2.set_total_duration(1000)

    # vida do morcego 2
    vida_m2 = [Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida_m2[0].x = vida_m2[1].x = vida_m2[2].x = vida_m2[3].x = bat2.x
    vida_m2[0].y = vida_m2[1].y = vida_m2[2].y = vida_m2[3].y = bat2.y
    barra_m2 = 0

    # tiro inimigo
    lista_de_tiros_inimigo_esquerda = []
    lista_de_tiros_inimigo_direita = []

    # personagem
    # movimentação
    # declarando e posicionando o personagem
    idle = Sprite("idle_direita.png", 4)
    idle.set_position((janela.width/2 - idle.width/2)-10, (janela.height/2 - idle.height/2)+110)

    # "máscara" para fazer as colisões do personagem ou dos monstros
    idle_object = Sprite("object.png")
    idle_object.set_position(idle.x, idle.y)

    # máscara dos morcegos
    bat_object = Sprite("bat_object.png")
    bat_object.x = bat.x
    bat_object.y = bat.y

    bat2_object = Sprite("bat_object.png")
    bat2_object.x = bat2.x
    bat2_object.y = bat2.y

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
    level1_8 = GameImage("fundo1_8.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358
    limite_superior = HEIGHT + 130
    bat_vely = 175
    bat2_vely = 175

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0

    # item dropável
    gold = Sprite("gold_blue.png")
    gold.x += 800
    gold.y += 400
    gold_visible = 1

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

    tiro_object_esquerda = Sprite("tiro_object.png")
    tiro_object_direita = Sprite("tiro_object.png")

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level1_8.draw()
        bolso.draw()

        # dinheiro
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

        bat.y += bat_vely * janela.delta_time()
        bat2.y += bat2_vely * janela.delta_time()

        bat_object.set_position(bat.x+30, bat.y+45)
        bat2_object.set_position(bat2.x+30, bat2.y+60)

        # morcego 1
        vida_m[0].x = vida_m[1].x = vida_m[2].x = vida_m[3].x = bat.x + 10
        vida_m[0].y = vida_m[1].y = vida_m[2].y = vida_m[3].y = bat.y + 10

        # morcego 2
        vida_m2[0].x = vida_m2[1].x = vida_m2[2].x = vida_m2[3].x = bat2.x + 10
        vida_m2[0].y = vida_m2[1].y = vida_m2[2].y = vida_m2[3].y = bat2.y + 10

        # personagem
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
                if barra_m <= 3:
                    if d.collided(bat_object) and d in lista_de_tiros_direita:
                        impacto.play()
                        if barra_m == 3:
                            bat_die.play()
                        barra_m += 1
                        lista_de_tiros_direita.remove(d)
                if barra_m2 <= 3:
                    if d.collided(bat2_object) and d in lista_de_tiros_direita:
                        impacto.play()
                        if barra_m2 == 3:
                            bat_die.play()
                        barra_m2 += 1
                        lista_de_tiros_direita.remove(d)
                if d in lista_de_tiros_direita:
                    d = limita_tiros_direita(d, lista_de_tiros_direita)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if barra_m <= 3:
                    if d.collided(bat_object) and d in lista_de_tiros_esquerda:
                        impacto.play()
                        if barra_m == 3:
                            bat_die.play()
                        barra_m += 1
                        lista_de_tiros_esquerda.remove(d)
                if barra_m2 <= 3:
                    if d.collided(bat2_object) and d in lista_de_tiros_esquerda:
                        impacto.play()
                        if barra_m2 == 3:
                            bat_die.play()
                        barra_m2 += 1
                        lista_de_tiros_esquerda.remove(d)
                if d in lista_de_tiros_esquerda:
                    d = limita_tiros_esquerda(d, lista_de_tiros_esquerda)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        # Inimigos
        # desenhar os morcegos e as barras de vidas e atualizá-las a cada acerto de tiro
        if barra_m <= 3:
            vida_m[barra_m].draw()
            bat.draw()
            bat.update()

        if barra_m2 <= 3:
            vida_m2[barra_m2].draw()
            bat2.draw()
            bat2.update()

        if barra_m > 3 and barra_m2 > 3: # morcegos mortos box de vida se pegar, recupera a vida total, escorpião morto

            if gold_visible == 1:
                gold.draw()

            if gold_visible == 1:
                if idle_object.collided(gold):
                    gold_visible = 0
                    coins = 550
                    coin2.play()

            if idle.x >= janela.width - idle.width + 140:
                jogar_1_9(coins, barra_p, musica_level_before_loop)

        # IA do morcego 1
        if barra_m <= 3:
            recarga_inimigo += janela.delta_time()

            # limite superior
            if bat.y <= limite_superior:
                bat.y = limite_superior
                bat_vely *= -1

            # limite inferior
            if bat.y >= janela.height - bat.height:
                bat.y = janela.height - bat.height
                bat_vely *= -1

            # vida dos morcego 1
            vida_m[barra_m].y = bat.y - 20

            # tiro do morcego 1
            if lista_de_tiros_inimigo_esquerda != []:
                for d in lista_de_tiros_inimigo_esquerda:
                    d.draw()
                    d.update()
                    d.x -= 200 * janela.delta_time()
                    tiro_object_esquerda.set_position(d.x+10, d.y)    
                    if tiro_object_esquerda.collided(idle_object) and d in lista_de_tiros_inimigo_esquerda:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_esquerda.remove(d)

            if recarga_inimigo >= 1:
                lista_de_tiros_inimigo_esquerda = pew_esquerda_inimigo(bat, lista_de_tiros_inimigo_esquerda)
                recarga_inimigo = 0

        # IA do morcego 2
        if barra_m2 <= 3:
            recarga_inimigo += janela.delta_time()

            # limite superior
            if bat2.y <= limite_superior:
                bat2.y = limite_superior
                bat2_vely *= -1

            # limite inferior
            if bat2.y >= janela.height - bat2.height:
                bat2.y = janela.height - bat2.height
                bat2_vely *= -1

            # vida dos morcego 2
            vida_m2[barra_m2].y = bat2.y - 20

            # tiro do morcego 2
            if lista_de_tiros_inimigo_direita != []:
                for d in lista_de_tiros_inimigo_direita:
                    d.draw()
                    d.update()
                    d.x += 200 * janela.delta_time()
                    tiro_object_direita.set_position(d.x+33, d.y)
                    if tiro_object_direita.collided(idle_object) and d in lista_de_tiros_inimigo_direita:
                        hurt.play()
                        barra_p += 1
                        lista_de_tiros_inimigo_direita.remove(d)

            if recarga_inimigo >= 1:
                lista_de_tiros_inimigo_direita = pew_direita_inimigo(bat2, lista_de_tiros_inimigo_direita)
                recarga_inimigo = 0

        recarga += janela.delta_time()

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
