def testDeOrientare(P, Q, R):
    px = P[0]
    py = P[1]
    qx = Q[0]
    qy = Q[1]
    rx = R[0]
    ry = R[1]

    det = qx * ry + rx * py + px * qy - qx * py - rx * qy - px * ry

    if det == 0:
        return 0
    elif det > 0:
        return 1
    else:
        return -1

# citirea celor n varfuri ale poligonului
n = int(input())
l_puncte = []
for i in range(n):
    x,y = [int(x) for x in input().split()]
    l_puncte.append((x,y))
# citirea celor m puncte din plan
m = int(input())
for i in range(m):
    x,y = [int(x) for x in input().split()]
    pct = (x,y)
    ok = 1
    for j in range(1, n):
        if testDeOrientare(l_puncte[j-1],l_puncte[j],pct) == 0:
            ok = 0
            break
        elif testDeOrientare(l_puncte[j-1], l_puncte[j], pct) < 0:
            ok = -1
            break
    if testDeOrientare(l_puncte[n-1], l_puncte[0], pct) == 0:
        ok = 0
    elif testDeOrientare(l_puncte[n-1], l_puncte[0], pct) < 0:
        ok = -1
    if ok == 0:
        print("BOUNDARY")
    elif ok == 1:
        print("INSIDE")
    else:
        print("OUTSIDE")
# 2 puncte de pe acoperirea convexa + alt punct
# acoperirea convexa are doar viraje la stanga
# daca am viraj la dreapta(-1) cu pct => punct inafara poligonului
# pct se afla pe contur => n-am viraj, merge drept
# ca pct sa fie inauntru poligonului trb ca sa am viraj la stanga
# cu toate punctele de pe acoperirea convexa
# la final verificare dintre primul si ultimul punct
