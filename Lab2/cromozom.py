# 1

class cromozom:
    def __init__(self, a, b, n, lista = None):
        self.a = a
        self.b = b
        self.n = n
        self.precizie = (b-a)/(pow(2, n))
        if(lista == None):
            self.lista = [0 for i in range(self.n)]
        else:
            self.lista = lista

    # 2
    def base_10(self):
        putere = 1
        nr = 0
        for i in range(len(self.lista) - 1, -1, -1):
            nr += putere * self.lista[i]
            putere *= 2
        nr *= self.precizie
        nr += self.a
        return nr

#3
l1 = [0,0,0,0]
l2 = [0,0,1,1]
c1 = cromozom(3,6,4,l1)
c2 = cromozom(3,6,4,l2)
print(c1.base_10())
c2.base_10()

