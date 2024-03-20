import numpy as np
import cv2
import matplotlib.pyplot as plt

def adjust_image(img, offset=0, scale=1.0):
    img_adj = img.astype(np.float16)
    img_adj = img_adj + offset
    img_adj = img_adj * scale
    img_adj = np.floor(img_adj + 0.5)
    img_adj[img_adj > 255] = 255
    img_adj[img_adj < 0 ] = 0
    return img_adj.astype(np.uint8)


img = cv2.imread( "..\dataset\Lena.pgm", -1 )
cv2.imshow( "Original Image", img )

img_adj = adjust_image(img, 150)
cv2.imshow( "+150", img_adj )

img_adj = adjust_image(img, -150)
cv2.imshow( "-150", img_adj )

img_adj = adjust_image(img, scale=0.6)
cv2.imshow( "*0.6", img_adj )

img_adj = adjust_image(img, scale=1.3)
cv2.imshow( "*1.3", img_adj )


cv2.waitKey( 0 )
cv2.destroyAllWindows( ) 