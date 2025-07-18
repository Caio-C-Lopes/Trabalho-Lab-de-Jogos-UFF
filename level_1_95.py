from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_1_boss import *

def jogar_1_95(coins, barra_per, key, musica_level_before_loop):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    chave = key

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
    level1_95 = GameImage("fundo1_95.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358

    recarga = 3

    # passagem
    ask = Sprite("ask.png")
    ask_not = Sprite("ask_not.png")
    pergunta = 0
    delay = 0
    ask_choice = 0
    barreira = Sprite("barreira.png")
    barreira.set_position(janela.width-barreira.width - 8, 265)

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)
    vel_per = 3
    last_time = time.time()

    while True:

        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level1_95.draw()
        bolso.draw()
        barreira.draw()
        # dinheiro
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

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
        if pergunta == 0:
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

        recarga += janela.delta_time()

        # proxima fase
        if idle.x >= janela.width - idle.width + 140:
            pergunta = 1
            idle.pause()
            if ask_choice == 0:
                ask.draw()
            if teclado.key_pressed("S"):
                musica_level_before_loop.stop()
                jogar_1_boss(coins, barra_p, chave)
            if teclado.key_pressed("N"):
                idle.x -= 20
                pergunta = 0

        janela.update()
