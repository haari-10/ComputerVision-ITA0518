import cv2
img=cv2.imread(r"C:\Users\murth\Documents\WhatsApp Image 2026-02-07 at 9.38.29 AM.jpeg")
overlay=img.copy()
cv2.putText(overlay,"WATERMARK",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
out=cv2.addWeighted(overlay,0.5,img,0.5,0)
cv2.imshow("Watermarked",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
