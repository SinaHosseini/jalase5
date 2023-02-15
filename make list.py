n = int(input("enter arz list: "))
m = int(input("enter tol list: "))
x = 0

for tol in range(m):
    if x % 2 == 0:
        if n % 2 == 1:
            y = (n+1)/2
            for i in range(int(y)):
                print("*", end="")
                if i < y-1:
                    print("#", end="")
        elif n % 2 == 0:
            y = n / 2
            for i in range(int(y)):
                print("*", end="")
                print("#", end="")
        x += 1

    elif x % 2 == 1:
        if n % 2 == 1:
            y = (n+1)/2
            for i in range(int(y)):
                print("#", end="")
                if i < y-1:
                    print("*", end="")
        elif n % 2 == 0:
            y = n / 2
            for i in range(int(y)):
                print("#", end="")
                print("*", end="")
        x += 1
    print(end="\n")
