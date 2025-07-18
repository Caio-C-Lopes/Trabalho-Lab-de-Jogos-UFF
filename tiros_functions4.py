from PPlay.sprite import *
def pew_direita(player, lista, light, heavy):
    if light == 1 and heavy == 0:
        tiro = Sprite("tiro_direita.png", 5)
        tiro.set_sequence_time(0, 4, 100, True)
        tiro.x = player.x + 240
        tiro.y = player.y + 160

    if heavy == 1 and light == 0:
        tiro = Sprite("tiro_direita2.png", 6)
        tiro.set_sequence_time(0, 5, 100, True)
        tiro.x = player.x + 190
        tiro.y = player.y + 130

    lista.append(tiro)

    return lista

def pew_esquerda(player, lista, light, heavy):
    if light == 1 and heavy == 0:
        tiro = Sprite("tiro_esquerda.png", 5)
        tiro.set_sequence_time(0, 4, 100, True)

        tiro.x = player.x + 55
        tiro.y = player.y + 160
    
    if heavy == 1 and light == 0:
        tiro = Sprite("tiro_esquerda2.png", 6)
        tiro.set_sequence_time(0, 5, 100, True)
        tiro.x = player.x + 40
        tiro.y = player.y + 130
    
    lista.append(tiro)

    return lista

def pew_esquerda_inimigo(inimigo, lista): # da frente
    tiro = Sprite("soul_tiro3.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 50
    tiro.y = inimigo.y + 70

    lista.append(tiro)

    return lista

def pew_esquerda_inimigo2(inimigo, lista): # de trás
    tiro = Sprite("soul_tiro3.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 20
    tiro.y = inimigo.y + 80

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