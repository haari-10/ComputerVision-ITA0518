import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,(0,0,0),(180,255,200))
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("BG Sub",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
