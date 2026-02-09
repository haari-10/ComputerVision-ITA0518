import cv2

text = input("Enter text: ")

img = cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")

cv2.putText(img, text, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Text Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
