import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sx=cv2.Sobel(gray,cv2.CV_64F,1,0)
sy=cv2.Sobel(gray,cv2.CV_64F,0,1)
cv2.imshow("Sobel X",sx)
cv2.imshow("Sobel Y",sy)
cv2.waitKey(0)
cv2.destroyAllWindows()
