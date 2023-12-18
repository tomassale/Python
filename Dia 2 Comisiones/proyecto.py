nombre = input('¿Cual es tu nombre?: ')
venta = int(input('¿Cuanto vendiste este mes?: '))
comision = round(venta*13/100,2)

print(f'Hola {nombre}, este mes vendiste {venta} y con una comision del 13% te corresponde {comision}')