import numpy as np
import cv2

filename = "..\dataset\Lena.pgm"  #input( "Please enter filename: " )
ROI_x, ROI_y = 124, 124 # eval( input( "Enter (x, y) for ROI: " ) )
ROI_nr, ROI_nc = 25, 25 #eval( input( "Enter (rows, columns) for ROI: " ) )
img = cv2.imread( filename, -1 )
ROI = img[ ROI_x : ROI_x + ROI_nr, ROI_y : ROI_y + ROI_nc ]
cv2.imwrite( "ROI.bmp", ROI )