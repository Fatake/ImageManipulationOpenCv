import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])

(B, G, R) = cv2.split(imagen)
cv2.imshow("Rojo", R)
cv2.imshow("Verde", G)
cv2.imshow("Azul", B)

merged = cv2.merge([B,G,R])
cv2.imshow("Merged",merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
