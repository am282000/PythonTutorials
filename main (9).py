import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "viru.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    # it is a 2d array => to convert img to grayscale
    
def dodge(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')     #uint 8 is the signed integer
    
ss=imageio.imread(img)      #to raed the given img
gray = rgb2gray(ss)

i=255-gray

blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)    #sigma is the intensity of blurness
r=dodge(blur,gray)
cv2.imwrite('sketch.png',r)


# Install these libraries first


# pip install numpy
# pip install imageio
# pip install opencv-python
# pip install image


