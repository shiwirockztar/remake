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
	os.system('pause')
	pass

def crear():
	print("creando equipo")
	a=Team()
	a.conductor=input("Por favor introduzca su nombre a elegir\n")
	a.carro=input("Por favor introduzca el equipo de escuderia\n")
	a.carril=input("Por favor introduzca la posiciona o carril a elegir\n")
	lista.append(a)
	pass

def jugar():
	print("jugando")
	pass

def buscar():
	filtro=input("Por favor introduzca palabra a buscar\n")
	for a in lista:
		if a.conductor==filtro or a.carro==filtro:
			print("El jugador ",a.conductor," juega con el carro ",a.carro,"en el carril ",a.carril)
			pass
		pass
	os.system('pause')	
	pass

def salir():
	print("saliendo")
	pass

def menu():
	op=0
	salir=4
	while op!=salir:
		os.system('cls')
		print("Menu")
		print("1.- Registrar jugador")
		print("2.- Mostrar competidores")
		print("3.- Jugar")
		print("4.- Salir")
		op=int(input("Por favor introduzca la opcion a elegir\n"))
		if op==1:
			crear()
			pass	
		elif op==2:
			mostrar()
			pass
		elif op==3:
			jugar()
			pass
		elif op==4:
			salir()
			pass
		#opcion oculta
		if op==9:
			buscar()
			pass
	
		pass

	pass


	
menu()
