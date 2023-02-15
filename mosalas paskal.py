from math import factorial

n = int(input("enter tol mosalas paskal: "))
for i in range(n): 
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    print(end="\n")