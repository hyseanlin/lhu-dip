import numpy as np
import cv2

img1 = cv2.imread( "../dataset/under_exposure_sample.jpg", 0)
img2 = cv2.equalizeHist( img1 )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Histogram Equalization", img2 )
cv2.waitKey( 0 )