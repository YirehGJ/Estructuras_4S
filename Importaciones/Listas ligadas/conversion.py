#import Nodo
'''Implementador'''
from Nodo import Nodo

e= [1, 2, 3, 4, 5]

if __name__ == '__main__':
    lista = list(range(1,6))
    head = Nodo()
    curr = head

    for i in e:
        curr.val = i
        curr.next = Nodo()
        curr = curr.next

    while head:
        print(head)
        head=head.next