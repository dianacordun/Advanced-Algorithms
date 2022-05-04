def testDeOrientare(P,Q,R):
    px = P[0]
    py = P[1]
    qx = Q[0]
    qy = Q[1]
    rx = R[0]
    ry = R[1]

    det = qx*ry + rx*py + px*qy - qx*py - rx*qy - px*ry

    if det == 0:
        return 0
    elif det < 0:
        return 1
    else:
        return -1

def robot(puncte):
    stanga = 0 # nr de viraje de stanga
    dreapta = 0 # nr de viraje de dreapta
    drept = 0 # nr dr de situatii in care a ramas pe aceeasi dreapta
    for i in range(len(puncte) - 1):
        directie = testDeOrientare(puncte[i], puncte[i + 1], puncte[(i + 2) % len(puncte)])
        if directie == -1:
            stanga += 1
        if directie == 1:
            dreapta += 1
        if directie == 0:
            drept += 1
    return stanga, dreapta, drept

n = int(input())
l_puncte = []
for el in range(n):
    a = tuple(float(x) for x in input().split())
    l_puncte.append(a)
stanga, dreapta, drept = robot(l_puncte)
print(stanga, dreapta, drept)
