from NodoD import Nodo

e = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    head = Nodo()
    curr = head
    i = 0
    while i < len(e):
        curr.val = e[i]
        curr.next = Nodo()
        curr.next.prev = curr  # El prev que definimos en clases
        curr = curr.next
        i += 1

    # En esta parte se imprimiran los datos de la lista e
    temp = head
    while temp:
        print(temp)
        temp = temp.next

    # Desdepus se imprimen los datos pero ahora de reversa
temp = head
while temp.next:
    temp = temp.next

while temp:
        print(temp)
        temp = temp.prev