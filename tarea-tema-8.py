class Persona():
    def __init__(self, edad, nombre, telefono,):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_edad(self):
        print(self.edad)
        return self.edad

    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad
        print(self.edad)
        return self.edad

    def mostrar_nombre(self):
        print(self.nombre)
        return self.nombre

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(self.nombre)
        return self.nombre

    def mostrar_telefono(self):
        print(self.telefono)
        return self.telefono

    def modificar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(self.telefono)
        return self.telefono


persona = Persona(14, "Luis", "0424578241")
# print(persona.edad)

persona.mostrar_edad()
persona.modificar_edad(12)
persona.mostrar_nombre()
persona.modificar_nombre("Joaquin")
persona.mostrar_telefono()
persona.modificar_telefono("0414567892")
