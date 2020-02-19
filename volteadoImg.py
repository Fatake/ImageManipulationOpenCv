import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original",imagen)

# Se puede voltear una imagen en torno al eje x o al eje y o ambos
# Codigo:
# 0 vertical al rededor de x
# 1 Horizontal al rededor de Y
# -1 ambos x and y
flipped = cv2.flip(imagen, 1)
cv2.imshow("Volteada 1",flipped)

flipped = cv2.flip(imagen, 0)
cv2.imshow("Volteada 2",flipped)

flipped = cv2.flip(imagen, -1)
cv2.imshow("Volteada 3",flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()