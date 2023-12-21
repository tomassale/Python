from random import randint

nombre = input('Ingrese su nombre: ')

intentos = 0
aleatorio = randint(1,100)

print(f'\nBueno {nombre} pense un numero del 1 al 100\nTenes 8 vidas, lo podras lograr?\n')
print(aleatorio)

while intentos < 8:
  numero = int(input('Ingrese un numero del 1 al 100: '))
  intentos += 1
  if(numero not in range(1,101)):
    print('Numero invalido\n')
  elif(numero < aleatorio):
    print('Intente un numero mas grande\n')
  elif(numero > aleatorio):
    print('Intente un numero mas chico\n')
  else:
    print(f'FELICIDADES {nombre.upper()} GANASTE CON EL NUMERO {aleatorio} CON {8 - intentos} VIDAS RESTANTES!!!')
    break
  print(f'Te quedan {8 - intentos} vidas')

if numero != aleatorio:
    print(f'Te quedaste sin vidas, el numero era {aleatorio} vuelve a empezar')