import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import os.path
from datetime import datetime

def CargarArchivo():
	dic = {}
	if(os.path.isfile("RegistroJuegos.json")):
		arch = open("RegistroJuegos.json","r+")
		dic = json.load(arch)
	arch = open("RegistroJuegos.json","w")
	return dic,arch

def IngresoJugador():
	layout = [[sg.Text("Nombre", size=(15, 1)), sg.InputText()],
			  [sg.Button("Añadir")]]

	window = sg.Window("Ingresa nombre", layout)
	event, nombre = window.read()
	window.close()
	return nombre[0]

def SetearMenu():
	layout = [[sg.Button("Ahorcado",key = "1")],
			  [sg.Button("Ta-TE-TI",key = "2")],
			  [sg.Button("Otello",key = "3")],
			  [sg.Button("Salir",key = "4")]]

	menu = sg.Window("Menu",layout)
	return menu

def main(args):
	sg.theme("Dark Amber")
	juegos = ["Ahorcado","Ta_TE-TI","Otello"]
	dic,arch = CargarArchivo()
	nombre = IngresoJugador()
	menu = SetearMenu()

	sigo_jugando = True
	while sigo_jugando:
		opcion, values = menu.read()
		if opcion == '4':
			break
		now = datetime.now()
		date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
		num = int(opcion)-1
		dic[date_time] =(nombre,juegos[num])

		if opcion == '1':
			hangman.main()
		elif opcion == '2':
			tictactoeModificado.main()
		elif opcion == '3':
			reversegam.main()
		else:
			print("forced close")
			break

	menu.close()
	json.dump(dic,arch)
	arch.close()
		
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
