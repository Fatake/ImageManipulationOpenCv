from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original", imagen)

canales = cv2.split(imagen)
colores = ("b","g","r")


plt.figure()
plt.title("Histograma de Colores")
plt.xlabel("Bins")
plt.ylabel("# de Pixels")

for (canal,color) in zip(canales,colores):
    histograma = cv2.calcHist([canal], [0], None, [256], [0,256])
    plt.plot(histograma, color=color)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()