import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--imagen", required=True, 
        help="Imagen pasada por Path")
args = vars(ap.parse_args())

imagen = cv2.imread(args["imagen"])
cv2.imshow("Original", imagen)


'''
            Tecnica "Averaging" o Promedio

Se establece una matriz de K*K donde K es impar
Se calcula el centro de la matriz de left-to-rigth y top-to-bottom
El centro se establece como promedio "Average" de todos los pixeles
Esta ventana se llama "convolution Kernel" o "Kernel".
Mientras el tamaño del kernel incremente, mas blur se aplica a la imagen
'''

blurred = np.hstack([#Horizontal stacks
    #########imagen, kernel K*K
    cv2.blur(imagen, (3,3)),
    cv2.blur(imagen, (5,5)),
    cv2.blur(imagen, (7,7))])
cv2.imshow("Averaged",blurred)

'''
                Tecnica Gaussian
En vez de usar una media simple como el desenfoque Averagin
La tecnica gausiana usa una media ponderada, donde los píxeles
de vecindad que están más cerca del píxel central contribuyen
con más "peso" al promedio.
Dado una imagen menos borroza pero mas natural
'''
blurred = np.hstack([
    #########imagen, kernel K*K, desviasion estanda en X
    cv2.GaussianBlur(imagen, (3,3),0),
    cv2.GaussianBlur(imagen, (5,5),0),
    cv2.GaussianBlur(imagen, (7,7),0)])
cv2.imshow("Gaussian",blurred)

'''
            Tenica de la media
Mas efectiva para eliminar ruido, parecido al de sonidos.
Ruido tipo "Sal y pimienta".
En vez de tomar el pixel central se toma la media de los pixeles vecinos al central
'''
blurred = np.hstack([
    #########imagen, size Kernel
    cv2.medianBlur(imagen, 3),
    cv2.medianBlur(imagen, 5),
    cv2.medianBlur(imagen, 7)])
cv2.imshow("Median",blurred)

'''
            Tenica Bilateral
Tecnica que atiende los bordes de la imagen, no solo reduciendo el ruido o detalles
Usa dos funciones Gausianas:
    1: Vecinos espaciales, pixeles que esta serca de un punto (x,y)
    2: modela la intensidad de píxeles del vecindario, 
    asegurando que solo los píxeles con intensidad similar se
    incluyan en el cálculo real del desenfoque.
Contras:
    Es mas lento que los demás métodos
'''
blurred = np.hstack([
    #imagen, diametro de pixeles vecinos, Desviacion del color, desviasion del espacio 
    cv2.bilateralFilter(imagen, 5, 21, 21),
    cv2.bilateralFilter(imagen, 7, 31, 31),
    cv2.bilateralFilter(imagen, 9, 41, 41)])
cv2.imshow("Bilateral",blurred)


cv2.waitKey(0)
cv2.destroyAllWindows()