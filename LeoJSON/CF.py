#import math
# Se importan las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
import json

# Se define la función 'cf', que toma como entrada un archivo 'file'
def cf(file):
    # Se intenta leer el archivo y cargarlo como un diccionario de Python
    try:
        # Se define la ruta para el archivo de salida
        supAdj = "../dinaOutputsAdj/" + file
        with open(file,"r") as j:
          cartaSup = json.load(j)

        # Si el valor de "GPM" es cero, se guarda el diccionario en el archivo de salida
        if cartaSup["GPM"] == 0:
            json_data = json.dumps(cartaSup)
            fileAdj = open(supAdj, "w")
            fileAdj.write(json_data)
            fileAdj.close()
            return

        # Se define la ruta para los archivos "sarta.json" y "calculados.json"
        sarta = file[0:file.rfind("/")]+"/sarta.json"
        calculados = file[0:file.rfind("/")]+"/calculados.json"
        fondo = "../DownHoleCards/" + file
        with open(calculados,"r") as calculados:
          calc = json.load(calculados)

        # Se convierten las listas de "position" y "force" en arrays de Numpy
        position = np.array(cartaSup["position"])
        force = np.array(cartaSup["force"])

        # Se actualiza el valor de "force" en el diccionario de entrada
        cartaSup["force"] = force.tolist()
        
        # Se convierte el diccionario actualizado en una cadena JSON
        json_data = json.dumps(cartaSup)
        
        # Se guarda la cadena JSON en el archivo de salida
        fileAdj = open(supAdj, "w")
        fileAdj.write(json_data)
        fileAdj.close()

        # Se lee el archivo "sarta.json" y se carga como un diccionario de Python
        with open(sarta,"r") as sarta:
          s = json.load(sarta)

        # Se calcula el tiempo total (en segundos) por tramo y el número total de tramos
        tTtotal = 60 / cartaSup["GPM"] 
        nTramos = s["n_tramos"]

        print (sarta, fondo)

        # Se imprime el valor de "peso_en_fluido" del archivo "calculados.json"
        print (calc["peso_en_fluido"])

        # Se definen las unidades de distancia y carga
        unidad_distancia =   s["unidad_distancia"] #-4.4482  #   
        unidad_carga = -4.4482 # s["unidad_carga"]

        # Se crean arrays de Numpy para la posición y la distancia recorrida en cada tramo
        x_tramo = np.zeros(shape=(4))
        d_tramo = np.zeros(shape=(4))

        # Se calcula la distancia recorrida en cada tramo y se actualiza el array 'x_tramo'
        for i in range(1,nTramos + 1):
          x_tramo[i] = x_tramo[i-1] + ( s["l_tramo"][i-1] *  s["l_varilla"] )

    # En caso de que ocurra una excepción, se imprime un mensaje en pantalla
    except:
        print("An exception occurred")

    # Se crea un gráfico con los datos de "position" y "force"


    plt.figure(figsize=(15,15))
    plt.plot(position, force)
    #plt.plot(U1, -Ux1)


    plt.title("Carta de fondo")
    plt.xlabel('Posicion')
    plt.ylabel('Fuerza')

    plt.show()

