#Preguntas
texto = input('Ingrese su texto: ').lower()
letra1 = input('Ingrese primer letra: ').lower()
letra2 = input('Ingrese segunda letra: ').lower()
letra3 = input('Ingrese tercer letra: ').lower()

#Primero
n1 = texto.count(letra1)
n2 = texto.count(letra2)
n3 = texto.count(letra3)

#Segundo
contador_palabras = len(texto.split())

#Tercero
primera = list(texto[0])
ultima = list(texto[-1])

#Cuarto
invertido = ' '.join(texto.split()[::-1])

#Quinto
python = 'python' in texto
dic = {True:'si', False:'no'}

#Consola
print('\nCANTIDAD DE LETRAS')
print(f'La letra {letra1} aparece {n1} vez/veces')
print(f'La letra {letra2} aparece {n2} vez/veces')
print(f'La letra {letra3} aparece {n3} vez/veces\n')

print('CONTADOR DE PALABRAS')
print(f'La cantidad de palabras de tu texto es: {contador_palabras}\n')

print('PRIMER Y ULTTMA LETRA')
print(f'La primer letra del texto es {primera[0]} y la ultima {ultima[0]}\n')

print('TEXTO INVERTIDO')
print(f'Su texto invertido quedaria asi: {invertido}\n')

print('PALABRA PYTHON')
print(f'La palabra python {dic[python]} se encuentra en el texto')