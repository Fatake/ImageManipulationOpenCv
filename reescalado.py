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


# Tener encuenta el radios aspecto de la imagen
'''
    La relación de aspecto es la relación proporcional del ancho
    y la altura de la imagen. Si no tenemos en cuenta la relación
    de aspecto, nuestro cambio de tamaño arrojará resultados que
    no parecen correctos.
'''
## Reescalado por el width
r = 150.0/ imagen.shape[1]
dim = (150, int(imagen.shape[0]*r))

resized = cv2.resize(imagen, dim, interpolation=cv2.INTER_AREA)
#cv2.INTER_LINEAR,cv2.INTER_CUBIC,cv2.INTER_NEAREST. en interpolation
cv2.imshow("Rescala",resized)


## Reescalado en Height
r = 50.0 / imagen.shape[0]
dim = (int(imagen.shape[1] * r), 150)
resized = cv2.resize(imagen, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Rescala(Height)", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()