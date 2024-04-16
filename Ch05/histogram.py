import cv2
import matplotlib.pyplot as plt

def histogram( f ):
	if f.ndim != 3:
		hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
		plt.plot( hist )
	else:
		color = ( 'b', 'g', 'r' )
		for i, col in enumerate( color ):
			hist = cv2.calcHist( f, [i], None, [256], [0,256] )
			plt.plot( hist, color = col )
	plt.xlim( [0,256] )
	plt.xlabel( "Intensity" )
	plt.ylabel( "#Intensities" )
	plt.show( )

img = cv2.imread( "../dataset/over_exposure_sample.jpg", 0)
cv2.imshow( "Original Image", img )
histogram( img )

cv2.waitKey( 0 )
