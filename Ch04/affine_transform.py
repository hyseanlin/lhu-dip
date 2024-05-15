import numpy as np
import cv2

img1 = cv2.imread( "../dataset/mature_girl.jpg", -1 )
nr, nc = img1.shape[:2]

pts1 = np.float32( [ [ 100, 100], [ nc, 0], [ 0, nr] ] )
pts2 = np.float32( [ [ 0, 0], [ nc, 0], [ 0, nr]  ] )
# 從 pts1 形成的三角形，轉換到 pts2 形成的三角形
T = cv2.getAffineTransform( pts1, pts2 )

img2 = cv2.warpAffine( img1, T, ( nc, nr ) )

cv2.imshow( "Original Image", img1 )
cv2.imshow( "Affine Transform", img2 )
cv2.waitKey( 0 )

cv2.destroyAllWindows()
cv2.imwrite( "O.bmp", img2 )