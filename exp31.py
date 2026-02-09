import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Segmented",th)
cv2.waitKey(0)
cv2.destroyAllWindows()
