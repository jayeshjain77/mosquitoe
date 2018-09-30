import cv2
import numpy as np

def mask(img):
    #im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    im = np.array(img)
    flat = im.flatten()
    for i in range(len(flat)):
        if (flat[i]<180 and flat[i]>75):
            flat[i]=0
       # else:
        #    flat[i] = 255
    flat1 = flat.reshape(im.shape)
    return flat1


img = cv2.imread('/home/jayesh/Desktop/images1.jpeg')
a = mask(img)
cv2.imwrite('mask4.png',a)
cv2.imshow('a',a)
cv2.waitKey(0)