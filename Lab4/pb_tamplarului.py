from scipy.optimize import linprog
# minimize negative for maximize
# unde am >=, obtin <= prin *(-1)
obj = [-180, -200] # Coeficientii pt x si y

lhs_ineq = [[5,  4],  [10,  20]]  # Coeficientii din stanga

rhs_ineq = [80, 200]  # Coeficientii din dreapta

bnd = [(0, float("inf")), (0, float("inf"))]  # Bounds of x and y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")

print(opt)
print(f"Maximul functiei este {opt.x}")