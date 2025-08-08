import math
#programa que calcule el area de figuras 
# en un plano cartesiano 
# dependiendo de las cordenadas dadas/introducidas
# muestra las listas con los resultados despues de ser procesadas
# Autor: Josue Perez 'El Jodue'
# EJEMPLO: 
#                                                  -1 ultimos lugares
#                                                  13 cosas
#conjunto_de_puntos=[0,7,6,0,3,-4,-3,-4,-6,0, 0, 7,'='] # lista con las cordenandas a calcular
#   numeracion      0 1 2 3 4  5  6  7  8 9 10 11 12
#   color           R V R V R  V  R  V  R V  R  V  R
#   binario         1 0 1 0 1  0  1  0  1 0  1  0  1

#---INTRODUCCION DE CORDENADAS---
conjunto_de_puntos=[]
while True:
	try:
		cordenada=int(input("introduce cordenada X: "))
	except ValueError:
		conjunto_de_puntos.append(cordenada)
		cordenada='='
	if cordenada == "=" :
		print('comensamos a trabajar')
		print(conjunto_de_puntos,'con esto aver que sale')
		break
	conjunto_de_puntos.append(cordenada)
	cordenada=int(input('introduce cordenana Y: '))
	conjunto_de_puntos.append(cordenada)


# PROSESAMIENTO DE LA INFORMACIO (RESOLVER INTEGRAL)
lista_roja=[]
cruze_rojo=0     #valores rojo de la columna izquierda
cruze_verde=3    #valores verdes de la columna derecha
caracteres=len(conjunto_de_puntos) #cuanta el total de cordenans aun con el simbolo '='
while True: # realiza las multiplicaciones hasta que el valor verde sea mayor que la cantidad de cordenadas de la lista
	parentesis=(conjunto_de_puntos[cruze_rojo]*conjunto_de_puntos[cruze_verde])
	lista_roja.append(parentesis)
	cruze_rojo=cruze_rojo+2
	cruze_verde=cruze_verde+2
	if cruze_verde>= caracteres:
		print('lista roja: ',lista_roja)
		break
cruze_rojo=1 #valores rojo de la columna derecha
cruze_verde=2
lista_verde=[]
while True:
	parentesis=(conjunto_de_puntos[cruze_rojo]*conjunto_de_puntos[cruze_verde])
	lista_verde.append(parentesis)
	cruze_rojo=cruze_rojo+2
	cruze_verde=cruze_verde+2
	if cruze_verde>=caracteres:
		lista_verde.pop(-1)
		print('lista verde',lista_verde)
		break


#SUMA DESPUES DE LA INTEGRAR 
suma_en_rojo=0
for r in lista_roja:
	suma_en_rojo=suma_en_rojo+(r)
print(f'la suma en fila roja es {suma_en_rojo}')

suma_en_verde=0
for v in lista_verde:
	suma_en_verde=suma_en_verde+(v)
print(f'la suma en fila verde es {suma_en_verde}')

#RESULTADO DE LA RESTA DESPUES DE SUMAR LOS RESULTADOS DE LAS MULTIPLICACIONES 
resultado=(suma_en_rojo)-(suma_en_verde)

# CAMINOS PARA EL RESULTADO:

if resultado<=0:
	print(resultado)
	print(':c')
	elevado=resultado**2
	resultado_positivo=math.sqrt(elevado)
	print(resultado_positivo)
	resultado_final=resultado_positivo/2
	print('al final de todo este codiguo')
	print('el resultado es: ')
	print(str(resultado_final), 'de area')
	print("autor Josue Perez")
else:
	print(resultado)
	print('c:')
	resultado_final=resultado/2
	print('al final de todo este codiguo')
	print('el resultado es: ')
	print(resultado_final, 'de area')
	print("autor Josue Perez")
