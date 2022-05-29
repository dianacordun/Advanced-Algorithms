def intersectie_semiplane(sp, punct):
    x_max, y_max = 9999999999, 9999999999
    x_min, y_min = -9999999999, -9999999999

    for el in sp:
        if el[0] == 0:  # vertical
            if el[2] + el[1] * punct[1] >= 0:
                continue
        else:  # horizontal
            if el[2] + el[0] * punct[0] >= 0:
                continue
        if el[0] == 0:  # vertical
            if -1 * el[2] / el[1] < punct[1]:
                y_min = max(y_min, -1 * el[2] / el[1])
            else:
                y_max = min(y_max, -1 * el[2] / el[1])
        else:  # horizontal
            if -1 * el[2] / el[0] < punct[0]:
                x_min = max(x_min, -1 * el[2] / el[0])
            else:
                x_max = min(x_max, -1 * el[2] / el[0])

    if x_max == 9999999999 or y_max == 9999999999 or x_min == -9999999999 or y_min == -9999999999:
        return 0

    return (x_max - x_min) * (y_max - y_min)  # surface


l_sp = []

n = int(input())
for _ in range(n):
    linie = [int(x) for x in input().split()]
    semiplan = (linie[0], linie[1], linie[2])
    l_sp.append(semiplan)

m = int(input())
for _ in range(m):
    linie = [float(x) for x in input().split()]
    punct = (linie[0], linie[1])
    x = intersectie_semiplane(l_sp, punct)
    if x == 0:
        print("NO")
    else:
        print("YES")
        print(x)
