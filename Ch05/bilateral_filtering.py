import numpy as np
import cv2

filter_size = 5
clrSigma = 25
spSigma = 25
img1 = cv2.imread( "../dataset/lena.pgm", 0)
img2 = cv2.bilateralFilter( img1, filter_size, clrSigma, spSigma)
# cv2.imshow( "Original Image", img1 )	
# cv2.imshow( "Bilateral Filtering", img2 )
cv2.imwrite(f'lenna_original.png', img1)
cv2.imwrite(f'lenna_bilateral_filtered_sz{filter_size}_clr{clrSigma}_sp{spSigma}.png', img2)
cv2.waitKey( 0 )