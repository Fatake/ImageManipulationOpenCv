import numpy as np
import argparse
import cv2
'''
Dado que colocar manualment eel valor de T es complicado
La tecnica Adaptativa considera a una cantidad pequeña
de pixeles vecinos 
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

thresh = cv2.adaptiveThreshold(blurr, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Mean Thresh", thresh)

thresh = cv2.adaptiveThreshold(blurr, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("gAUSSIAN Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()