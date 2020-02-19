import cv2
import numpy as np 

captura = cv2.VideoCapture(0)

#Rango del color en HSV
colorBajo = np.array([100,100,20],np.uint8)
colorAlto = np.array([125,255,255],np.uint8)

while True:
    ret,frame = captura.read()

    #Mientras grabe ret
    if ret == True:
        #Se obtiene una imagen del video un FRame
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
        #Mascara del color para que no se mueste otro color
        mask = cv2.inRange(frameHSV,colorBajo,colorAlto)

        cv2.imshow("Mascara",mask)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
cv2.destroyAllWindows