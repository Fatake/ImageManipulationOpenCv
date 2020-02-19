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

# Matriz M que define cuantos pixeles de desplazamiento
# [1,0,tx] donde tx es el numero de pixeles que se movera a la izquierda o derecha
# negativos izquierda
# positivos derecha
#
# [0,1,ty] donde tx es num de piceles que se movera arriba o abajo
# negativos arriba
# positivos Abajo
M = np.float32([[1, 0, 25], [0, 1, 50]])
desplazo = cv2.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))
cv2.imshow("Imagen desplazada abajo derecha",desplazo)

M = np.float32([[1, 0, -50], [0, 1, -90]])
desplazo = cv2.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))
cv2.imshow("Imagen Desplazada arriba izquierda", desplazo)

#Fin de archivo
cv2.waitKey(0)
cv2.destroyAllWindows()