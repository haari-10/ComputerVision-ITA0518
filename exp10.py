import cv2

img = cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
rotate = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Original",img)
cv2.imshow("Rotated",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
