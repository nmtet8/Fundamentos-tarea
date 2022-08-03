def suma(a, b, c):
    print(a + b + c)


class Coche(object):

    def __init__(self, puertas=0):

        self.puertas = puertas

    def aumentar(self):
        self.puertas += 1


miCoche = Coche(4)
print(miCoche.puertas)

miCoche.aumentar()
print(miCoche.puertas)
