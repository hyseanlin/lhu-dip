import numpy as np
import cv2
filter_size = 5
sigma = 0
img1 = cv2.imread( "../dataset/lena.pgm", 0)
img2 = cv2.GaussianBlur( img1, ( filter_size , filter_size  ), 0 )
# cv2.imshow( "Original Image", img1 )	
# cv2.imshow( "Gaussian Filtering", img2 )
cv2.imwrite(f'lenna_gauss_filtered_sz{filter_size}_sigma{sigma}.png', img2)

cv2.waitKey( 0 )