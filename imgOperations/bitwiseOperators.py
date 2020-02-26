import numpy as np
import cv2

'''
Operaciones entre bits:
    and
    or
    xor
    not
normalmente usada en imagenes de escala de grices
'''

recangulo = np.zeros((300, 300), dtype ="uint8")
cv2.rectangle(recangulo, (25, 25), (275, 275), 255, -1)
cv2.imshow("recangulo", recangulo)

circulo = np.zeros((300, 300), dtype ="uint8")
cv2.circle(circulo, (150, 150), 150, 255, -1)
cv2.imshow("circulo", circulo)

# Operaciones bit a bit
#Se Comara 2 pixeles menos en Not que solo es la negacione de un pixel

bitwiseAnd = cv2.bitwise_and(recangulo, circulo)
cv2.imshow("AND", bitwiseAnd)


bitwiseOr = cv2.bitwise_or(recangulo, circulo)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(recangulo, circulo)
cv2.imshow("XOR", bitwiseXor)


bitwiseNot = cv2.bitwise_not(circulo)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)
cv2.destroyAllWindows()