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

(h, w) = imagen.shape[:2]
centro = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(centro, 45, 1.0)
rotada = cv2.warpAffine(imagen, M, (w,h))
cv2.imshow("Rotada 45",rotada)

M = cv2.getRotationMatrix2D(centro, -90, 1.0)
rotada = cv2.warpAffine(imagen, M, (w,h))
cv2.imshow("Rotada -90",rotada)

rotada = imutils.rotate(imagen,180)
cv2.imshow("Rotada 180",rotada)

cv2.waitKey(0)
cv2.destroyAllWindows()