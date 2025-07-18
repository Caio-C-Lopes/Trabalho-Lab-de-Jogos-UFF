from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_3_95 import*

def jogar_3_9(coins, barra_per, dash_got, leve, pesado, musica_level_before_loop):
    janela = Window(950, 594)
    janela.set_title("Before I Die")
    musica_level_before_loop.stop()

    wind = pygame.mixer.Sound("wind.wav")
    wind.play(loops=-1)

    wind.set_volume(0.1)

    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("soul_sfx.wav")
    ordem_errada_sfx = pygame.mixer.Sound("ordem_errada_sfx.wav")
    orb_sfx = pygame.mixer.Sound("orb_sfx.wav")
    pegar_orb_sfx = pygame.mixer.Sound("pegar_orb_sfx.wav")
    hurt = pygame.mixer.Sound("hurt.wav")
    item_sfx = pygame.mixer.Sound("item_sfx.wav")
    orb_unlock_sfx = pygame.mixer.Sound("orb_unlock.wav")
    pygame.mixer.music.set_volume(0.23)
    item_sfx.set_volume(0.4)
    soul_sfx.set_volume(0.5)
    impacto.set_volume(0.5)
    hurt.set_volume(0.4)
    orb_sfx.set_volume(0.5)
    pegar_orb_sfx.set_volume(0.7)
    orb_unlock_sfx.set_volume(0.5)
    ordem_errada_sfx.set_volume(0.5)

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
    level3_9 = GameImage("fundo3_9.png")

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

    tela_tiro_sfx = pygame.mixer.Sound("tela_tiro_sfx.wav")
    tela_tiro_sfx.set_volume(0.6)
    toca_troca = False
    run_toca = True

    barra = 4
    # sala de puzzle
    # colocar os as cores dos orbes na ordem do arco-íris

    # estatuas que impedem o jogador de avançar
    statue1 = Sprite("dragao_puzzle.png")
    statue1.set_position((janela.width/2 - statue1.width/2)+335, (janela.height/2 - statue1.height/2)+40)

    statue2 = Sprite("dragao_puzzle.png")
    statue2.set_position((janela.width/2 - statue2.width/2)+335, (janela.height/2 - statue2.height/2)-60)

    statue3 = Sprite("dragao_puzzle.png")
    statue3.set_position((janela.width/2 - statue3.width/2)+335, (janela.height/2 - statue3.height/2)+160)

    # orbes
    orbe_vermelho = Sprite("orbe_vermelho.png", 4)
    orbe_vermelho.set_total_duration(700)
    orbe_vermelho.set_position((janela.width/2 - orbe_vermelho.width/2)-170, (janela.height/2 - orbe_vermelho.height/2)+263)

    orbe_laranja = Sprite("orbe_laranja.png", 4)
    orbe_laranja.set_total_duration(700)
    orbe_laranja.set_position((janela.width/2 - orbe_laranja.width/2)-80, (janela.height/2 - orbe_laranja.height/2)+263)

    orbe_amarelo = Sprite("orbe_amarelo.png", 4)
    orbe_amarelo.set_total_duration(700)
    orbe_amarelo.set_position((janela.width/2 - orbe_amarelo.width/2)-265, (janela.height/2 - orbe_amarelo.height/2)+263)

    orbe_verde = Sprite("orbe_verde.png", 4)
    orbe_verde.set_total_duration(700)
    orbe_verde.set_position((janela.width/2 - orbe_verde.width/2)+10, (janela.height/2 - orbe_verde.height/2)+263)

    orbe_azul = Sprite("orbe_azul.png", 4)
    orbe_azul.set_total_duration(700)
    orbe_azul.set_position((janela.width/2 - orbe_azul.width/2)+100, (janela.height/2 - orbe_azul.height/2)+263)


    # orbes objects para interagir
    orbe_vermelho_object = Sprite("orbe_object.png")
    orbe_vermelho_object.set_position(orbe_vermelho.x+30, orbe_vermelho.y-5)

    orbe_laranja_object = Sprite("orbe_object.png")
    orbe_laranja_object.set_position(orbe_laranja.x+30, orbe_laranja.y-5)

    orbe_amarelo_object = Sprite("orbe_object.png")
    orbe_amarelo_object.set_position(orbe_amarelo.x+30, orbe_amarelo.y-5)

    orbe_verde_object = Sprite("orbe_object.png")
    orbe_verde_object.set_position(orbe_verde.x+30, orbe_verde.y-5)

    orbe_azul_object = Sprite("orbe_object.png")
    orbe_azul_object.set_position(orbe_azul.x+30, orbe_azul.y-5)


    # interação com os pilares
    pilar_object1 = Sprite("pilar_object.png")
    pilar_object1.set_position((janela.width/2 - pilar_object1.width/2)-268, (janela.height/2 - pilar_object1.height/2)-43)

    pilar_object2 = Sprite("pilar_object.png")
    pilar_object2.set_position((janela.width/2 - pilar_object1.width/2)-175, (janela.height/2 - pilar_object1.height/2)-43)

    pilar_object3 = Sprite("pilar_object.png")
    pilar_object3.set_position((janela.width/2 - pilar_object1.width/2)-81, (janela.height/2 - pilar_object1.height/2)-43)

    pilar_object4 = Sprite("pilar_object.png")
    pilar_object4.set_position((janela.width/2 - pilar_object1.width/2)+14, (janela.height/2 - pilar_object1.height/2)-43)

    pilar_object5 = Sprite("pilar_object.png")
    pilar_object5.set_position((janela.width/2 - pilar_object1.width/2)+109, (janela.height/2 - pilar_object1.height/2)-43)

    mouse = janela.get_mouse()

    hand1 = Sprite("maozinha_puzzel.png")
    hand2 = Sprite("maozinha_puzzel.png")
    hand3 = Sprite("maozinha_puzzel.png")
    hand4 = Sprite("maozinha_puzzel.png")
    hand5 = Sprite("maozinha_puzzel.png")

    # pilar 1
    hand1.set_position((janela.width/2 - hand1.width/2)-267, (janela.height/2 - hand1.height/2)-172)

    # pilar 2
    hand2.set_position((janela.width/2 - hand2.width/2)-180, (janela.height/2 - hand2.height/2)-172)

    # pilar 3
    hand3.set_position((janela.width/2 - hand3.width/2)-85, (janela.height/2 - hand3.height/2)-172)

    # pilar 4
    hand4.set_position((janela.width/2 - hand4.width/2)+10, (janela.height/2 - hand4.height/2)-172)

    # pilar 5
    hand5.set_position((janela.width/2 - hand5.width/2)+105, (janela.height/2 - hand5.height/2)-172)

    # contador para saber se a ordem está correta
    ordem = 0

    # variaveis para saber se o jogador escolheu ou não a posição do orbe
    
    # geral
    escolhendo = 0

    # amarelo
    escolhido_amarelo = False
    escolher_amarelo = False

    # vermelho
    escolhido_vermelho = False
    escolher_vermelho = False

    # laranja
    escolhido_laranja = False
    escolher_laranja = False

    # verde
    escolhido_verde = False
    escolher_verde = False

    # azul
    escolhido_azul = False
    escolher_azul = False


    # variaveis para as posições dos orbes nos pilares
    pilar1_x = orbe_amarelo.x-4
    pilar1_y = orbe_amarelo.y-400

    pilar2_x = orbe_amarelo.x+90
    pilar2_y = orbe_amarelo.y-400

    pilar3_x = orbe_amarelo.x+183
    pilar3_y = orbe_amarelo.y-400

    pilar4_x = orbe_amarelo.x+279
    pilar4_y = orbe_amarelo.y-400

    pilar5_x = orbe_amarelo.x+374
    pilar5_y = orbe_amarelo.y-400

    
    # variaveis para que os orbes não fiquem sobrepostos

    # em relação as possíveis posições do orbe amarelo
    pilar1_amarelo = 0
    pilar2_amarelo = 0
    pilar3_amarelo = 0
    pilar4_amarelo = 0
    pilar5_amarelo = 0

    # em relação as possíveis posições do orbe vermelho
    pilar1_vermelho = 0
    pilar2_vermelho = 0
    pilar3_vermelho = 0
    pilar4_vermelho = 0
    pilar5_vermelho = 0

    # em relação as possíveis posições do orbe laranja
    pilar1_laranja = 0
    pilar2_laranja = 0
    pilar3_laranja = 0
    pilar4_laranja = 0
    pilar5_laranja = 0

    # em relação as possíveis posições do orbe verde
    pilar1_verde = 0
    pilar2_verde = 0
    pilar3_verde = 0
    pilar4_verde = 0
    pilar5_verde = 0

    # em relação as possíveis posições do orbe azul
    pilar1_azul = 0
    pilar2_azul = 0
    pilar3_azul = 0
    pilar4_azul = 0
    pilar5_azul = 0

    # contador pra resetar a sequência, se as posições estiverem erradas
    contando = 0 

    run_unlock = True
    toca_unlock = False
    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level3_9.draw()

        while toca_unlock == True and run_unlock == True:
            orb_unlock_sfx.play()
            run_unlock = False
            break

        if contando == 5:
            if ordem == 5:
                statue1.hide()
                toca_unlock = True
            else:
                ordem = 0
                contando = 0
                # resetando todo mundo
                # em relação as possíveis posições do orbe amarelo
                pilar1_amarelo = 0
                pilar2_amarelo = 0
                pilar3_amarelo = 0
                pilar4_amarelo = 0
                pilar5_amarelo = 0

                # em relação as possíveis posições do orbe vermelho
                pilar1_vermelho = 0
                pilar2_vermelho = 0
                pilar3_vermelho = 0
                pilar4_vermelho = 0
                pilar5_vermelho = 0

                # em relação as possíveis posições do orbe laranja
                pilar1_laranja = 0
                pilar2_laranja = 0
                pilar3_laranja = 0
                pilar4_laranja = 0
                pilar5_laranja = 0

                # em relação as possíveis posições do orbe verde
                pilar1_verde = 0
                pilar2_verde = 0
                pilar3_verde = 0
                pilar4_verde = 0
                pilar5_verde = 0

                # em relação as possíveis posições do orbe azul
                pilar1_azul = 0
                pilar2_azul = 0
                pilar3_azul = 0
                pilar4_azul = 0
                pilar5_azul = 0

                # geral
                escolhendo = 0

                # amarelo
                escolhido_amarelo = False
                escolher_amarelo = False

                # vermelho
                escolhido_vermelho = False
                escolher_vermelho = False

                # laranja
                escolhido_laranja = False
                escolher_laranja = False

                # verde
                escolhido_verde = False
                escolher_verde = False

                # azul
                escolhido_azul = False
                escolher_azul = False

                # orbes
                orbe_vermelho.set_position((janela.width/2 - orbe_vermelho.width/2)-170, (janela.height/2 - orbe_vermelho.height/2)+263)

                orbe_laranja.set_position((janela.width/2 - orbe_laranja.width/2)-80, (janela.height/2 - orbe_laranja.height/2)+263)

                orbe_amarelo.set_position((janela.width/2 - orbe_amarelo.width/2)-265, (janela.height/2 - orbe_amarelo.height/2)+263)

                orbe_verde.set_position((janela.width/2 - orbe_verde.width/2)+10, (janela.height/2 - orbe_verde.height/2)+263)

                orbe_azul.set_position((janela.width/2 - orbe_azul.width/2)+100, (janela.height/2 - orbe_azul.height/2)+263)
                ordem_errada_sfx.play()

        # puzzel dos orbes
        if escolher_vermelho == False:
            orbe_vermelho.draw()
            orbe_vermelho.update()

        if escolher_laranja == False:
            orbe_laranja.draw()
            orbe_laranja.update()

        if escolher_amarelo == False:
            orbe_amarelo.draw()
            orbe_amarelo.update()

        if escolher_verde == False:
            orbe_verde.draw()
            orbe_verde.update()

        if escolher_azul == False:
            orbe_azul.draw()
            orbe_azul.update()

        # escolhendo a posição dos orbes

        # escolher a posição do orbe amarelo
        if escolher_amarelo == True:

            if mouse.is_over_object(pilar_object1) and pilar1_vermelho == 0 and pilar1_laranja == 0 and pilar1_verde == 0 and pilar1_azul == 0:
                hand1.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_amarelo = False
                    orbe_amarelo.set_position(pilar1_x, pilar1_y)
                    escolhido_amarelo = True
                    pilar1_amarelo = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object2) and pilar2_vermelho == 0 and pilar2_laranja == 0 and pilar2_verde == 0 and pilar2_azul == 0:
                hand2.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_amarelo = False
                    orbe_amarelo.set_position(pilar2_x, pilar2_y)
                    escolhido_amarelo = True
                    pilar2_amarelo = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object3) and pilar3_vermelho == 0 and pilar3_laranja == 0 and pilar3_verde == 0 and pilar3_azul == 0:
                hand3.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_amarelo = False
                    ordem += 1
                    orbe_amarelo.set_position(pilar3_x, pilar3_y)
                    escolhido_amarelo = True
                    pilar3_amarelo = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object4) and pilar4_vermelho == 0 and pilar4_laranja == 0 and pilar4_verde == 0 and pilar4_azul == 0:
                hand4.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_amarelo = False
                    orbe_amarelo.set_position(pilar4_x, pilar4_y)
                    escolhido_amarelo = True
                    pilar4_amarelo = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object5) and pilar5_vermelho == 0 and pilar5_laranja == 0 and pilar5_verde == 0 and pilar5_azul == 0:
                hand5.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_amarelo = False
                    orbe_amarelo.set_position(pilar5_x, pilar5_y)
                    escolhido_amarelo = True
                    pilar5_amarelo = 1
                    contando += 1
                    orb_sfx.play()

        # escolher a posição do orbe vermelho
        if escolher_vermelho == True:

            if mouse.is_over_object(pilar_object1) and pilar1_amarelo == 0 and pilar1_laranja == 0 and pilar1_verde == 0 and pilar1_azul == 0:
                hand1.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_vermelho = False
                    orbe_vermelho.set_position(pilar1_x, pilar1_y)
                    escolhido_vermelho = True
                    ordem += 1
                    pilar1_vermelho = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object2) and pilar2_amarelo == 0 and pilar2_laranja == 0 and pilar2_verde == 0 and pilar2_azul == 0:
                hand2.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_vermelho = False
                    orbe_vermelho.set_position(pilar2_x, pilar2_y)
                    escolhido_vermelho = True
                    pilar2_vermelho = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object3) and pilar3_amarelo == 0 and pilar3_laranja == 0 and pilar3_verde == 0 and pilar3_azul == 0:
                hand3.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_vermelho = False
                    orbe_vermelho.set_position(pilar3_x, pilar3_y)
                    escolhido_vermelho = True
                    pilar3_vermelho = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object4) and pilar4_amarelo == 0 and pilar4_laranja == 0 and pilar4_verde == 0 and pilar4_azul == 0:
                hand4.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_vermelho = False
                    orbe_vermelho.set_position(pilar4_x, pilar4_y)
                    escolhido_vermelho = True
                    pilar4_vermelho = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object5) and pilar5_amarelo == 0 and pilar5_laranja == 0 and pilar5_verde == 0 and pilar5_azul == 0:
                hand5.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_vermelho = False
                    orbe_vermelho.set_position(pilar5_x, pilar5_y)
                    escolhido_vermelho = True
                    pilar5_vermelho = 1
                    contando += 1
                    orb_sfx.play()


        # escolher a posição do orbe laranja
        if escolher_laranja == True:

            if mouse.is_over_object(pilar_object1) and pilar1_amarelo == 0 and pilar1_vermelho == 0 and pilar1_verde == 0 and pilar1_azul == 0: 
                hand1.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_laranja = False
                    orbe_laranja.set_position(pilar1_x, pilar1_y)
                    escolhido_laranja = True
                    pilar1_laranja = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object2) and pilar2_amarelo == 0 and pilar2_vermelho == 0 and pilar2_verde == 0 and pilar2_azul == 0:
                hand2.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_laranja = False
                    orbe_laranja.set_position(pilar2_x, pilar2_y)
                    escolhido_laranja = True
                    ordem += 1
                    pilar2_laranja = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object3) and pilar3_amarelo == 0 and pilar3_vermelho == 0 and pilar3_verde == 0 and pilar3_azul == 0:
                hand3.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_laranja = False
                    orbe_laranja.set_position(pilar3_x, pilar3_y)
                    escolhido_laranja = True
                    pilar3_laranja = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object4) and pilar4_amarelo == 0 and pilar4_vermelho == 0 and pilar4_verde == 0 and pilar4_azul == 0:
                hand4.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_laranja = False
                    orbe_laranja.set_position(pilar4_x, pilar4_y)
                    escolhido_laranja = True
                    pilar4_laranja = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object5) and pilar5_amarelo == 0 and pilar5_vermelho == 0 and pilar5_verde == 0 and pilar5_azul == 0:
                hand5.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_laranja = False
                    orbe_laranja.set_position(pilar5_x, pilar5_y)
                    escolhido_laranja = True
                    pilar5_laranja = 1
                    contando += 1
                    orb_sfx.play()

        # escolher a posição do orbe verde
        if escolher_verde == True:

            if mouse.is_over_object(pilar_object1) and pilar1_amarelo == 0 and pilar1_vermelho == 0 and pilar1_laranja == 0 and pilar1_azul == 0:
                hand1.draw()
                if mouse.is_button_pressed(1) and pilar1_amarelo == 0 and pilar1_vermelho == 0 and pilar1_laranja == 0 and pilar1_azul == 0:
                    escolhendo = 0
                    escolher_verde = False
                    orbe_verde.set_position(pilar1_x, pilar1_y)
                    escolhido_verde = True
                    pilar1_verde = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object2) and pilar2_amarelo == 0 and pilar2_vermelho == 0 and pilar2_laranja == 0 and pilar2_azul == 0:
                hand2.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_verde = False
                    orbe_verde.set_position(pilar2_x, pilar2_y)
                    escolhido_verde = True
                    pilar2_verde = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object3) and pilar3_amarelo == 0 and pilar3_vermelho == 0 and pilar3_laranja == 0 and pilar3_azul == 0:
                hand3.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_verde = False
                    orbe_verde.set_position(pilar3_x, pilar3_y)
                    escolhido_verde = True
                    pilar3_verde = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object4) and pilar4_amarelo == 0 and pilar4_vermelho == 0 and pilar4_laranja == 0 and pilar4_azul == 0:
                hand4.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_verde = False
                    orbe_verde.set_position(pilar4_x, pilar4_y)
                    escolhido_verde = True
                    ordem += 1
                    pilar4_verde = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object5) and pilar5_amarelo == 0 and pilar5_vermelho == 0 and pilar5_laranja == 0 and pilar5_azul == 0:
                hand5.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_verde = False
                    orbe_verde.set_position(pilar5_x, pilar5_y)
                    escolhido_verde = True
                    pilar5_verde = 1
                    contando += 1
                    orb_sfx.play()

        # escolher a posição do orbe azul
        if escolher_azul == True:

            if mouse.is_over_object(pilar_object1) and pilar1_amarelo == 0 and pilar1_vermelho == 0 and pilar1_laranja == 0 and pilar1_verde == 0:
                hand1.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_azul = False
                    orbe_azul.set_position(pilar1_x, pilar1_y)
                    escolhido_azul = True
                    pilar1_azul = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object2) and pilar2_amarelo == 0 and pilar2_vermelho == 0 and pilar2_laranja == 0 and pilar2_verde == 0:
                hand2.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_azul = False
                    orbe_azul.set_position(pilar2_x, pilar2_y)
                    escolhido_azul = True
                    pilar2_azul = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object3) and pilar3_amarelo == 0 and pilar3_vermelho == 0 and pilar3_laranja == 0 and pilar3_verde == 0:
                hand3.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_azul = False
                    orbe_azul.set_position(pilar3_x, pilar3_y)
                    escolhido_azul = True
                    pilar3_azul = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object4) and pilar4_amarelo == 0 and pilar4_vermelho == 0 and pilar4_laranja == 0 and pilar4_verde == 0:
                hand4.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_azul = False
                    orbe_azul.set_position(pilar4_x, pilar4_y)
                    escolhido_azul = True
                    pilar4_azul = 1
                    contando += 1
                    orb_sfx.play()

            if mouse.is_over_object(pilar_object5) and pilar5_amarelo == 0 and pilar5_vermelho == 0 and pilar5_laranja == 0 and pilar5_verde == 0:
                hand5.draw()
                if mouse.is_button_pressed(1):
                    escolhendo = 0
                    escolher_azul = False
                    orbe_azul.set_position(pilar5_x, pilar5_y)
                    escolhido_azul = True
                    ordem += 1
                    pilar5_azul = 1
                    contando += 1
                    orb_sfx.play()

        # interação do personagem com os orbes

        # interagindo com o orbe amarelo
        if escolher_amarelo == False and escolhido_amarelo == False:
            if idle_object.collided(orbe_amarelo_object):
                janela.draw_text("Press E to Interact", idle_object.x-70, idle_object.y-40, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    escolher_amarelo = True
                    escolhendo = 1
                    pegar_orb_sfx.play()
        
        # interagindo com o orbe vermelho
        if escolher_vermelho == False and escolhido_vermelho == False:
            if idle_object.collided(orbe_vermelho_object):
                janela.draw_text("Press E to Interact", idle_object.x-70, idle_object.y-40, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    escolher_vermelho = True
                    escolhendo = 1
                    pegar_orb_sfx.play()


        # interagindo com o orbe laranja
        if escolher_laranja == False and escolhido_laranja == False:
            if idle_object.collided(orbe_laranja_object):
                janela.draw_text("Press E to Interact", idle_object.x-70, idle_object.y-40, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    escolher_laranja = True
                    escolhendo = 1
                    pegar_orb_sfx.play()



        if escolher_verde == False and escolhido_verde == False:
            if idle_object.collided(orbe_verde_object):
                janela.draw_text("Press E to Interact", idle_object.x-70, idle_object.y-40, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    escolher_verde = True
                    escolhendo = 1
                    pegar_orb_sfx.play()


        if escolher_azul == False and escolhido_azul == False:
            if idle_object.collided(orbe_azul_object):
                janela.draw_text("Press E to Interact", idle_object.x-70, idle_object.y-40, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
                if teclado.key_pressed("E"):
                    escolher_azul = True
                    escolhendo = 1
                    pegar_orb_sfx.play()

        # dinheiro
        bolso.draw()
        gema_azul_portrait.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        gema_verde_portrait.draw()

        if idle.x >= janela.width - idle.width + 140 and ordem == 5:
            wind.stop()
            jogar_3_95(coins, barra_p, dash_got, light, heavy)
                    
        run_direita.x = run_esquerda.x = idle_esquerda.x = idle_direita.x = idle.x
        run_direita.y = run_esquerda.y = idle_esquerda.y = idle_direita.y = idle.y

        statue2.draw()

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
        if escolhendo == 0:
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
                if ordem == 5:
                    if teclado.key_pressed("D") and idle.x <= 720:
                        idle = run_direita
                        idle.x += vel_per * dt
                else:
                    if teclado.key_pressed("D") and idle.x <= 500:
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

            if idle.y <= 307:
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

                if idle.y <= 307:
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

                if idle.y <= 307:
                    # andar para baixo virado para esquerda
                    if teclado.key_pressed("S") and idle.y <= WIDTH and virado_esquerda:
                        idle = run_esquerda
                        idle.y += vel_per * dt

                moving = False

            idle_object.set_position(idle.x + 160, idle.y + 140)

        # desenhar a barra de vida do player e atualizá-la a cada hit inimigo
        if barra_p <= 3:
            vida_p[barra_p].draw()

        statue1.draw()
        statue3.draw()

        # troca dos tiros
        if barra > 3: # somente se todos os inimigos estiverem derrotados

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