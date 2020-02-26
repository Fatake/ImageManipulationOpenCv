import numpy as np
import argparse
import cv2
'''
Un histograma representa la distribución de intensidades de píxeles 
(ya sea color o escala de grises) en una imagen. 
Se puede visualizar como un gráfico (o Grafo) 
que proporciona una intuición de alto nivel de la distribución de intensidad. 

eje x o bins es la distribucion de los pixeles
eje y es las veces que cae en esa distribucion

Se requiere contraste brillo e intensidad de distribucion

cv2.calcHist(imagen, canales, mascara, histSize, rangos)
    imagen:
        imagen que se va a computar en el histograma
    canales:
        Lista de indices del canal que se va a computar
        escala de grices [0]
        RGB [0,1,2]
    mascara:
        Si es dada, solo se va a computar la seleccion donde está la mascara
    histSize: //Eje X
        es el numero de "binds" es una lista para cada canal que se computara
        por ejemplo para 32 bins en RGB [32,32,32]
    rangos: //Eje Y
        rango posible de valores de pixeles normalmente [0,255] oara cada cabak
        HSV cambia
'''
