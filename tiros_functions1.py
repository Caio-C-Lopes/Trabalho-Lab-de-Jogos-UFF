from PPlay.sprite import *
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

def pew_esquerda_inimigo(inimigo, lista):
    tiro = Sprite("tiro_esquerda_inimigo.png", 4)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = inimigo.x - 20
    tiro.y = inimigo.y

    lista.append(tiro)

    return lista

def pew_direita_inimigo(inimigo, lista):
    tiro = Sprite("tiro_direita_inimigo.png", 4)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = inimigo.x + 20
    tiro.y = inimigo.y

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

def pew_direita_inimigo_pequeno(inimigo, lista):
    tiro = Sprite("tiro_direita_inimigo_2.png", 4)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = inimigo.x + 40
    tiro.y = inimigo.y + 35

    lista.append(tiro)

    return lista

def pew_esquerda_inimigo_pequeno(inimigo, lista):
    tiro = Sprite("tiro_esquerda_inimigo_2.png", 4)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = inimigo.x - 40
    tiro.y = inimigo.y + 35

    lista.append(tiro)

    return lista