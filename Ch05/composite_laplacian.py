import numpy as np
import cv2

def composite_laplacian( f ):
	kernel = np.array( [ [0, -1, 0 ],
                     [-1, 4, -1],
                     [0, -1, 0] ] )
	temp = cv2.filter2D( f, cv2.CV_32F, kernel )
	g = np.uint8( np.clip( temp, 0, 255 ) )
	return g
		
def main( ):
    img1 = cv2.imread( "../dataset/lena.ppm", 0)
    img2 = composite_laplacian( img1 )
    cv2.imshow( "Original Image", img1 )	
    cv2.imshow( "Composite Laplacian", img2 )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()

main( )