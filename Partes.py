#Uma relação binária R em A e B é um subconjunto de A x B,
#Uma relação binaária de R em A é um subconjunto de A x A, i.e.,
#R pertence a P(AxA) ou R está contido igual AxA
#################################################

#ATIVIDADE#
# Dado Conjunto fazer uma relação de Produto Cartesiano, Subconjuntos e sua classificação(Reflexiva,Simétrica,Transitiva)

# Exemplo
# >classifica([1,2])      #input como lista
# output: "Produto Catesiano: [[1,1],[1,2],[2,1],[2,2]]"
# output: "Partes: [[],[(1,1)],[(1,2)],[(2,1)],[(2,2),[(1,1),(1,2)],[(1,1),(1,2)],[(1,1),(2,1)],[(1,1),(2,2)],[(1,2),(2,1)],
#         [(1,2),(2,1)],[(1,2),(2,2)],[(1,1),(1,2),(2,1)],[(1,1),(1,2),(2,2)],[(1,1),(1,2),(2,2)],[(1,2),(2,1),(2,2)],
#         [(1,2),(2,1),(2,2)],[(1,1),(1,2),(2,1),(2,2)],[(1,1),(1,2),(2,2)]]

def cartesian_product(elements):
    cartesian=[]
    for first in range(len(elements)):
        for seccond in range(len(elements)):
            cartesian.append([elements[first],elements[seccond]])
    
    return cartesian

def subset(conj):
    result = [[]]
    for element in conj:
        result += [sub + [element] for sub in result]
    return result

###############################################################################

def classifica(relation, conj):
    S = reflexiva(relation,conj) +  transitiva(relation,conj) + simetrica(relation,conj)
    if "STR":
        S += "E"
    return S

def reflexiva(rel, conj):
    for elem in conj:
        if not (elem, elem) in rel:
            return ""
    return "R"

def transitiva(rel, conj):
    for a in conj:
        for b in conj:
            for c in conj:
                if (a,b) in rel and (b,c) in rel and not (a,c) in rel:
                    return ""
    return "T"

def simetrica(rel, conj):
    for a in conj:
        for b in conj:
            if (a,b) in rel and not (b,a) in rel:
                return("")
    return "S"

def main():
    cartesiano = cartesian_product([1,2])
    print(f"Produto Cartesiano: {cartesiano}\nPartes:")
    for partes in subset(cartesiano):
        print(f"{partes} classificado em {classifica(partes)}")

if __name__ == "__main__":
    main()

#########
#Formatar um arquivo