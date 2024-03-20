import numpy as np
import cv2
import matplotlib.pyplot as plt

def adjust_image(img, offset=0, scale=1.0):
    img_adj = img.astype(np.float16)
    # 請注意四則運算的前後關係是有不同的效果
    # 在本例中，我們事先執行加法、在執行乘法
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
print('(img).mean()=', img.mean())
print('(img).std()=', img_adj.std())
print('(img_adj+150).mean()=', img_adj.mean())
print('(img_adj+150).std()=', img_adj.std())


img_adj = adjust_image(img, -150)
cv2.imshow( "-150", img_adj )

img_adj = adjust_image(img, scale=0.6)
cv2.imshow( "*0.6", img_adj )

img_adj = adjust_image(img, scale=1.3)
cv2.imshow( "*1.3", img_adj )

img_adj = adjust_image(img, scale=1.3, offset=50)
cv2.imshow( "(img+150)*1.3", img_adj )


cv2.waitKey( 0 )
cv2.destroyAllWindows( ) 