from os import system
from pathlib import Path

#Variables necesarias
rutas = Path('D:\\','Programacion','Practica','Python','Curso','Udemy','Dia 6 Recetario','Recetas')
recetas = {ruta.name for ruta in rutas.iterdir() if ruta.is_dir()}

#Imprimir opciones
def imprimir(name, arr):
  system('cls')
  print('-' * 42)
  print(f'\t{name}')
  print('-' * 42)
  for idx, i in enumerate(arr, start=1):
    print(f'  [{idx}] {i}')
  print('-' * 42)

#Inicio de programa
def saludo():

  system('cls')
  print('-' * 42)
  print('\tBienvenido a su recetario')
  print('-' * 42)
  print('''
    [1] Leer receta
    [2] Crear receta
    [3] Crear categoria
    [4] Borrar receta
    [5] Borrar categoria
    [6] Finalizar recetario
  ''')
  print('-' * 42)
  eleccion = int(input('Seleccione su opcion: '))
  return eleccion

#Inicio de codigo
def ejecucion():
  eleccion = saludo()
  while eleccion > 6 and eleccion < 1:
    return saludo()
  else:
    match eleccion:
      case 1:
        leer_receta()
      case 2:
        crear_receta()
      case 3:
        crear_categoria()
      case 4:
        borrar_receta()
      case 5:
        borrar_categoria()
      case 6:
        finalizar_codigo()
  return eleccion

#Opcion 1
def seleccionar_categoria():
  lista = list(recetas)
  imprimir('Recetas disponibles', recetas)
  archivo = int(input('Seleccione una categoria: '))
  if archivo <= len(recetas):
    return lista[archivo - 1]
  else:
    print("Selección no válida.")
    return None

def leer_receta():
    categoria = seleccionar_categoria()
    if categoria:
        rutario_categoria = Path(rutas, categoria)

        system('cls')
        print('-' * 42)
        print(f'\tRecetas disponibles en {categoria}')
        print('-' * 42)

        recetas_en_categoria = list(Path(rutario_categoria).glob('*.txt'))
        if recetas_en_categoria:
            for idx, txt in enumerate(recetas_en_categoria, start=1):
                print(f'  [{idx}] {txt.stem}')
            print('-' * 42)
            pregunta = int(input('¿Qué receta desea leer?: '))
            if 1 <= pregunta <= len(recetas_en_categoria):
                receta_seleccionada = recetas_en_categoria[pregunta - 1]
                contenido_receta = receta_seleccionada.read_text()
                print(contenido_receta)
            else:
                print("Selección de receta no válida.")
        else:
            print("No hay recetas disponibles en esta categoría.")
    else:
      print("Categoría no válida.")

#Opcion 2
def crear_receta():
  categoria = seleccionar_categoria()
  if categoria:
    rutario_categoria = Path(rutas, categoria)

    system('cls')
    print('-' * 42)
    print(f'\tRecetas disponibles en {categoria}')
    print('-' * 42)
    recetas_en_categoria = list(Path(rutario_categoria).glob('*.txt'))
    if recetas_en_categoria:
      for idx, txt in enumerate(recetas_en_categoria, start=1):
        print(f'  [{idx}] {txt.stem}')
    else:
      print('No hay recetas, crea la primera')
    print('-' * 42)
    nombre = input('¿Qué receta desea crear?: ')
    contenido = input('Escriba su receta: ')
    archivo = Path(rutas, categoria, f'{nombre}.txt')
  with archivo.open('w', encoding='utf-8') as f:
    f.write(contenido) 
    f.close()
  return ejecucion()


#Opcion 3
def crear_categoria():
  imprimir('Crear receta', recetas)
  categoria = str(input('¿Que categoria desea crear?: '))

  recetas.add(categoria)
  Path.mkdir(Path(rutas, f'{categoria}'))
  return ejecucion()

#Opcion 4
def borrar_receta():
  categoria = seleccionar_categoria()
  if categoria:
    rutario_categoria = Path(rutas, categoria)

    system('cls')
    print('-' * 42)
    print(f'\tRecetas disponibles en {categoria}')
    print('-' * 42)
    recetas_en_categoria = list(Path(rutario_categoria).glob('*.txt'))
    if recetas_en_categoria:
      for idx, txt in enumerate(recetas_en_categoria, start=1):
        print(f'  [{idx}] {txt.stem}')
    else:
      print('No hay recetas en esta categoria')
      return None
    print('-' * 42)
    eliminado = int(input('¿Qué receta desea eliminar?: '))
    if 1 <= eliminado <= len(recetas_en_categoria):
      receta = recetas_en_categoria[eliminado - 1]
      Path.unlink(Path(rutas, categoria, f'{receta}'))
  return ejecucion()

#Opcion 5
def borrar_categoria():
  lista = list(recetas)
  imprimir('Borrar categoria', recetas)
  categoria = int(input('¿Que categoria desea eliminar?: '))

  if categoria <= len(recetas):
    lista = lista[categoria - 1]
    recetas.discard(lista)
    Path(rutas, f'{lista}').rmdir()
    return ejecucion()
  else:
    print("Selección no válida.")
    return None

#Opcion 6
def finalizar_codigo():
  system('cls')
  print('Gracias vuelva prontos!!')
  return

if __name__ == '__main__':
  ejecucion()