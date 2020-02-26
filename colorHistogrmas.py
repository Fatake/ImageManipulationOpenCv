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

fig = plt.figure()

ax = fig.add_subplot(131)
histograma = cv2.calcHist([canales[1], canales[0]], [0,1], None,
        [32,32], [0,256,0,256])

p = ax.imshow(histograma, interpolation = "nearest")
ax.set_title("2D Hist G y B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([canales[1], canales[2]], [0, 1], None,
        [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation ="nearest")
ax.set_title("2D Hist G y R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([canales[0], canales[2]], [0, 1], None,
        [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation ="nearest")
ax.set_title("2D Hist B y R")
plt.colorbar(p)

#Histograma 3D
hist = cv2.calcHist([imagen], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape:{}, with{} values".format(hist.shape, hist.flatten().shape[0]))


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()