import cv2
import numpy as np
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
kernel=np.ones((5,5),np.uint8)
er=cv2.erode(img,kernel,1)
cv2.imshow("Erosion",er)
cv2.waitKey(0)
cv2.destroyAllWindows()
