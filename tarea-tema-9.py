class Persona():
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono


class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito


class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario


cliente = Cliente(45, "Pedro", "0414567892", 120)
trabajador = Trabajador(30, "Cheo", "598337228", 45)

print(cliente.edad, cliente.nombre, cliente.telefono, cliente.telefono)
print(trabajador.edad, trabajador.nombre,
      trabajador.telefono, trabajador.salario)
