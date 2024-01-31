def fib(n):#Definicion de la funcion Fibonacci de forma recursiva
    '''La variable n representa el termino que queremos calcular de la secuencia de Fibonacci
    en otras palabras es la posicion en la que estamos y la que buscamos.
    Ya que empezamos con posiciones "0 y 1" y debido a que hay una condicional solo los regresa
    tal cual por lo que la secuencia se empezara a ver [0,1] a partir de aqui como la siguiente
    posicion es 2 es donde se empieza a relizar las funciones recursivas.
    En el primer return la funcion se llama a si misma con el n-1 para asi darnos a entender 
    que esta calculando el numero anterior en la secuencia, despues se vuelve a llamar a si misma
    pero ahora con n-2 que con esto estaria calculando el numero dos lugares antes del que queremos
    calcular, despues de que tiene los 2 numeros realiza una suma y el producto de esta suma es la
    que se convertira en el numero en la posicion n.
    '''
    if n > 2:#
        return fib(n - 1) + fib(n - 2)
    return n

x = int(input("Ingresa un numero: "))#Se le solicita al usuario ingresar un numero que sera la posicion hasta donde llegara la funcion
#El for es una comprension de lista, que funciona solo despues de haber pasado por un if
#Las listas comprensivas forsozamente deben de pasar por un if para que se pueda en listar
t=[fib(i) for i in range(x)]#Genera una lista del tamaño proporcionado con los terminos de Fibonacci
print(t)#Imprime la lista que contiene los digitos de Fibonacci