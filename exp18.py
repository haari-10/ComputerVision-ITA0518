import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
roi=img[100:300,100:300]
img[300:500,300:500]=roi
cv2.imshow("ROI",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
