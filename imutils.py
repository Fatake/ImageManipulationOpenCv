import numpy as np
import cv2

#
# Funcion que hace una imagen transladada en x, y
#
def translate(imagen, x, y):
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

#
# Funcion que rota una Imagen
#
def rotate(imagen, angulo, center = None, scale = 1.0):
    (h, w) = imagen.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angulo, scale)
    rotada = cv2.warpAffine(imagen, M, (w, h))

    return rotada

#
# Funcion que reescala una imagen
#
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height /float(h)
        dim = (int(w * r), height)
    else:
        r = width /float(w)
        dim = (width,int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized