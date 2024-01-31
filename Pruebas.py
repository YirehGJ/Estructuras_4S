def fact(n: int)->int:
    if(n == 0):
        return 1

    return n * fact(n - 1)
n=int(input("Ingresa un numero: "))
print(fact(5))