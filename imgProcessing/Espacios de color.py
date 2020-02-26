import cv2
import numpy as np

'''
#Crear una matriz de 300 x 300 de 3 canales
bgr = np.zeros((300,300,3),dtype=np.uint8)
Las imagenes brg son la lectura por defecto de cv2

bgr[:,:,:]=(255,0,0)#Color azul
cv2.imshow('BGR',bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
bgr = cv2.imread('Oxido.png')
C1 = bgr[:,:,0]#Canal B
C2 = bgr[:,:,1]#Canal G
C3 = bgr[:,:,2]#Canar R

cv2.imshow('BGR',np.hstack([C1,C2,C3]))

#Para cambiar a RGB
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
C1 = rgb[:,:,0]#Canal B
C2 = rgb[:,:,1]#Canal G
C3 = rgb[:,:,2]#Canar R
cv2.imshow('RGB',np.hstack([C1,C2,C3]))

#Escala de Grises 
gris = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('gris',gris)

#Fin de archivo
cv2.waitKey(0)
cv2.destroyAllWindows()