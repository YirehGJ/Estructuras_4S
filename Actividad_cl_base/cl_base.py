''' Implementación de lista circular '''
from node import Node

class CircularLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

        self.counter += 1

    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        if not self.head:
            print("Lista Vacia")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.counter -= 1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        if not self.head:
            print("Lista Vacia")
            return

        current = self.head
        for _ in range(self.counter):
            print(current.val, end=" ==> ")
            current = current.next
        print()

if __name__ == '__main__':
    lista_circular = CircularLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    for item in lista_tradicional:
        lista_circular.tailInsert(item)

    # Impresión de la lista
    print("Lista Circular: ")
    lista_circular.traverse()

    # Adición de un nuevo elemento al final
    n = False
    lista_circular.tailInsert(n)
    print("Despues de añadir el ultimo elemento: ", end=" ")
    lista_circular.traverse()

    # Adición de un nuevo elemento al inicio
    n = 'Estructuras'
    lista_circular.headInsert(n)
    print("Despues de añadir el primer elemento: ", end=" ")
    lista_circular.traverse()

    # Eliminación del primer elemento e impresión
    lista_circular.headRemove()
    print("Despues de eliminar el primer elemento: ", end=" ")
    lista_circular.traverse()