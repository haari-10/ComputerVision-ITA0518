import cv2

img = cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)
cv2.imshow("Original",img)
cv2.imshow("Canny Outline",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
