import numeros #Importacion de archivo
from os import system
import time

# Impresion de turno en consola
def sacar_turno():
  while True:
    system('cls')
    print('-' * 42)
    print('\tBienvenido a la farmacia')
    print('-' * 42)
    print('''
      [1] Perfumeria
      [2] Medicamentos
      [3] Cosmetica
    ''')
    print('-' * 42)
    try:
      pregunta = int(input('Sacar turno: '))
      if pregunta in range(1,4):
        turno = pregunta
    except ValueError:
      print('Esta no es una opcion valida')
    else:
      break
  numeros.decorador(turno)
  time.sleep(3)
  return sacar_turno()


if __name__ == '__main__':
  sacar_turno()