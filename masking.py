'''
Herramienta Poderoza en Procesamiento de Imagenes
Using a mask allows us to focus only on the portions of 
the image that interests us.

uses:
    computer xision system to recognize faces
'''
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original",imagen)

# mismo alto y ancho de la imagen 
mask = np.zeros(imagen.shape[:2], dtype="uint8")

# Se busca el centro de la imagen // integer division
(cx, cy) = (imagen.shape[1] // 2, imagen.shape[0] // 2)
# Se dibuja un rectangulo del tamaño de la mascara
cv2.rectangle(mask, (cx-75, cy-75), (cx+75 , cy+75), 255, -1)
cv2.imshow("Mascara",mask)

masked = cv2.bitwise_and(imagen, imagen, mask= mask)
cv2.imshow("Mascara Aplicada", masked)


mask = np.zeros(imagen.shape[:2], dtype ="uint8")
cv2.circle(mask, (cx, cy), 100, 255, -1)

masked = cv2.bitwise_and(imagen, imagen, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mascara Aplicada Circulo", masked)


cv2.waitKey(0)
cv2.destroyAllWindows()
