import cv2

# el ,1 es a escala de colores
imagen = cv2.imread("Oxido.png",1)
# el ,0 es a escala de negro
#imagen = cv2.imread("Oxido.png",0)

cv2.imshow("Prueba de Imagen",imagen)

#Guarda Imagen
cv2.imwrite("Nuevo.png",cv2.imread("Oxido.png",0))

#Tabaja en milsegundos
cv2.waitKey(0)#= es cualquier tecla
cv2.destroyAllWindows()