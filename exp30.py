import cv2
smile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
s=smile.detectMultiScale(gray,1.8,20)
for(x,y,w,h) in s:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
cv2.imshow("Smile",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
