def testDeOrientare(P,Q,R):
    px = P[0]
    py = P[1]
    qx = Q[0]
    qy = Q[1]
    rx = R[0]
    ry = R[1]

    det = qx*ry + rx*py + px*qy - qx*py - rx*qy - px*ry

    if det == 0:
        print("TOUCH")
    elif det < 0:
        print("RIGHT")
    else:
        print("LEFT")

t = int(input())
for el in range(t):
    l = [int(x) for x in input().split()]
    P = (l[0], l[1])
    Q = (l[2], l[3])
    R = (l[4], l[5])
    testDeOrientare(P,Q,R)