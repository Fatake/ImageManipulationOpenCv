from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Gray", imagen)

histograma = cv2.calcHist([imagen], [0], None, [256], [0,256])

#Plt crea una tabla para graficar
plt.figure()
plt.title("Histograma de Escala de Grices")
plt.xlabel("Bins")
plt.ylabel("# de Pixels")
plt.plot(histograma)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()