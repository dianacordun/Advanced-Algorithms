# Travelling salesman problem
# Problema NP-hard
from math import sqrt

# 1
def citire(nume_fisier):
    orase = []
    with open(nume_fisier) as fisier:
        for item in fisier:
            x, y = [int(el) for el in item.split()]
            orase.append((x, y))
    return orase

orase = citire("orase.in")
print(orase)

#2
def dist_euclidiana(o1, o2):
    return round(sqrt((o2[0] - o1[0])**2 + (o2[1] - o1[1])**2), 2)

#print(dist_euclidiana(orase[0],orase[1]))

#3
# graf = [(o1,o2,d)], graf neorientat
# trb sa fac dist dintre oricare 2 orase
def graf_orase(orase):
    n = len(orase)
    graf = [[0] * n for i in range(n)]

    # graf este o matrice de distante
    for i in range(n):
        for j in range(n):
            if graf[i][j] == 0 and i != j:
                graf[i][j] = dist_euclidiana(orase[i],orase[j])
                graf[j][i] = dist_euclidiana(orase[i],orase[j])
    print(graf)
    return graf


graf = graf_orase(orase)

#4
# timp: O(n!)
solutie = []
# cost = costul solutiei curente
# costul minim gsit
def tsp_bf(graf, viz, pozCurenta, n, nr, cost):

    if nr == n and graf[pozCurenta][0]: #daca am ajuns la ultimul nod si este legat de nodul de start
        solutie.append(cost + graf[pozCurenta][0])
        return

    for i in range(n):
        #Daca este nevizitat si am drum intre orasul selectat si cel la care ma aflu acum
        if viz[i] == False and graf[pozCurenta][i]:
            viz[i] = True
            #costul creste cu distanta dintre cei doi
            tsp_bf(graf, viz, i, n, nr + 1, cost + graf[pozCurenta][i])
            viz[i] = False

n = len(graf) #nr de noduri
viz = [False for i in range(n)]
viz[0] = True #pornim din primul nod, il marcam ca fiind vizitat

tsp_bf(graf, viz, 0, n, 1, 0)

print(min(solutie))
