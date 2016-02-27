#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import json
def menu():

	print "Selecciona una opción"
	print "\t1 - Listado de centros de Murcia "
	print "\t2 - Numero de centros por localidad"
	print "\t3 - Dime la localidad y te doy sus coordenadas"
	print "\t4 - Dame la pedania y te digo el numero de centros que hay"
	print "\t5 - Dame parte del telef. o fax y te digo los centros que tienen esos numeros"
	print "\t0 - salir"
while True:
	menu() # Mostramos el menu
 	opcionMenu = raw_input("Inserta un numero de la opción >> ") # solicituamos una opción al usuario
 	lista=[]
	    	# Codigo que lista el nombre de todos los centros de Murcia
		
	if opcionMenu=="1":
		# Codigo que lista el nombre de todos los centros de Murcia
		with open("colegios-murcia.json") as fichero:
			datos = json.load(fichero)
		for centros in datos:
			print centros["Centro"]
		

		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="2":
		for peda in datos:
			lista.append(peda["Pedania"])
		print " En",lista[0], "hay", lista.count("Lorca"), "centros."
		print " En",lista[1], "hay", lista.count("Purias"), "centros."
		print " En",lista[2], "hay", lista.count("La Paca"), "centros."
		print " En",lista[3], "hay", lista.count("Tercia"), "centros."
		print " En",lista[4], "hay", lista.count("Torrecilla"), "centros."
		print " En",lista[6], "hay", lista.count("Ramonete"), "centros."
		print " En",lista[7], "hay", lista.count("Morata"), "centros."
		print " En",lista[8], "hay", lista.count("Escucha"), "centros."
		print " En",lista[9], "hay", lista.count("Marchena"), "centros."
		print " En",lista[10], "hay", lista.count("La Hoya"), "centros."
		print " En",lista[11], "hay", lista.count("Escucha"), "centros."
		print " En",lista[12], "hay", lista.count("Cazalla"), "centros."
		print " En",lista[13], "hay", lista.count("Campillo"), "centros."
		print " En",lista[14], "hay", lista.count("Zarcilla de Ramos"), "centros."
		print " En",lista[15], "hay", lista.count("Zarzadilla de Totana"), "centros."
		print " En",lista[16], "hay", lista.count("Aviles"), "centros."
		print " En",lista[17], "hay", lista.count("Coy"), "centros."
		print " En",lista[18], "hay", lista.count("La Tova"), "centros."
		

		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="3":

		print ""

		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="4":

		print ""

		raw_input("\npulsa Intro para continuar")		

	elif opcionMenu=="5":

		print ""

		raw_input("\npulsa Intro para continuar")	

	elif opcionMenu=="0":

		break

	else:

		print ""

		raw_input("\npulsa Intro para continuar")
