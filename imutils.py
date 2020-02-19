import numpy as np
import cv2

#
# Funcion que hace una imagen transladada en x, y
#
def imageTranslate(imagen, x, y):
    '''
    Matriz M que define cuantos pixeles de desplazamiento
    [1,0,tx] donde tx es el numero de pixeles que se movera a la izquierda o derecha
    negativos izquierda
    positivos derecha
    
    [0,1,ty] donde tx es num de piceles que se movera arriba o abajo
    negativos arriba
    positivos Abajo
    '''
    M = np.float32([[1, 0, x], [0, 1, y]])
    desplazada = cv2.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))

    return desplazada