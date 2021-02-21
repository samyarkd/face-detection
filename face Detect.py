import cv2
import random


# face detection with image
face_data = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')
img = cv2.imread('/2.jpg')
img = cv2.resize(img, (960, 540))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_corners = face_data.detectMultiScale(gray_img)
print(face_corners)


 # first way
"""
z = 0
while z < len(face_corners):
	(x, y, w, h) = face_corners[z]
	# (image , (xywh= Face coordinates ) (BGR), pen size)
	cv2.rectangle(img, (x, y), (x+w, y+h), (50, 255, 255), 4)
	cv2.imshow('CV2', img)
	z+=1
"""
# secend way
for (x, y, w, h) in face_corners:
	# (image , (xywh= Face coordinates ) (BGR), pen size)
	cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)

img = cv2.resize(img, (960, 540))
cv2.imshow('CV2', img)
cv2.waitKey()
print("Code worked normanly !!")


# real time in video or webcam

"""
face_data = cv2.CascadeClassifier('C:/Users/SkBrut/Desktop/Python Projects/haarcascade_frontalface_default.xml')

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

