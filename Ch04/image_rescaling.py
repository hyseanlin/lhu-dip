import numpy as np
import cv2

img = cv2.imread( "../dataset/mature_girl.png", -1 )
nr1, nc1 = img.shape[:2]  # original size
nr2, nc2 = nr1*2, nc1*2 # resize
img1 = cv2.resize( img, ( nc2, nr2 ), interpolation = cv2.INTER_NEAREST )
# img2 = cv2.resize( img1, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

img2 = cv2.resize( img, ( nc2, nr2 ), interpolation = cv2.INTER_LINEAR ) # 雙線性內插法(bilinear)
# img2 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

img3 = cv2.resize( img, ( nc2, nr2 ), interpolation = cv2.INTER_CUBIC ) # 雙立方內插法(bicubic)
# img3 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
# cv2.imshow( "Original Image", img )
# cv2.imshow( "Nearest Neighbor", img1 )
# cv2.imshow( "Bilinear", img2 )
# cv2.imshow( "Bicubic", img3 )
# cv2.waitKey( 0 )
# cv2.destroyAllWindows()

cv2.imwrite('mature_girl_nn.bmp', img1)
cv2.imwrite('mature_girl_linear.bmp', img2)
cv2.imwrite('mature_girl_cubi.bmp', img3)