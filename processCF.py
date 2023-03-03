
import time
import json
import sys
import logging
from CF import cf
from os import listdir
import os.path
from os.path import isfile, join, isdir
import re

# Si este archivo es el que se está ejecutando, ejecuta el siguiente bloque de código
if __name__ == "__main__":
	# Obtenemos el directorio fuente de los argumentos de línea de comandos o usamos el directorio actual
	src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
	# Configuramos el registro de eventos para que se muestren los detalles del archivo, línea, nivel de registro, etc.
	logging.basicConfig(format='%(lineno)d - %(asctime)s -%(filename)s - %(levelname)s : %(message)s',
									level=logging.INFO,
									filename = 'MainLogger.log', 
									#, filemode = 'w'
									#,  
									)
	# Definimos los patrones de archivo que queremos buscar
	patterns = "*" 
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	mypath = "./"
	# Obtenemos una lista de todos los directorios en el directorio actual
	onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]
	# Iteramos a través de cada directorio
	for f in onlydir:
		# Si hay un archivo llamado "sarta.json" en el directorio actual, imprimimos su nombre
		if os.path.exists(mypath + f + "/sarta.json"):
			print(f)
			# Iteramos a través de cada archivo en el directorio actual
			for d in listdir(join(mypath, f)):
				# Si el nombre del archivo coincide con un patrón específico, ejecutamos una función en él
				if re.match(r'\d\d\d\d_\d\d_\d\d \d\d~\d\d~\d\d.json',d):
					file = mypath + f + "/" + d
					print(file)
					cf(file)
	# Imprimimos una lista de todos los directorios en el directorio actual
	print(onlydir)

