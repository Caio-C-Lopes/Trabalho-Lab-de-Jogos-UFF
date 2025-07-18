from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_1_95 import *

def jogar_1_9(coins, barra_per,musica_level_before_loop):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    heal = pygame.mixer.Sound("heal.wav")
    buy = pygame.mixer.Sound("buy.wav")
    heal.set_volume(0.4)
    buy.set_volume(0.4)

    # Trader
    trader = Sprite("trader.png", 12)
    trader.set_total_duration(1000)
    trader.x = 0
    trader.y = 120
    talk_trader = Sprite("talk.png")
    talk_trader.set_position(74, 236)
    balao_trader = Sprite("balao_trader.png")
    balao_trader.set_position(janela.width - balao_trader.width, 0)
    shop = Sprite("shop.png")
    shop.set_position(janela.width - shop.width, 20)

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
    level1_9 = GameImage("fundo1_9.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358

    recarga = 3

    # money money
    coins = coins
    bolso = Sprite("bolso.png")
    bolso.set_position(2, 490)
    vel_per = 3
    last_time = time.time()

    # conversation variable
    fala = 0
    fala_trader = 0

    # shop items
    vida = Sprite("vida_box.png")
    vida.set_position((janela.width/2 - vida.width/2)+140, (janela.height/2 - vida.height/2)-21)
    chave = Sprite("key.png")
    chave.set_position((janela.width/2 - chave.width/2)+320, (janela.height/2 - chave.height/2)-55)

    # shop values
    gold_vida = Sprite("gold.png")
    gold_chave = Sprite("gold.png")

    gold_vida.set_position(vida.x-25, vida.y+50)
    gold_chave.set_position(chave.x-10, chave.y+118)

    # shop variables
    health = 0
    key = 0

    vel_per = 3
    last_time = time.time()

    touch = pygame.mixer.Sound("Retro7.wav") # go
    touch.set_volume(1)

    touch2 = pygame.mixer.Sound("Modern5.wav") # back
    touch2.set_volume(1)

    while True:

        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level1_9.draw()
        bolso.draw()
        # dinheiro
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)

        trader.draw()
        trader.update()

        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

        idle.draw()
        run_direita.update()
        run_esquerda.update()
        idle_direita.update()
        idle_esquerda.update()
        
        # desenhar a barra de vida do player
        vida_p[barra_p].draw()

        # portrait do personagem
        portrait.draw()

        # movimentação do player
        # esquerda
        if fala == 0 and fala_trader == 0:
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

        if idle.x >= janela.width - idle.width + 140:
            jogar_1_95(coins, barra_p, key, musica_level_before_loop)

        recarga += janela.delta_time()

        if idle_object.collided(talk_trader) and fala_trader == 0:
            janela.draw_text("Press T to Talk", 35, 180, size=35, color=("Green"), font_name="Arial", bold=False, italic=False)
            if teclado.key_pressed("T"):
                touch.play()
                fala_trader = 1
                idle.pause()

        if fala_trader == 1:
            balao_trader.draw()
            shop.draw()
            janela.draw_text("Press C to Close", 580, 490, size=40, color=("White"), font_name="Arial", bold=True, italic=False)

            # item vida
            if health == 0:
                vida.draw()
                gold_vida.draw()
                janela.draw_text("Press F to Buy", vida.x-30, vida.y+90, size=20, color=("Yellow"), font_name="Arial", bold=True, italic=False)
                janela.draw_text("300", vida.x+23, vida.y+57, size=30, color=("Green"), font_name="Arial", bold=True, italic=False)

            # item chave
            if key == 0:
                chave.draw()
                gold_chave.draw()
                janela.draw_text("Press G to Buy", chave.x-18, chave.y+160, size=20, color=("Yellow"), font_name="Arial", bold=True, italic=False)
                janela.draw_text("550", chave.x+40, chave.y+127, size=30, color=("Green"), font_name="Arial", bold=True, italic=False)

            if teclado.key_pressed("F") and coins >= 300:
                health = 1
                buy.play()
                barra_p = 0
                coins = 250
                heal.play()

            if teclado.key_pressed("G") and coins == 550:
                key = 1
                buy.play()
                coins = 0

            if teclado.key_pressed("C"):
                fala_trader = 0
                touch2.play()
                idle.play()

        janela.update()
