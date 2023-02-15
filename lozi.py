adad = int(input("enter tol lozi: "))

for i in range(adad):
    print(" " * (adad - i), "* " * (i))

for i in range(adad - 2, -1, -1):
    print(" " * (adad - i), "* " * (i))
