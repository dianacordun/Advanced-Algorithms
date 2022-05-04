# Huffman Coding

# 1
#timp: O(n) - n = lungimea sirului
#spatiu: O(m) -m = nr de simboluri distincte

def citire(sir):
    d_frecv = {}
    for c in sir:
        if c in d_frecv:
            d_frecv[c] += 1
        else:
            d_frecv[c] = 1
    return d_frecv


f = open("ex2.in")
sir = f.readline()
if len(sir) == 0:
    print("Sirul introdus este gol!")
    exit(1)
vec_frecventa = citire(sir)
print(f"Frecventa simbolurilor: {vec_frecventa}")
f.close()


# 2
#timp: O(n*log n) - n = nr de caractere unice
#spatiu: O(n) - foloseste un dictionar si o lista cu maxim n obiecte + inca un dictionar pentru memorarea codurilor

# nod din arborele huffman
class nod:
    def __init__(self, frecventa, simbol, stanga=None, dreapta=None):
        self.frecventa = frecventa
        self.simbol = simbol
        self.stanga = stanga
        self.dreapta = dreapta
        self.directie = ''  # 0-stanga, 1-dreapta
        # constructor pentru nod


def calculeaza_cod(nod, val='', d_coduri= {}):
    nou_cod = val + str(nod.directie)

    if nod.stanga:
        calculeaza_cod(nod.stanga, nou_cod,d_coduri)
    if nod.dreapta:
        calculeaza_cod(nod.dreapta, nou_cod,d_coduri)

    # cazul in care nodul curent este frunza
    if not nod.stanga and not nod.dreapta:
        #retin simbolul si codul intr-un dictionar
        d_coduri[nod.simbol]= nou_cod
        #print(f"{nod.simbol} are codul {nou_cod}")
    return d_coduri

def arbore_Huffman(vec_frecventa):
    # lista de noduri
    noduri = []
    for x in vec_frecventa:
        noduri.append(nod(vec_frecventa[x], x)) #adaugam in lista toate nodurile din vectorul de frecventa

    while len(noduri) > 1:  # algoritmul se opreste cand am ramas cu un singur nod (=> am concatenat toate nodurile si am adunat toate frecventele)

        # sortarea nodurilor crescator dupa frecventa
        noduri = sorted(noduri, key=lambda x: x.frecventa)

        # aleg primele 2 cele mai mici noduri (simbolurile cu frecventa cea mai mica)
        stanga = noduri[0]
        dreapta = noduri[1]

        # le pun directii
        stanga.directie = 0
        dreapta.directie = 1

        # cream un nou nod
        # frecventa = suma frecventelor nodurilor cu frecventa cea mai mica
        # concatenam simbolurile
        # simbolurile de baza vor fi in stanga, respectiv in dreapta
        nou = nod(stanga.frecventa + dreapta.frecventa, stanga.simbol + dreapta.simbol, stanga, dreapta)

        noduri.remove(stanga)
        noduri.remove(dreapta)
        noduri.append(nou)
    return nou

radacina = arbore_Huffman(vec_frecventa)
calculeaza_cod(radacina)

# 3
# timp O(n) - n = lungimea sirului
# spatiu: O(m) - un dictionar de lungime m(nr de simboluri distincte)
def codifica_sir(sir, nod):
    dict_coduri = calculeaza_cod(nod)
    sir_nou = ''
    for c in sir:
        sir_nou = sir_nou + dict_coduri[c]
    return sir_nou

s = "aabcddd"
print(f"Sirul {s} are codificarea ", codifica_sir(s, radacina))


# 4
# timp: O(n*log m), n-nr de simboluri, m-inaltimea arborelui
# spatiu: O(1) - nu sunt folosite colectii

def decodifica_sir(sir, nod):
    sir_nou = ''
    nod_curent = nod

    for i in range(len(sir)):
        if sir[i] == '0': #cand intalnim 0, mergem in stanga
            nod_curent = nod_curent.stanga
        else:
            nod_curent = nod_curent.dreapta

        if not nod_curent.stanga and not nod_curent.dreapta:
            sir_nou = sir_nou + nod_curent.simbol
            nod_curent = nod
    return sir_nou

s2 = "1010110111000"
print(f"Sirul {s2} are decodificarea ", decodifica_sir(s2, radacina))

# 5
# Output-ul ocupa doar de doua ori mai putin spatiu

f = open("shakespeare.in")
sir = f.read()
if len(sir) == 0:
    print("Sirul introdus este gol!")
    exit(1)
vec_frecventa = citire(sir)
print(f"\nExercitiul 5.")
f.close()
radacina = arbore_Huffman(vec_frecventa)

sir_codificat = codifica_sir(sir,radacina)
decodifica_sir(sir_codificat,radacina)

print(f"Marime input: {len(sir)*8} biti / {len(sir)} bytes")
dict_Huffman = calculeaza_cod(radacina)

suma = 0
for el in vec_frecventa:
    suma += vec_frecventa[el] * len(dict_Huffman[el])

print(f"Marime output: {suma} biti / {suma//8} bytes")