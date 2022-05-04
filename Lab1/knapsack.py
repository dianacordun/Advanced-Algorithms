# Fractional Knapsack Problem

# n - saci, fiecare cu tip diferit de grana
# un sac are CANTITATE (kg) si o VALOARE (lei)
# putem lua sacii intregi, sau orice procent
# maxim M kg

# 1

def citire(nume_fisier):
    f = open(nume_fisier)
    nr_saci = int(f.readline())
    l_saci = []
    for i in range(nr_saci):
        x, y = [int(x) for x in f.readline().split()]
        l_saci.append((x, y))

    cant_max = int(f.readline())
    f.close()
    return nr_saci, l_saci, cant_max

n, saci, M=citire("ex1.in")

# print(nr_saci, saci, cant_max)

# 2
# timp: O(n*log n) - n = nr de saci
# spatiu: O(n)

# saci =[(valoare,greutate)]
# maximizarea profitului => sortam crescator dupa raportul valoare/greutate

saci.sort(key=lambda x: x[0]/x[1])

selectat = 0
val = 0

while (selectat < M and len(saci)):
    # a doua conditie este pentru cazul in care cantitatea maxima permisa > pretul tuturor ghiozdanelor
    if (selectat + saci[0][1] > M): # daca nu incape intreaga cantitate in ghiozdan
        fractiune = (M - selectat) / saci[0][1]
        val += fractiune*saci[0][1]
        break
    else:
        selectat += saci[0][1]
        val += saci[0][0]
        del saci[0] # n^2


print(f"Valoarea maxima obtinuta din cele {M} kilograme este {val} lei.")

#3
"""
Metoda Greedy nu mai produce rezultate optime intrucat ar putea ramane cantitate neachizitionata.
"""



