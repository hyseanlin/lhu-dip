import numpy as np
import cv2

img = cv2.imread( ".\dataset\Lena.pgm", -1 )
cv2.imshow( "Example", img )
cv2.waitKey( 0 )
cv2.destroyAllWindows( )