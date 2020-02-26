# Todas las imagenes tienen pixeles de rango [0,255]
# Ya que se usa 8bits sin signo
from __future__ import print_function
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original",imagen)

# 200 + 100 en cv2.add retorna el 255 ya que son 8 bits y el 300 no
# es un numero representable
print("max de 255:{}".format(cv2.add(np.uint8([200]), np.uint8([100]))))#suma

# De mismo nodo la resta de 50-100 en 8 bits es 0 ya que estamos tomando
# 8bits sin signo
print("min de 0:{}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))#Resta

# Por otro lado cuando opera solo con arreglos de numpy---------------

# Tanto en suma con en resta una vez pasado el 255 de los 8 bits
# vuelve a contar desde el 0 o a restar desde el 255
# "wraps around"
print("wrap around:{}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around:{}".format(np.uint8([50]) - np.uint8([100])))

#----------------Con imagen-----------------

#Matriz de puros unos de tamaño de la imagen que se multiplica a 100
matriz = np.ones(imagen.shape, dtype ="uint8")*100
sumado = cv2.add(imagen, matriz) #Se agregan 100 a cada pixel de la imagen
cv2.imshow("Suma", sumado)

matriz = np.ones(imagen.shape, dtype ="uint8")*100
restado = cv2.subtract(imagen, matriz)#Se restra 100 a cada pixel de la imagen
cv2.imshow("resta", restado)

cv2.waitKey(0)
cv2.destroyAllWindows()