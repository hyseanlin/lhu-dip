import numpy as np
import cv2

img1 = cv2.imread( "../dataset/mature_girl.jpg")

img2 = img1.copy()
img2[:, :, 0] = cv2.equalizeHist( img1[:, :, 0] )
img2[:, :, 1] = cv2.equalizeHist( img1[:, :, 1] )
img2[:, :, 2] = cv2.equalizeHist( img1[:, :, 2] )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Histogram Equalization", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()