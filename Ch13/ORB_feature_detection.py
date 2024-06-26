import numpy as np
import cv2

def ORB_feature_detection( f ):
	g = cv2.cvtColor( f, cv2.COLOR_GRAY2BGR )	
	orb = cv2.ORB_create()
	kp = orb.detect( f, None )	
	kp, des = orb.compute( f, kp )	
	g = cv2.drawKeypoints( f, kp, g, color = (255, 0, 0) )
	return g

def main( ):
	img1 = cv2.imread( "Blox.bmp", 0 )
	img2 = ORB_feature_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "ORB Feature Detection", img2 )
	cv2.waitKey( 0 )
	cv2.imwrite( "Test.bmp", img2 )

main( )