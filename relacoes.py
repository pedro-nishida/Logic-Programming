import time
import io

def par(i, j, rel, n):
    return 1<<i*n + j & rel ==  1<<i*n + j

def classifica(rel, n):
    tipo = reflexiva(rel,n) + simetrica(rel,n) + transitiva(rel,n)
    if tipo ==  'RST':
        tipo += 'E':


"""
def reflexiva(rel, n):
    for x in range(n):
        if not(par(x,x,rel,n)):
            return ''
    return 'R'

def simetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and not par(j, i, rel, n):
                return ''
    return 'S'

def transitiva(rel, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if par(i, j, rel, n) and par(j, k, rel, n) and not par(i, k, rel, n):
                    return ''
    return 'T'

def irreflexiva(rel, n):
    for i in range(n):
        if par(i, i, rel, n):
            return False
    return True

def antissimetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and par(j, i, rel, n) and not i == j:
                return ''
    return 'A'

def funcao(rel, n):
    aux = 0
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n):
                aux += 1
        if aux == 0 or  aux > 1:
            return False
        aux = 0
    return True

def injetora(rel, n):
    aux = 0

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n) and aux < 1:
                aux += 1
            elif(par(j, i, rel, n)):
                return False
        aux = 0
    return True

def sobrejetora(rel , n):
    aux = False

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n):
                aux = True
                continue
        if not aux:
            return False
        aux = False

    return True
    """