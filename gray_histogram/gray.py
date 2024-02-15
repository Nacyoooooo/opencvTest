import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('gdut.jpg',0)
equ=cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
hist,bins = np.histogram(img.flatten(),256,[0,256])
e,b = np.histogram(equ.flatten(),256,[0,256])

for i in e:
    print(i)
print(e.ndim)
print(hist.ndim)
print(equ,type(equ),equ.ndim)
cv.imwrite('res.jpg',res)
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()