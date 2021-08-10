import sys          #libreria para limpiar pantalla
import time         #libreria para el uso del time.sleep()
import random       #libreria para el uso de los numero aleatorios
import os           #libreria para el uso del os.system('cls')

global lista
lista= list()

# definimos los atributos
class Team:
	carro=""
	conductor=""
	carril=0


def mostrar():
	print("visual")
	for a in lista:
		print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril) 
		pass	
	pass

def crear():
	print("creando equipo")
	a=Team()
	a.conductor=raw_input("Por favor introduzca la posiciona o carril a elegir\n")
	a.carro=raw_input("Por favor introduzca el equipo de escuderia\n")
	a.carril=raw_input("Por favor introduzca la posiciona o carril a elegir\n")
	lista.append(a)
	pass

def menu():
	op=0
	salir=4
	while op!=salir:
		print('''
         Menu :
0>montoya	 3>hamilton	 
1>vettel         4>alonzo
2>schumacher     5>speede 
''')
		pass
	pass

menuC='''
         Menu :
0>montoya	 3>hamilton	 
1>vettel         4>alonzo
2>schumacher     5>speede 
'''
	
