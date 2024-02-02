#Función fibonacci:
# Esta función genera los primeros n términos de la secuencia Fibonacci.
# Parámetros:
#   - n: El número de términos de la secuencia Fibonacci que se desea generar.
# Retorna:
#   - Una lista que contiene los primeros n términos de la secuencia Fibonacci.
def fibonacci(n):
    # Inicia la secuencia Fibonacci con los primeros dos términos: 0 y 1.
    fib_sequence = [0, 1]
    # Mientras la longitud de la secuencia sea menor que n, se añade el siguiente término
    # sumando los dos últimos términos y agregándolo a la secuencia.
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    # Retorna la secuencia Fibonacci generada.
    return fib_sequence

# Solicita al usuario que ingrese el número de términos de la secuencia Fibonacci que desea generar.
n = int(input("Ingresa el número de términos de la secuencia Fibonacci que deseas generar: "))

# Llama a la función fibonacci con el número ingresado por el usuario y imprime el resultado.
print(fibonacci(n))