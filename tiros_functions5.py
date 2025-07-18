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

def pew_esquerda_inimigo(inimigo, lista): # dragao
    tiro = Sprite("tiro_dragon.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 60
    tiro.y = inimigo.y + 100

    lista.append(tiro)

    return lista

def pew_esquerda_inimigo2(inimigo, lista): # dragao
    tiro = Sprite("tiro_dragon.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 60
    tiro.y = inimigo.y + 130

    lista.append(tiro)

    return lista

def pew_obelisco1(inimigo, lista): # de cima
    tiro = Sprite("tiro_obelisk.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 40
    tiro.y = inimigo.y + 240
    lista.append(tiro)

    return lista

def pew_obelisco2(inimigo, lista): # de baixo
    tiro = Sprite("tiro_obelisk.png", 4)
    tiro.set_sequence_time(0, 3, 300, True)

    tiro.x = inimigo.x - 40
    tiro.y = inimigo.y + 300
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