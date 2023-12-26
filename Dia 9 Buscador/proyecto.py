import re
import time
import os
import datetime
from pathlib import Path
import math

#Ruta a al carpeta
carpeta = Path('D:\\', 'Programacion','Practica','Python','Curso','Udemy','Dia 9 Buscador', 'Proyecto_pautas', 'Mi_Gran_Directorio')
buscador = os.walk(carpeta)

#Ejecucion en pantalla
def ejecucion():
  fecha = datetime.datetime.now().strftime("%d/%m/%Y")
  inicio = time.time()
  print('-'*33)
  print(f'Fecha de busqueda: {fecha}')
  buscador_serie(buscador)
  final = time.time()
  print(f'Duracion de la busqueda: {math.ceil(final-inicio)}')
  print('-'*33)

#Buscador de numero en serie con patron respectivo
def buscador_serie(lib):
  patron = r'N\D{3}-\d{5}'
  cantidad_obj = 0
  print('\n\tARCHIVO' + '\t'*4 + 'NRO. SERIE')
  print('-'*12+'\t\t'+'-'*10 + '\n')
  for car,sub,arc in lib:
    for obj in arc:
      path = Path(car, obj)
      res = re.findall(patron, path.read_text())
      if res != []:
        print(f'{obj}\t\t{res[0]}')
        cantidad_obj += 1
  print(f'\nNumeros encontrados: {cantidad_obj} segundos')


if __name__ == '__main__':
  ejecucion()