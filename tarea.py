numeroIf = input("Ingrese un número ")

if int(numeroIf) < 0:
    print("El número que hes ingresado es negativo")
elif int(numeroIf) > 0:
    print("El número que has ingresado es negativo")
else:
    print("Has marcado el cero")

numeroWhile = 0

while int(numeroWhile) < 3:
    print(numeroWhile)
    numeroWhile += 1

numeroFor = 3

for x in range(numeroFor):
    numeroFor -= 1
    print(numeroFor)

estacion = "VERANO"

if estacion == "INVIERNO":
    print(" es invierno")
elif estacion == "OTOÑO":
    print(" es otoño")
elif estacion == "PRIMAVERA":
    print(" es primavera")
else:
    print("es verano")
