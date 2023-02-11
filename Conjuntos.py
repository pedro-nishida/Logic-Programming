def produto_cartesiano(conj): #Conjunto AxA
    resultado = []
    for i in conj:
        for j in conj:
            resultado += [[i,j]]
    return resultado

def partes_de_conj(p, n):
  r = []
  for aux in range(2**(len(p))):
    r.append([])
    i = 0
    while(len(p) > i):  # for i in range (len(p))
      if(aux & 2**i > 0): # Verifica se o bit tá ligado
        r[aux].append(p[i])# Caso acenda, append na relacao
        
      i += 1
    classe = classifica(aux,n)
    resultado = str(r[aux]) + classe + "\n"
    arq.write(resultado)
  return None

def par(i, j, rel, n):
    return 1<<i*n + j & rel == 1<<i*n + j

def classifica(rel, n):
    classe = ""
    if(reflexiva(rel,n)):
        classe += "- Reflexiva -"
    if(simetrica(rel, n)):
        classe += "- Simetrica -"
    if(transitiva(rel, n)):
        classe += "- Transitiva -"
    if(irreflexiva(rel, n)):
        classe += "- Irreflexiva -"
    if(antissimetrica(rel, n)):
        classe += "- Antissimetrica -"
    if "- Reflexiva -" in classe and "- Simetrica -" in classe and "- Transitiva -" in classe:
        classe += "- Equivalência -"
    if(funcao(rel, n) and rel != 0) :
        classe += "- Função -"
        if injetora(rel, n) and sobrejetora(rel, n):
            classe += "- F.Injetora e F.Sobrejetora -"
        elif injetora(rel, n):
            classe += "- F.Injetora -"
        elif sobrejetora(rel, n):
            classe += "- F.Sobrejetora -"

    
    return classe

def reflexiva(rel, n):
    for x in range(n):
        if not(par(x,x,rel,n)):
            return False
    return True

def simetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and not par(j, i, rel, n):
                return False
    return True

def transitiva(rel, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if par(i, j, rel, n) and par(j, k, rel, n) and not par(i, k, rel, n):
                    return False
    return True

def irreflexiva(rel, n):
    for i in range(n):
        if par(i, i, rel, n):
            return False
    return True

def antissimetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and par(j, i, rel, n) and not i == j:
                return False
    return True

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

arq = open("Resultado.txt", "x")
import time
antes = time.time()
r = [1,2]    
p = produto_cartesiano(r)
partes_de_conj(p,len(r))

arq.close()
depois = time.time()
print(depois - antes)
