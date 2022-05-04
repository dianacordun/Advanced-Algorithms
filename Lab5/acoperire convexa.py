def testDeOrientare(P,Q,R):
    if Q[0]*R[1] + R[0]*P[1] + P[0]*Q[1] - Q[0]*P[1] - R[0]*Q[1] - P[0]*R[1] == 0:
        return 'TOUCH'
    elif Q[0]*R[1] + R[0]*P[1] + P[0]*Q[1] - Q[0]*P[1] - R[0]*Q[1] - P[0]*R[1] < 0:
        return 'RIGHT'
    else:
        return 'LEFT'

def acoperirePartiala(l_puncte, d=False):
    if d:
        viraj = 'RIGHT'
    else:
        viraj = 'LEFT'
    l_puncte.sort(key=lambda x: [x[0], x[1]]) #sortare lexicografica
    acoperire = [l_puncte[0], l_puncte[1]] #incep cu primele 2 puncte
    for i in range(2, len(l_puncte)): #pentru fiecare punct, adaug la acoperire urmatorul punct cel mai din stanga
        acoperire.append(l_puncte[i])
        while len(acoperire) >= 3 and testDeOrientare(acoperire[-3], acoperire[-2], acoperire[-1]) != viraj:
             #cat timp acoperirea are mai mult de
             #2 puncte si ultimele 3 nu determina viraj la stanga/dreapta(in directia dorita in functie de acoperirea sup/inf)                                                                                                      #(in functie de jumatatea de acoperire)
            acoperire.remove(acoperire[-2]) #sterge penultimul punct
    return acoperire

def graham(l):
    inf = acoperirePartiala(l)
    sup = acoperirePartiala(l, True)
    #sup = sup[1:-1]  # eliminarea capetelor pt a nu avea duplicate
    sup.reverse()

    return inf + sup[1:-1] #concatenarea Ls si Li

n = int(input())
l_puncte = []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    l_puncte.append((x,y))
Conv = graham(l_puncte)
print(len(Conv))
for punct in Conv:
    print(punct[0], punct[1])