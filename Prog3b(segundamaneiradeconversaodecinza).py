import cv2

im = cv2.imread('trabalho.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('buraconegro_gray.jpg', img)
print('..|imagem salva com sucesso')
