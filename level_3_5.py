from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from level_3_8 import *

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

def jogar_3_5(coins, barra_per, dash_got, leve, pesado, musica_level_before_loop):
    janela = Window(950, 594)
    janela.set_title("Before I Die")

    impacto = pygame.mixer.Sound("impact.wav")
    soul_sfx = pygame.mixer.Sound("cabeca_sfx.wav")
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
    level3_5 = GameImage("fundo3_1.png")

    # inputs#
    teclado = Window.get_keyboard()

    # moving variables
    moving = False
    virado_direita = True
    virado_esquerda = False
    HEIGHT = 100
    WIDTH = 358
    limite_superior = HEIGHT + 70
    vely = 280

    # attacking variables
    lista_de_tiros_direita = []
    lista_de_tiros_esquerda = []
    direita = False
    esquerda = False
    recarga = 3
    recarga_inimigo = 0
    lista_de_tiros_inimigo = []
    lista_de_tiros_inimigo2 = []
    colisao1 = 0
    colisao2 = 0
    colisao3 = 0

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

    # cabeças
    # skull 1
    # andando pra direita
    skull_direita1 = Sprite("skull_direita.png", 3)
    skull_direita1.set_total_duration(700)
    skull_direita1.set_position((janela.width/2 - skull_direita1.width/2)+400, (janela.height/2 - skull_direita1.height/2)+110)

    # andando pra esquerda
    skull_esquerda1 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup1 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup1.set_total_duration(700)
    skull_esquerda1.set_position(skull_direita1.x, skull_direita1.y)
    skull_esquerda1.set_total_duration(700)

    # object
    skull1_object = Sprite("skull_object.png")
    skull1_object.set_position(skull_esquerda1.x+30, skull_esquerda1.y+45)

    # skull1 vida
    vida1 = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = vida1[4].x = vida1[5].x = vida1[6].x = skull_esquerda1.x
    vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = vida1[4].y = vida1[5].y = vida1[6].y = skull_esquerda1.y
    barra_skull1 = 0


    # skull 2
    # andando pra direita
    skull_direita2 = Sprite("skull_direita.png", 3)
    skull_direita2.set_total_duration(700)
    skull_direita2.set_position((janela.width/2 - skull_direita2.width/2)+400, (janela.height/2 - skull_direita2.height/2))

    # andando pra esquerda
    skull_esquerda2 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup2 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup2.set_total_duration(700)
    skull_esquerda2.set_position(skull_direita2.x, skull_direita2.y)
    skull_esquerda2.set_total_duration(700)

    # object
    skull2_object = Sprite("skull_object.png")
    skull2_object.set_position(skull_esquerda2.x+30, skull_esquerda2.y+45)

    # skull2 vida
    vida2 = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = skull_esquerda2.x
    vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = skull_esquerda2.y
    barra_skull2 = 0


    # skull 3
    # andando pra direita
    skull_direita3 = Sprite("skull_direita.png", 3)
    skull_direita3.set_total_duration(700)
    skull_direita3.set_position((janela.width/2 - skull_direita3.width/2)+400, (janela.height/2 - skull_direita3.height/2)+220)

    # andando pra esquerda
    skull_esquerda3 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup3 = Sprite("skull_esquerda.png", 3)
    skull_esquerda_backup3.set_total_duration(700)
    skull_esquerda3.set_position(skull_direita3.x, skull_direita3.y)
    skull_esquerda3.set_total_duration(700)

    # object
    skull3_object = Sprite("skull_object.png")
    skull3_object.set_position(skull_esquerda3.x+30, skull_esquerda3.y+45)

    # skull3 vida
    vida3 = [Sprite("barra_cheia_red.png"), Sprite("barra_1_red.png"), Sprite("barra_2_red.png"), Sprite("barra_3_red.png"), Sprite("barra_cheia.png"), Sprite("barra_1.png"), Sprite("barra_2.png"), Sprite("barra_3.png")]
    vida3[0].x = vida3[1].x = vida3[2].x = vida3[3].x = vida3[4].x = vida3[5].x = vida3[6].x = skull_esquerda3.x
    vida3[0].y = vida3[1].y = vida3[2].y = vida3[3].y = vida3[4].y = vida3[5].y = vida3[6].y = skull_esquerda3.y
    barra_skull3 = 0


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
    
    # dragao
    dragon = Sprite("dragon.png", 3)
    dragon.set_total_duration(800)
    dragon.set_position((janela.width/2 - dragon.width/2)+300, (janela.height/2 - dragon.height/2)+70)

    # fire trap 1
    fire_trap = Sprite("fire_trap.png", 14)
    fire_trap.set_total_duration(1600)
    fire_trap.set_position((janela.width/2 - fire_trap.width/2), (janela.height/2 - fire_trap.height/2)+5)

    # fire trap 2
    fire_trap2 = Sprite("fire_trap.png", 14)
    fire_trap2.set_total_duration(1600)
    fire_trap2.set_position((janela.width/2 - fire_trap.width/2)+300, (janela.height/2 - fire_trap.height/2)+5)

    # fire trap 3
    fire_trap3 = Sprite("fire_trap.png", 14)
    fire_trap3.set_total_duration(1600)
    fire_trap3.set_position((janela.width/2 - fire_trap.width/2)-300, (janela.height/2 - fire_trap.height/2)+5)

    # fire trap 4
    fire_trap4 = Sprite("fire_trap.png", 14)
    fire_trap4.set_total_duration(1600)
    fire_trap4.set_position((janela.width/2 - fire_trap.width/2), (janela.height - fire_trap.height)-15)

    # fire trap 5
    fire_trap5 = Sprite("fire_trap.png", 14)
    fire_trap5.set_total_duration(1600)
    fire_trap5.set_position((janela.width/2 - fire_trap.width/2)+300, (janela.height - fire_trap.height)-15)

    # fire trap 6
    fire_trap6 = Sprite("fire_trap.png", 14)
    fire_trap6.set_total_duration(1600)
    fire_trap6.set_position((janela.width/2 - fire_trap.width/2)-300, (janela.height - fire_trap.height)-15)

    fire_trap_object1 = Sprite("trap_object.png")
    fire_trap_object1.set_position(fire_trap.x+5, fire_trap.y+28)

    fire_trap_object2 = Sprite("trap_object.png")
    fire_trap_object2.set_position(fire_trap2.x+5, fire_trap2.y+28)

    fire_trap_object3 = Sprite("trap_object.png")
    fire_trap_object3.set_position(fire_trap3.x+5, fire_trap3.y+28)

    fire_trap_object4 = Sprite("trap_object.png")
    fire_trap_object4.set_position(fire_trap4.x+5, fire_trap4.y+28)

    fire_trap_object5 = Sprite("trap_object.png")
    fire_trap_object5.set_position(fire_trap5.x+5, fire_trap5.y+28)   

    fire_trap_object6 = Sprite("trap_object.png")
    fire_trap_object6.set_position(fire_trap6.x+5, fire_trap6.y+28) 

    trap_timer = 0

    while True:
        janela.set_background_color("BLACK")
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        level3_5.draw()

        # armadilhas
        fire_trap.draw()
        fire_trap.update()

        fire_trap2.draw()
        fire_trap2.update()

        fire_trap3.draw()
        fire_trap3.update()

        fire_trap4.draw()
        fire_trap4.update()

        fire_trap5.draw()
        fire_trap5.update()

        fire_trap6.draw()
        fire_trap6.update()
        trap_timer += janela.delta_time()

        if trap_timer > 1:
            if idle_object.collided(fire_trap_object1):
                barra_p += 1
                hurt.play()

            if idle_object.collided(fire_trap_object2):
                barra_p += 1
                hurt.play()

            if idle_object.collided(fire_trap_object3):
                barra_p += 1
                hurt.play()

            if idle_object.collided(fire_trap_object4):
                barra_p += 1
                hurt.play()

            if idle_object.collided(fire_trap_object5):
                barra_p += 1
                hurt.play()

            if idle_object.collided(fire_trap_object6):
                barra_p += 1
                hurt.play()
            trap_timer = 0

        if fire_trap.curr_frame == 0:
            trap_timer = 0

        #dragon.draw()
        #dragon.update()

        # dinheiro
        bolso.draw()
        gema_azul_portrait.draw()
        janela.draw_text(str(coins), 100, 530, size=30, color=(0, 255, 0), font_name="Arial", bold=True, italic=False)
        gema_verde_portrait.draw()

        # skull 1
        skull1_object.set_position(skull_esquerda1.x+30, skull_esquerda1.y+45)
        skull_direita1.x = skull_esquerda1.x
        skull_direita1.y = skull_esquerda1.y
        vida1[0].x = vida1[1].x = vida1[2].x = vida1[3].x = vida1[4].x = vida1[5].x = vida1[6].x = skull_esquerda1.x+3
        vida1[0].y = vida1[1].y = vida1[2].y = vida1[3].y = vida1[4].y = vida1[5].y = vida1[6].y = skull_esquerda1.y+6      

        # skull 2
        skull2_object.set_position(skull_esquerda2.x+30, skull_esquerda2.y+45)
        skull_direita2.x = skull_esquerda2.x
        skull_direita2.y = skull_esquerda2.y
        vida2[0].x = vida2[1].x = vida2[2].x = vida2[3].x = vida2[4].x = vida2[5].x = vida2[6].x = skull_esquerda2.x+3
        vida2[0].y = vida2[1].y = vida2[2].y = vida2[3].y = vida2[4].y = vida2[5].y = vida2[6].y = skull_esquerda2.y+6  

        # skull 3
        skull3_object.set_position(skull_esquerda3.x+30, skull_esquerda3.y+45)
        skull_direita3.x = skull_esquerda3.x
        skull_direita3.y = skull_esquerda3.y
        vida3[0].x = vida3[1].x = vida3[2].x = vida3[3].x = vida3[4].x = vida3[5].x = vida3[6].x = skull_esquerda3.x+3
        vida3[0].y = vida3[1].y = vida3[2].y = vida3[3].y = vida3[4].y = vida3[5].y = vida3[6].y = skull_esquerda3.y+6  

        if idle.x >= janela.width - idle.width + 140:
            jogar_3_8(coins, barra_p, dash_got, light, heavy, musica_level_before_loop)
                    
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
                if barra_skull1 <= 3:
                    if d.collided(skull1_object) and d in lista_de_tiros_direita:
                        if barra_skull1 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull1 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull1 += 2
                        lista_de_tiros_direita.remove(d)

                if barra_skull2 <= 3:
                    if d.collided(skull2_object) and d in lista_de_tiros_direita:
                        if barra_skull2 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull2 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull2 += 2
                        lista_de_tiros_direita.remove(d)

                if barra_skull3 <= 3:
                    if d.collided(skull3_object) and d in lista_de_tiros_direita:
                        if barra_skull3 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull3 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull3 += 2
                        lista_de_tiros_direita.remove(d)

        if lista_de_tiros_esquerda != [] and esquerda: #esquerda
            for d in lista_de_tiros_esquerda:
                d.draw()
                d.update()
                d.x -= 200 * janela.delta_time()
                if barra_skull1 <= 3:
                    if d.collided(skull1_object) and d in lista_de_tiros_esquerda:
                        if barra_skull1 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull1 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull1 += 2
                        lista_de_tiros_esquerda.remove(d)

                if barra_skull2 <= 3:
                    if d.collided(skull2_object) and d in lista_de_tiros_esquerda:
                        if barra_skull2 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull2 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull2 += 2
                        lista_de_tiros_esquerda.remove(d)

                if barra_skull3 <= 3:
                    if d.collided(skull3_object) and d in lista_de_tiros_esquerda:
                        if barra_skull3 == 3:
                            soul_sfx.play()
                        impacto.play()
                        if light == 1 and heavy == 0:
                            barra_skull3 += 1
                        elif light == 0 and heavy == 1:
                            barra_skull3 += 2
                        lista_de_tiros_esquerda.remove(d)

        if lista_de_tiros_esquerda == []:
            esquerda = False

        if lista_de_tiros_direita == []:
            direita = False

        recarga += janela.delta_time()

        # IA da skull 1
        if barra_skull1 <= 3:
            vida1[barra_skull1].draw()
            skull_esquerda1.draw()
            skull_esquerda1.update()
            skull_esquerda_backup1.x = skull_esquerda1.x
            skull_esquerda_backup1.y = skull_esquerda1.y
            # deixar a skull sempre virado pro personagem
            if idle_object.x > skull1_object.x and idle_object.x - skull1_object.x > 10:
                skull_esquerda1 = skull_direita1
            if idle_object.x < skull1_object.x and skull1_object.x - idle_object.x > 10:
                skull_esquerda1 = skull_esquerda_backup1

            # perseguição da skull pelo personagem
            # eixo x
            if idle_object.x < skull1_object.x:
                skull_esquerda1.x -= 1 * dt
            elif idle_object.x > skull1_object.x:
                skull_esquerda1.x += 1 * dt

            # eixo y
            if idle_object.y < skull1_object.y:
                skull_esquerda1.y -= 1 * dt
            elif idle_object.y > skull1_object.y:
                skull_esquerda1.y += 1 * dt

            # colisão da skull 1 com o personagem
            while colisao1 == 0:
                if skull1_object.collided(idle_object):
                    hurt.play()
                    barra_p += 1
                    colisao1 = 1
                    barra_skull1 = 4
                break
        
        # IA da skull 2
        if barra_skull2 <= 3:
            vida2[barra_skull2].draw()
            skull_esquerda2.draw()
            skull_esquerda2.update()
            skull_esquerda_backup2.x = skull_esquerda2.x
            skull_esquerda_backup2.y = skull_esquerda2.y
            # deixar a skull sempre virado pro personagem
            if idle_object.x > skull2_object.x and idle_object.x - skull2_object.x > 10:
                skull_esquerda2 = skull_direita2
            if idle_object.x < skull2_object.x and skull2_object.x - idle_object.x > 10:
                skull_esquerda2 = skull_esquerda_backup2

            # perseguição da skull pelo personagem
            # eixo x
            if idle_object.x < skull1_object.x:
                if barra_skull1 > 3:
                    skull_esquerda2.x -= 1 * dt
                else:
                    skull_esquerda2.x -= 0.8 * dt

            elif idle_object.x > skull1_object.x:
                if barra_skull1 > 3:
                    skull_esquerda2.x += 1 * dt
                else:
                    skull_esquerda2.x += 0.8 * dt

            # eixo y
            if idle_object.y < skull2_object.y:
                if barra_skull1 > 3:
                    skull_esquerda2.y -= 1 * dt
                else:
                    skull_esquerda2.y -= 0.8 * dt

            elif idle_object.y > skull2_object.y:
                if barra_skull1 > 3:
                    skull_esquerda2.y += 1 * dt
                else:
                    skull_esquerda2.y += 0.8 * dt

            # colisão da skull 1 com o personagem
            while colisao2 == 0:
                if skull2_object.collided(idle_object):
                    hurt.play()
                    barra_p += 1
                    colisao2 = 1
                    barra_skull2 = 4
                break

        # IA da skull 3
        if barra_skull3 <= 3:
            vida3[barra_skull3].draw()
            skull_esquerda3.draw()
            skull_esquerda3.update()
            skull_esquerda_backup3.x = skull_esquerda3.x
            skull_esquerda_backup3.y = skull_esquerda3.y
            # deixar a skull sempre virado pro personagem
            if idle_object.x > skull3_object.x and idle_object.x - skull3_object.x > 10:
                skull_esquerda3 = skull_direita3
            if idle_object.x < skull3_object.x and skull3_object.x - idle_object.x > 10:
                skull_esquerda3 = skull_esquerda_backup3

            # perseguição da skull pelo personagem
            # eixo x
            if idle_object.x < skull3_object.x:
                if barra_skull2 > 3:
                    skull_esquerda3.x -= 1.5 * dt
                else:
                    skull_esquerda3.x -= 0.6 * dt

            elif idle_object.x > skull3_object.x:
                if barra_skull2 > 3:
                    skull_esquerda3.x += 1.5 * dt
                else:
                    skull_esquerda3.x += 0.6 * dt

            # eixo y
            if idle_object.y < skull3_object.y:
                if barra_skull2 > 3:
                    skull_esquerda3.y -= 1.5 * dt
                else:
                    skull_esquerda3.y -= 0.6 * dt

            elif idle_object.y > skull3_object.y:
                if barra_skull2 > 3:
                    skull_esquerda3.y += 1.5 * dt
                else:
                    skull_esquerda3.y += 0.6 * dt

            # colisão da skull 1 com o personagem
            while colisao3 == 0:
                if skull3_object.collided(idle_object):
                    hurt.play()
                    barra_p += 1
                    colisao3 = 1
                    barra_skull3 = 4
                break

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

        # troca dos tiros
        if barra_skull1 > 3 and barra_skull2 > 3 and barra_skull3 > 3: # somente se todos os inimigos estiverem derrotados

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
