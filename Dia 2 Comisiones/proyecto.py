#Inputs
nombre = input('¿Cual es tu nombre?: ')
venta = int(input('¿Cuanto vendiste este mes?: '))

#Logica
comision = round(venta*13/100,2)

#Resultado
print(f'Hola {nombre}, este mes vendiste {venta} y con una comision del 13% te corresponde {comision}')