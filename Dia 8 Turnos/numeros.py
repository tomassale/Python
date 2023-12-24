from os import system

# Funciones para generar numeros del 1 al 10000 en los rubros
def num_per():
  for n in range(1, 10000):
    yield f'\t   P - {n}'

def num_cos():
  for n in range(1,10000):
    yield f'\t   C - {n}'

def num_far():
  for n in range(1,10000):
    yield f'\t   F - {n}'

# Generacion de turnos
p = num_per()
f = num_far()
c = num_cos()

# Salida de turno pedido
def decorador(rubro):
  system('cls')
  print('-' * 42)
  print('\tTurno retirado')
  print('-' * 42)
  print('\tSu número es:')
  if rubro == 1:
    print(next(p))
  elif rubro == 2:
    print(next(f))
  else:
    print(next(c))
  print('-' * 42)
  print('  Aguarde y será atendido')
  print('-' * 42)