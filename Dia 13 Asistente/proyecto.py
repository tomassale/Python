#Importaciones
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import os
import pyautogui as pa
import datetime
import time
from AppOpener import open, close

# Rutas de apps
visual = '"C:\\Users\\tomas\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code"'
spotify = '"C:\\Users\\tomas\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"'
notion = '"C:\\Users\\tomas\\AppData\\Local\\Programs\\Notion\\Notion.exe"'
screenshots = 'C:\\Users\\tomas\\OneDrive\\Pictures\\Capturas de pantalla'
#Opciones de voz
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'

#Interpretacion de voz
def audio_a_texto():
  r = sr.Recognizer()
  with sr.Microphone() as origen:
    r.pause_threshold = 0.5
    audio = r.listen(origen)

    try:
      pedido = r.recognize_google(audio, language='es-ar')
      return pedido
    #No devuelve el pedido
    except sr.UnknownValueError:
      return 'Sigo esperando'
    except sr.RequestError:
      return 'Sigo esperando'
    except:
      return 'Sigo esperando'
    
# Mensaje de respuesta
def hablar(mensaje):
  engine = pyttsx3.init()
  engine.setProperty('voice', id3)

  engine.say(mensaje)
  engine.runAndWait()

# Captura de pantalla
def screenshot():
  screen = pa.screenshot()
  screen.save(os.path.join(screenshots, 'screenCapture.png'))

# Devolver dia de hoy
def pedir_dia():
  dia = datetime.date.today()
  dia_semana = dia.weekday()
  
  calendario = {0: 'Lunes',
                1: 'Martes',
                2: 'Miercoles',
                3: 'Jueves',
                4: 'Viernes',
                5: 'Sabado',
                6: 'Domingo'}
  hablar(f'Hoy es {calendario[dia_semana]}')

# Pedir la hora actual
def pedir_hora():
  hora = datetime.datetime.now()
  hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
  hablar(hora)

# Saludo de inicio
def saludo_inicial():
  hora = datetime.datetime.now()
  if hora.hour < 6 or hora.hour > 20:
    momento = 'Buenas noches'
  elif 6 <= hora.hour < 13:
    momento = 'Buen dia'
  else:
    momento = 'Buenas tardes'

  hablar(f'{momento}, dime en que te puedo ayudar')

# Comandos de voz
def pedir_cosas():
  pedido = audio_a_texto().lower()
  if 'asistente' == pedido:
    comenzar = True
    saludo_inicial()
    while comenzar:
      pedido = audio_a_texto().lower()
      if 'abrir youtube' in pedido:
          hablar('Abriendo YouTube')
          webbrowser.open('https://www.youtube.com')
          continue
      elif 'abrir ópera' in pedido:
          hablar('Abriendo Opera GX')
          webbrowser.open('https://www.google.com')
          continue
      elif 'abrir setup' in pedido:
          hablar('Abriendo setup')
          open('notion', 'navegador opera gx', 'visual')
          continue
      elif 'abrir gaming' in pedido:
          hablar('Abriendo')
          continue
      elif 'abrir' in pedido:
          pedido = pedido.replace('abrir', '').strip()
          hablar(f'Abriendo {pedido}')
          open(pedido)
          continue
      elif 'cerrar' in pedido:
          pedido = pedido.replace('cerrar', '').strip()
          hablar(f'Cerrando {pedido}')
          close(pedido)
          continue
      elif 'abrir curso de python' in pedido:
          hablar('Abriendo curso de python')
          webbrowser.open('https://www.youtube.com/watch?v=_y9qQZXE24A')
      elif 'abrir curso de ingreso' in pedido:
          hablar('Abriendo Unlam Web')
          webbrowser.open('https://mielingreso.unlam.edu.ar/principal/home/')
          pa.moveTo(1750, 450)
          time.sleep(2)
      elif 'qué día es hoy' in pedido:
          pedir_dia()
          continue
      elif 'qué hora es' in pedido:
          pedir_hora()
          continue
      elif 'busca' in pedido:
          hablar('Ya mismo estoy en eso')
          pedido = pedido.replace('busca', '')
          pywhatkit.search(pedido)
          hablar('Esto es lo que he encontrado')
          continue
      elif 'reproduci' in pedido:
          pedido = pedido.replace('reproducir', '')
          pywhatkit.playonyt(pedido)
          hablar(f'Reproduciendo {pedido} en youtube')
          continue
      elif 'contame un chiste' in pedido:
          hablar(pyjokes.get_joke('es'))
          continue
      elif 'sacar screenshot' in pedido:
          hablar('Sacando screenshot')
          screenshot()
          continue
      elif 'precio de' in pedido:
          accion = pedido.split('de')[-1].strip()
          cartera = {'apple':'APPL',
                      'amazon':'AMZN',
                      'google':'GOOGL'}
          try:
              accion_buscada = cartera[accion]
              accion_buscada = yf.Ticker(accion_buscada)
              precio_actual = accion_buscada.info['regularMarketPrice']
              hablar(f'El precio de {accion} es {precio_actual}')
              continue
          except:
              hablar("Perdón pero no la he encontrado")
              continue
      elif 'gracias asistente' in pedido:
          hablar("Me voy a descansar, cualquier cosa me avisas")
          pedir_cosas()
  else:
    pedir_cosas()

# Inicio de programa
if __name__ == '__main__': 
  pedir_cosas()