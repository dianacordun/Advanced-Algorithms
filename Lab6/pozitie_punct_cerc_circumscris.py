# coordonatele varfurilor triunghiului
x_a, y_a = [int(x) for x in input().split()]
x_b, y_b = [int(x) for x in input().split()]
x_c, y_c = [int(x) for x in input().split()]

def calculeaza_det(mat, total=0):
    indici = list(range(len(mat))) # lista de indici de lungimea matricei
    if len(mat) == 2 and len(mat[0]) == 2: # pt matrice de 2x2
        val = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return val

    for coloana in indici:
        mat_mica = mat
        mat_mica = mat_mica[1:]
        h = len(mat_mica)

        for i in range(h):
            mat_mica[i] = mat_mica[i][0:coloana] + mat_mica[i][coloana + 1:]

        semn = (-1) ** (coloana % 2)
        det_mic = calculeaza_det(mat_mica)
        total += semn * mat[0][coloana] * det_mic

    return total


m = int(input()) # nr de puncte ale caror pozitii relative trebuie determinate

for i in range(m):
    x_d, y_d = [int(x) for x in input().split()]
    matrice = [[x_a, y_a, x_a ** 2 + y_a ** 2, 1],
               [x_b, y_b, x_b ** 2 + y_b ** 2, 1],
               [x_c, y_c, x_c ** 2 + y_c ** 2, 1],
               [x_d, y_d, x_d ** 2 + y_d ** 2, 1]]

    determinant = calculeaza_det(matrice)

    if determinant > 0:
        print("INSIDE")
    elif determinant == 0: # punctele sunt conciclice
        print("BOUNDARY")
    else:
        print("OUTSIDE")