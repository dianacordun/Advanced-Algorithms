# LCS - Longest Common Subsequences


#subsecventa, nu subsir
# elemente din sir
# o multime are 2^n partitii => un sir are tot atatea subsecvente

# 1
# timp: O(2^n)
# spatiu: O(1)

#i, j - ultimele pozitii ale sirurilor
def lcs(sir1, sir2, i, j):
    #cazul in care sirurile sunt goale
    if i == -1 or j == -1:
        return 0

    if sir1[i] == sir2[j]:
        return 1 + lcs(sir1,sir2, i-1, j-1)

    #cazul in care cele doua caractere nu se potrivesc
    return max(lcs(sir1,sir2,i-1,j), lcs(sir1,sir2, i, j-1))

sir1 = "ABCDGH"
sir2 = "AEDFHR"
i = len(sir1)
j = len(sir2)
rezultat = lcs(sir1,sir2, i - 1, j - 1)
print(rezultat) #ADH - 3


# 2
# timp: O(1)
# spatiu: O(1)
def lcs_1_1(sir1, sir2):
    if sir1 == sir2:
        return 1
    else:
        return 0

sir1 = "A"
sir2 = "A"
rezultat = lcs_1_1(sir1,sir2)
print(rezultat)

# 3
# timp: O(n) - n = lungimea celui de-al doilea sir
# spatiu: O(1)
def lcs_1_n(sir1, sir2):
    if sir1 in sir2: #verificam daca sirul de un caracter apare in celalalt
        return 1
    else:
        return 0

sir1 = "A"
sir2 = "AEDFHR"
rezultat = lcs_1_n(sir1,sir2)
print(rezultat)

# 4
# timp: O(n*m)
# spatiu: O(n*m)

def lcs_dinamic(sir1, sir2):
    n = len(sir1)
    m = len(sir2)
    L = [ [None]*(m+1) for x in range(n+1)] #+1 fata de n si m

    #L[i][j] va contine lungimea LCS-ului dintre sir1[0..i-1] si sir2[0..j-1]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0: #margine de 0-uri
                L[i][j] = 0
            elif sir1[i-1] == sir2[j - 1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1]) #maximul dintre celula din stanga si cea de deasupra

    return L[n][m]

sir1 = "AGGTAB"
sir2 = "GXTXAYB"
i = len(sir1)
j = len(sir2)
rezultat = lcs_dinamic(sir1,sir2)
print(rezultat) #4 - GTAB