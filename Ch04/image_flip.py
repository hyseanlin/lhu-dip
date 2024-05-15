import numpy as np
import cv2

img = cv2.imread( "../dataset/mature_girl.jpg", -1 )
img1 = cv2.flip( img, 0 ) # 上下(垂直)翻轉
img2 = cv2.flip( img, 1 ) # 左右(水平)翻轉
img3 = cv2.flip( img, -1 ) # 左右上下翻轉
cv2.imshow( "Original Image", img )
cv2.imshow( "Flip Vertically", img1 )
cv2.imshow( "Flip Horizontally", img2 )
cv2.imshow( "Flip Vertically and Horizontally", img3 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()