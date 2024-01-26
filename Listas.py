# Nombre_de_la_variable =[]
# metodo2 = list("ABCDE")

# print (metodo2)

# for i in "cadena de caracteres":
#     print(i)

# lista = range(100) # range (a,b,c) [a,b)
# # print(list(lista)) 

# for i in lista: # for i in range(100)
#     print(i)

# x = list(range(1,11,2)) # for [int i = 1; i < 10, i +=2]    # n = 5
# #print(x)

# #for i in range(10):#para saber la cantidad de la lista length se escribe asi  range(len(x))
# for i in range(len(x)):
#     print(x[i]) #para ver el indise correspondinte se puede de esta manera  print(i, x[i])

# for i, elemnto in enumerate (x):
#     print (i, elemnto)    

# import random

# desordenada = [random.randint(1, 100) for _ in range(10)]
# print (desordenada)
# desordenada.sort() # de esta manera aremos que los random que salgan se acomoden de mas chico al mas grande   #nlog(n) -> bubbleSort n
# desordenada.sort(reverse=True)
# print(desordenada) #se vuelve a escribir el print para qver los cambios 

# otraLista = list("Marco Cordero")
# otraLista.reverse()
# elemento = otraLista[0] + otraLista[1] + otraLista[2] #Mar
# elemento = otraLista[:4]#tambien puede ser [0:4] esto solo imprime del inicio hasta el limite el limite es : despues de esto
# elemento = otraLista[4:]
# elemento = otraLista[0:-1:3]# cuando es con -numero se quiere llegar
# elemento = otraLista[::-1]#De esta manera se puede invertir un literable o una lista


# print(elemento)
# otraLista.reverse() #para voltear la lista
# print(otraLista)

# elementoVolte = ''.join(list(reversed(elemento)))
# print(elementoVolte)


# otraLista = list("Marco Cordero")
# otraLista.reverse()
# holder = ''
# for i in range(len(otraLista)):
#     holder = otraLista[i] + holder
# print(holder)#Si el print queda dentro del for te dara un tipo de piramide

lista = list(range(10))
print(lista[len(lista)-1])
print(lista)
holder = lista.pop(0)#.pp sirve para eliminar un elemento de una lista si esta vacio elimina el mas alto
print(holder)
print(lista)

listavacia = []
for i in range(50):
    listavacia.append(i+1) # Esto funciona para rellenar listas
print(listavacia)

x = [0,1,2,3,1,4,0]
x.insert(0,True)
print(x)