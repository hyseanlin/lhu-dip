import numpy as np
import cv2

def image_quantization( f, bits ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	levels = 2 ** bits
	interval = 256 / levels
	gray_level_interval = 255 / ( levels - 1 )
	table = np.zeros( 256 )
	for k in range( 256 ):
		for l in range( levels ):
			if k >= l * interval and l < ( l + 1 ) * interval:
				table[k] = round( l * gray_level_interval ) 
    
	for x in range( nr ):
		for y in range( nc ):
			g[x,y] = np.uint8( table[f[x,y]] )
    
	return g
	
def main( ):
	img1 = cv2.imread( "../dataset/lena.ppm", -1 )
	img2 = image_quantization( img1, 2 )
	img3 = image_quantization( img1, 3 )
	img4 = image_quantization( img1, 2 )
	img5 = image_quantization( img1, 1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Quantization (5-bit)", img2 )
	cv2.imshow( "Quantization (3-bit)", img3 )
	cv2.imshow( "Quantization (2-bit)", img4 )
	cv2.imshow( "Quantization (1-bit)", img5 )
	cv2.waitKey( 0 )

main( )