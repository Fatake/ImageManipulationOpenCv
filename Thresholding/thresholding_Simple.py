import numpy as np
import argparse
import cv2
'''
Thresholdin o umbral es la binarizacion de una imagen.
De escala de gtrices a imagen binaria

Un umbral basico seria, tomar un pixel de valor p
donde todos los pixeles menores al valor p se ponen en cero
y todos los que sean masyores iguales a 255

utilizado para hacer focus a objetos o areas de interes
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

## Normal
(T, thresh) = cv2.threshold(blurr, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("img Threshold", thresh)

# Invertido
###############################Img,  valor T, Valor maximo, Metodo
(T, threshInv) = cv2.threshold(blurr, 155, 255, cv2.THRESH_BINARY_INV)
# Retorna dos valores, el valor T que especificamos y la imagen con el umbral
cv2.imshow("img ThresholdInv", threshInv)

cv2.imshow("Oxido", cv2.bitwise_and(imagen,imagen, mask=threshInv))

cv2.waitKey(0)
cv2.destroyAllWindows()