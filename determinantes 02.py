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


import math
def bucles(cruze_rojo,cruze_verde,conjunto_de_puntos,caracteres,color,popear):
   brakecs=[]
   verdad=True
   while verdad:
      parentesis=(conjunto_de_puntos[cruze_rojo]*conjunto_de_puntos[cruze_verde])
      brakecs.append(parentesis)
      cruze_rojo=cruze_rojo+2
      cruze_verde=cruze_verde+2
      if cruze_verde>= caracteres and popear==False:
         verdad=False
         print(f'lista {color}',brakecs)
         return brakecs
      elif cruze_verde>=caracteres and popear==True:
         verdad=False
         brakecs.pop(-1)
         print(f'lista {color}',brakecs)
         return brakecs
def suma_listas(lista,color):
   suma=0
   for i in lista:
      suma=suma+(i)
   print(f'la suma en fila {color} es {suma}')
   return suma
cordenadas=[]

#---INTRODUCCION DE CORDENADAS---
while True:
	try:
		cordenada=int(input("introduce cordenada X: "))
	except ValueError:
		cordenadas.append(cordenada)
		cordenada="="
	if cordenada == "=" :
		print('comensamos a trabajar')
		print(cordenadas,'con esto aver que sale')
		break
	cordenadas.append(cordenada)
	cordenada=int(input('introduce cordenana Y: '))
	cordenadas.append(cordenada)

# PROSESAMIENTO DE LA INFORMACIO (RESOLVER DETERMINATE)
caracteres_sin_funcion=len(cordenadas)
lista_roja=bucles(0,3,cordenadas,caracteres_sin_funcion,'roja',False) #valores rojo de la columna izquierda
lista_verde=bucles(1,2,cordenadas,caracteres_sin_funcion,'verde',True) #valores verdes de la columna derecha
sumaR=suma_listas(lista_roja,'Rojo')
sumaV=suma_listas(lista_verde,'Verde')

#RESULTADO DE LA RESTA DESPUES DE SUMAR LOS RESULTADOS DE LAS MULTIPLICACIONES
resultado=(sumaR)-(sumaV)
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










