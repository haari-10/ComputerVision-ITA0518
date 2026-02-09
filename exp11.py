import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
rot=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("Rotated",rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
