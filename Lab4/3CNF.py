from scipy.optimize import linprog

obj= [1,1,1,1,1] # Coeficientii pt x si y

lhs_ineq = [[-1,  -1, 0, -1, 0],  [-1, 0, -1,0, -1 ], [0,-1,0, -1, -1 ]]  # Coeficientii din stanga

rhs_ineq = [-1, -1, -1]  # Coeficientii din dreapta

bnd = [(0, 1), (0, 1), (0, 1), (0, 1), (0,1)]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds= bnd, method="revised simplex")

print(opt)


l = []
for el in opt.x:
    if el > 1/3:
        l.append(True)
    else:
        l.append(False)
print(l)
print((l[0] or l[1] or l[3]) and (l[0] or l[2] or l[4]) and (l[1] or l[3] or l[4]))


