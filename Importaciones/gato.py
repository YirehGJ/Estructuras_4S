from objetos import Animal

class Perro(Animal):
    def init(self, nombre):
        super().init(nombre)

    def ladrar(self):
        print('Woof')


if name == 'main':
    perro = Animal('Cookie')
    #print(perro)

    perro = Perro('Churru')
    print(perro)
    perro.ladrar()