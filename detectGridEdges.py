import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# image to detect
img = cv.imread("IMG_4075.jpg",0)
# optimal Canny params
edges = cv.Canny(img,100,100)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
