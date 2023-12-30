import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#Base de datos
ruta = './public/img/Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

# Meter imagenes de db en array
for nombre in lista_empleados:
  imagen_actual = cv2.imread(f'{ruta}/{nombre}')
  mis_imagenes.append(imagen_actual)
  nombres_empleados.append(os.path.splitext(nombre)[0])

#Codificacion de imagen
def codificar(imagenes):
  lista_codificada = []
  for img in imagenes:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    codificado = fr.face_encodings(img)[0]
    lista_codificada.append(codificado)
  return lista_codificada

# Revision de foto
def registro(persona):
  f = open('registro.csv', 'r+')
  lista_datos = f.readlines()
  nombres_registro = []
  for linea in lista_datos:
    ingreso = linea.split(',')
    nombres_registro.append(ingreso[0])
  if persona not in nombres_registro:
    ahora = datetime.now().strftime('%H:%M:%S')
    f.writelines(f'\n{persona}, {ahora}')

lista_empleados_codificada = codificar(mis_imagenes)

#Tomar img de web cam
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
exito, imagen = captura.read()

# Registro de persona en db
if not exito:
  print('No se ha podido tomar la captura')
else:
  cara_captura = fr.face_locations(imagen)
  cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

  for ccodif, cubic in zip(cara_captura_codificada, cara_captura):
    coincidencias = fr.compare_faces(lista_empleados_codificada, ccodif)
    distancias = fr.face_distance(lista_empleados_codificada)
    indice_coincidencia = numpy.argmin(distancias)

    if distancias[indice_coincidencia] > 0.6:
      print('No hay coincidencia')
    else:
      nombre = nombres_empleados[indice_coincidencia]
      y1,x2,y2,x1 = cubic
      cv2.rectangle(imagen, (x1,y1), (x2,y2), (0,255,0), 2)
      cv2.rectangle(imagen, (x1,y2 - 35), (x2, y2), (0,255,0), cv2.FILLED)
      cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
      
      registro(nombre)

      cv2.imshow('Imagen web', imagen)
      cv2.waitKey(0)
