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

desplazo = imutils.translate(imagen, 0, 100)
cv2.imshow("Imagen desplazada abajo derecha",desplazo)

M = np.float32([[1, 0, -50], [0, 1, -90]])
desplazo = imutils.translate(imagen, -50, -90)
cv2.imshow("Imagen Desplazada arriba izquierda", desplazo)

cv2.waitKey(0)
cv2.destroyAllWindows()