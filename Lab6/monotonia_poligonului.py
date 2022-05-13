n = int(input())
l_puncte = []

for i in range(n):
    x, y = [int(x) for x in input().split()]
    l_puncte.append((x, y))

# axa = 0 pt X, 1 pt Y
# verific 2 cate 2 punctele daca au x-rile sau y-urile in ordine
# daca sunt egale, primul pct trebuie sa fie citit inaintea celui de-al doilea
def monotonie(puncte, i, j, axa):
    if puncte[i][axa] < puncte[j][axa]:
        return True
    if puncte[i][axa] == puncte[j][axa] and i < j:
        return True
    return False

flagx = 0
for i in range(n):
    if monotonie(l_puncte, i, (i + 1) % n, 0) and monotonie(l_puncte, i, i - 1, 0):
        flagx += 1

flagy = 0
for i in range(n):
    if monotonie(l_puncte, i, (i + 1) % n, 1) and monotonie(l_puncte, i, i - 1, 1):
        flagy += 1

if flagx == 1:
    print("YES")
else:
    print("NO")

if flagy == 1:
    print("YES")
else:
    print("NO")
