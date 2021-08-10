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

	def crear():
		print("creando equipo")
		a=Team()
		a.conductor=raw_input("Por favor introduzca la posiciona o carril a elegir\n")
		a.carril=raw_input("Por favor introduzca el equipo de escuderia\n")
		a.carril=raw_input("Por favor introduzca la posiciona o carril a elegir\n")
		lista.append(a)
		pass

	def mostrar():
		print("visual")	
		pass