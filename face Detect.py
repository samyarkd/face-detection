import cv2

# دیتا صورت
face_data = cv2.CascadeClassifier('C:/Users/SkBrut/Desktop/Python Projects/haarcascade_frontalface_default.xml')

# انتخاب عکس
#img = cv2.imread('C:/Users/SkBrut/Desktop/Python Projects/3.jpg')
#img = cv2.resize(img,(960, 540))





video = cv2.VideoCapture('C:/Users/SkBrut/Desktop/Python Projects/4.mp4')

successful_frame_read,frame = video.read()

# سیاه سفید کردن عکس
img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# تشخیص
face = face_data.detectMultiScale(img_gray)
# مربع
# (image , (mokhtasat gooshe aval --> (x, y) ), (mokhtasat gooshe dovom --> (x+w, y+h) ), color (B,G,R) , pen size)

for (x, y ,w ,h) in face:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)

# نمایش عکس
cv2.imshow('Face Detection' , img)

# صبر بکن 

cv2.waitKey()



print("Your code is working!!")






















"""
import cv2
import random

face_data = cv2.CascadeClassifier('C:/Users/SkBrut/Desktop/Python Projects/haarcascade_frontalface_default.xml')
# انتخاب یک عکس برای تشخیص چهره
img = cv2.imread('C:/Users/SkBrut/Desktop/Python Projects/3.jpg')
img = cv2.resize(img, (960, 540))

# سیاه سفید کردن با cvtColor که مخفف convert color to color هست
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  تشخیص چهره و مشخص کردن گوشه های چهره
face_corners = face_data.detectMultiScale(gray_img)
# گوشه های چهره
print(face_corners)



# کشیدن مربع دور چهره
# (image , (mokhtasat gooshe aval --> (x, y) ), (mokhtasat gooshe dovom --> (x+w, y+h) ), color (R,G,B) , pen size)

# روش اول


z = 0
while z < len(face_corners):
	(x, y, w, h) = face_corners[z]
	cv2.rectangle(img, (x, y), (x+w, y+h), (50, 255, 255), 4)
	cv2.rectangle(img, (x+1, y+1), (x+1+w, y+1+h), (50, 0, 0), 2)
	# نمایش عکس
	cv2.imshow('CV2', img)
	z+=1


# روش دوم
for (x, y, w, h) in face_corners:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)

# نمایش عکس
img = cv2.resize(img, (960, 540))
cv2.imshow('CV2', img)
# بعد از نمایش عکس خیلی سریع پنجره عکس بسته میشه برای همین باید کاری بکنیم که در این مرحله صبر بکنه
cv2.waitKey()
print("Code worked normanly !!")



# الگریتم تشخیص چهره haar cascade Algoritm
face_data = cv2.CascadeClassifier('C:/Users/SkBrut/Desktop/Python Projects/haarcascade_frontalface_default.xml')

# تشخیص چهره در ویدئو
video = cv2.VideoCapture('C:/Users/SkBrut/Desktop/Python Projects/4.mp4')

while True:
	successful_frame_read, frame = video.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_corners = face_data.detectMultiScale(gray_frame)
	for (x, y, w, h) in face_corners:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0 ,255, 0), 4)
	cv2.imshow("Face Detection", frame)
	cv2.waitKey(1)
video.release()


"""