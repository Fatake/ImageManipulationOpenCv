from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def trazarHistograma(imagen, titulo, mask=None):
    canales = cv2.split(imagen)
    colores = ("b","g","r")
    plt.figure()
    plt.title(titulo)
    plt.xlabel("Bins")
    plt.ylabel("# de pixeles")

    for (canal,color) in zip(canales,colores):
        histograma = cv2.calcHist([canal], [0], mask, [256], [0,256])
        plt.plot(histograma, color=color)
        plt.xlim([0,256])

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original", imagen)
trazarHistograma(imagen,"Historigrama de imagen Original")


mask = np.zeros(imagen.shape[:2], dtype ="uint8")
cv2.rectangle(mask, (73, 11), (184, 100), 255, -1)
cv2.imshow("Mascara", mask)
masked = cv2.bitwise_and(imagen, imagen, mask = mask)
cv2.imshow("AplicandoMascara", masked)
trazarHistograma(imagen,"Historigrama Con Mascara",mask)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()