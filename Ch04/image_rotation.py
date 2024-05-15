import numpy as np
import cv2
import math

img1 = cv2.imread( "../dataset/mature_girl.jpg", -1 )
nr2, nc2 = img1.shape[:2]

rot_center = (0, 0) #( nr2 / 2, nc2 / 2 )
rotation_matrix = cv2.getRotationMatrix2D(rot_center , 0, 1 )

rotation_matrix[0][0] = 1.0
rotation_matrix[0][1] = 0.0
rotation_matrix[0][2] = 105.0
rotation_matrix[1][0] = 0.0
rotation_matrix[1][1] = 1.0
rotation_matrix[1][2] = 105.0

img2 = cv2.warpAffine( img1, rotation_matrix, ( nr2, nc2 ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Rotation", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()