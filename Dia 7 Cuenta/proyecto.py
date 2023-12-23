#from ABC import abstract
from os import system
import random

#Clase padre
class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
  
#Clase hija
class Cliente(Persona):
  def __init__(self, nombre, apellido):
    super().__init__(nombre, apellido)
    self.numero_cuenta = random.randint(1, 10000)
    self.balance = 0
  
  #Mostrar en consola cuando se la llame
  def __str__(self):
    return f'{self.nombre} {self.apellido}\nCliente: #{int(self.numero_cuenta)}\nBalance: ${int(self.balance)}'
  
  #Deposito de plata
  def depositar(self):
    deposito = int(input('¿Cuanto desea depositar en su cuenta?: '))
    while deposito < 0:
      deposito = int(input('Seleccione un numero positivo: '))
    else:
      self.balance += deposito
      return ejecucion()

  #Retiro de plata
  def retirar(self):
    retiro = int(input('¿Cuanto desea retirar de su cuenta?: '))
    while self.balance < retiro:
      retiro = int(input('Balance insuficiente, seleccione menos: '))
    else: 
      self.balance -= retiro
      return ejecucion()
  
#Funcion para crear Cliente
def crear_usuario():
  system('cls')
  print('-' * 42)
  print('\tBienvenido a BankingAcc')
  print('-' * 42)
  nombre = str(input('Ingrese su nombre: '))
  apellido = str(input('Ingrese su apellido: '))
  return Cliente(nombre, apellido)

#Inicio del programa
def ejecucion():
  system('cls')
  print('-' * 42)
  print('\tBienvenido a BankingAcc')
  print('-' * 42)
  print(cliente)
  print('-' * 42)
  print('''
    [1] Depositar
    [2] Retirar
    [3] Salir
  ''')
  print('-' * 42)
  eleccion = int(input('Seleccione su opcion: '))
  while eleccion > 3 and eleccion < 1:
    return ejecucion()
  else:
    match eleccion:
      case 1:
        cliente.depositar()
      case 2:
        cliente.retirar()
      case 3:
        system('cls')
        print('Gracias vuelva prontos!!')
  return eleccion

cliente = crear_usuario()

if __name__ == '__main__':
  ejecucion()