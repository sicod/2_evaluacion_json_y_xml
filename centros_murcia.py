#!/usr/bin/python2
# -*- coding: utf-8 -*-

import json
with open("colegios-murcia.json") as fichero:
    datos = json.load(fichero)
# Codigo que lista el nombre de todos los centros de Murcia
for centros in datos:
	print centros["Centro"]

