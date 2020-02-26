import numpy as np
import argparse
import cv2
'''
La ecualización del histograma mejora el contraste de una
imagen al "estirar" la distribución de píxeles.

histogram equialization is applied to grayscale
'''

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

equalizada = cv2.equalizeHist(imagen)
cv2.imshow("Histograma Ecualizado", np.hstack([imagen, equalizada]))

cv2.waitKey(0)
cv2.destroyAllWindows()