jadval_zarb = []
n = int(input("enter arz: "))
m = int(input("enter tol: "))

for i in range(n):
    n_l = []
    for j in range(m):
        n_l.append((i+1)*(j+1))
    jadval_zarb.append(n_l)
    print(jadval_zarb[i], end="\n")
