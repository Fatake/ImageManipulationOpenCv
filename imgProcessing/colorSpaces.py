import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("original", imagen)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()