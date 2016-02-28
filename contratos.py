#!/usr/bin/env/ python2
# -*- coding: utf-8 -*-

from lxml import etree
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def menu():

	print "Selecciona una opción"
	print "\t1 - Listado de numero expediente y el area a que pertenece "
	print "\t2 - Mostrar el numero de contratos en ejecución "
	print "\t3 - Mostrar contratos entre un limite inferior y superior "
	print "\t4 - Dime el nombre de un area y muestro contratista y objeto de la licitación "
	print "\t5 - Dame area y muestro importe total licitaciones "
	print "\t0 - salir"
while True:
	menu() # Mostramos el menu
 	opcionMenu = raw_input("Inserta un numero de la opción >> ") # solicituamos una opción al usuario
 	lista=[]
 	arbol= etree.parse('contratosadjudicados_2015.xml')
	raiz=arbol.getroot()
	doc=raiz.findall("contrato")
	if opcionMenu=="1":
		
		for lis in doc:
			print " Nº Expediente: ", lis[0].text, " Area a la que pertenece: ", lis[2].text
		
		

		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="2":
		for contr in doc:
			
			lista.append(contr[12].text)
		print " Hay ", len (lista[0]),"proyectos en Ejecución"
			
		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="3":
		nombre=raw_input( "Dime elcentro de que quieres las coordenadas: ")
		
		
		
		raw_input("\npulsa Intro para continuar")

	elif opcionMenu=="4":
		local=raw_input("Dime la localidad: ")
		

		raw_input("\npulsa Intro para continuar")		

	elif opcionMenu=="5":
		tel=raw_input(" Dime el nº telf. o fax para saber el centro: ")
		
			

		

		raw_input("\npulsa Intro para continuar")	

	elif opcionMenu=="0":

		break

	else:

		print ""

		raw_input("\npulsa Intro para continuar")
