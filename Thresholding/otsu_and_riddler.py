import numpy as np
import argparse
import mahotas
import cv2
'''
La tecnica de Otsu asume que existen dos picos en la escala d grises 
de un historigrama de una imagen
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original", imagen)
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(imagen, (5,5), 0)
cv2.imshow("EscalaGRis",imagen)

T = mahotas.thresholding.otsu(blurr)
print("Otsu threshold: {}".format(T))

thresh = imagen.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu",thresh)

T = mahotas.thresholding.rc(blurr)
print("Riddler-Carvard: {}".format(T))
thresh = imagen.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Carvard",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()