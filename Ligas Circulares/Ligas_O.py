from NodoT import Nodo

e = [1, 2, 3, 4, 5]
repeticiones = 100

if __name__ == '__main__':
    head = Nodo()
    curr = head
    i = 0
    while i < len(e) * repeticiones:
        curr.val = e[i % len(e)]
        if i < len(e) * repeticiones - 1:#En esta parte definimos una condicional para saber que no es el ultimo elemnto
            curr.next = Nodo()
            curr.next.prev = curr  # El prev que definimos en clases
            curr = curr.next
        else:
            # En esta parte establecemos el puntero next al primer nodo ya que es el ultimo elemento
            curr.next = head
            head.prev = curr
        i += 1

    # Imprimir el contenido de la lista circular
    temp = head
    for _ in range(len(e) * repeticiones):
        print(f'Valor del Nodo = {temp.val}')
        temp = temp.next
        if temp == head:
            break
