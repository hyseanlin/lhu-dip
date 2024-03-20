import numpy as np
import cv2

img = cv2.imread( "Baboon.bmp", -1 )
img1 = cv2.flip( img, 0 ) # 上下(垂直)翻轉
img2 = cv2.flip( img, 1 ) # 左右(水平)翻轉
cv2.imshow( "Original Image", img )
cv2.imshow( "Flip Vertically", img1 )
cv2.imshow( "Flip Horizontally", img2 )
cv2.waitKey( 0 )