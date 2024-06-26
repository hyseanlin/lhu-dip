import numpy as np
import cv2

def harris_corner_detection( f ):
	g = cv2.cvtColor( f, cv2.COLOR_GRAY2BGR )
	nr, nc = f.shape[:2]
	gray = np.float32( f )
	dst = cv2.cornerHarris( gray, 2, 3, 0.04 )
	for x in range( nr ):
		for y in range( nc ):
			if dst[x,y] > 0.1 * dst.max():
				cv2.circle( g, (y,x), 5, [255,0,0], 2 )
	return g

def main( ):
	img1 = cv2.imread( "Blox.bmp", 0 )
	img2 = harris_corner_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Harris Corners", img2 )
	cv2.waitKey( 0 )

main( )