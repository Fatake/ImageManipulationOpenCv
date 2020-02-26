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

recortada = imagen[1:116, 100:213]
cv2.imshow("Original",recortada)

cv2.waitKey(0)
cv2.destroyAllWindows()