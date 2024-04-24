import numpy as np
import cv2
from scipy.signal import convolve2d

img1 = cv2.imread( "../dataset/lena.pgm", 0)
img2 = cv2.blur( img1, ( 3, 3 ) )
'''
our_filter = np.array( [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1] ] )
img2 = convolve2d( img1, our_filter, 'same' )
img2 = img2.astype(np.uint8)
'''
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Average Filtering", img2 )
cv2.waitKey( 0 )