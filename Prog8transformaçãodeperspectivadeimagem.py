import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('trabalho.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[60,70],[390,70],[30,350],[380,390]])
pts2 = np.float32([[10,20],[300,20],[50,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Antes')
plt.subplot(122),plt.imshow(dst),plt.title('Depois')
plt.show()
