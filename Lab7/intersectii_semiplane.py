def intersectie_semiplane(sp):
    x_max, y_max = 9999999999, 9999999999
    x_min, y_min = -9999999999, -9999999999

    for el in sp:  # getting the "edge" of every halfplane
        s = -9999999999
        d = 9999999999
        if el[0] == 0:  # vertical
            if el[1] < 0:
                s = -1 * el[2] / el[1]
            else:
                d = -1 * el[2] / el[1]
        else:  # horizontal
            if el[0] < 0:
                s = -1 * el[2] / el[0]
            else:
                d = -1 * el[2] / el[0]
        if el[0] == 0:  # vertical
            y_min = max(y_min, s)
            y_max = min(y_max, d)
        else:  # horizontal
            x_min = max(x_min, s)
            x_max = min(x_max, d)

    if y_min > y_max or x_min > x_max:
        return 0  # VOID
    if (x_min != -9999999999 and x_max != 9999999999) and (y_min != -9999999999 and y_max != 9999999999):
        return 1  # BOUNDED
    return 2  # UNBOUNDED


l_sp = []

n = int(input())
for i in range(n):
    linie = [int(x) for x in input().split()]
    el = (linie[0], linie[1], linie[2])
    l_sp.append(el)
if intersectie_semiplane(l_sp) == 1:
    print("BOUNDED")
elif intersectie_semiplane(l_sp) == 0:
    print("VOID")
else:
    print("UNBOUNDED")
