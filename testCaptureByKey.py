import cv2
import numpy as np 

# cap = cv2.VideoCapture(0)

# while True:
# 	ret, frame = cap.read()
# 	cv2.imshow("Test Picture", frame) # displays captured image

# if k == 27 : 
# 	cv2.destroyAllWindows()
# elif k == ord('s'):
# 	cv2.imwrite('messigray.png',img)


cam = cv2.VideoCapture(0)
while True :
	s, imageFromCam = cam.read() # captures imageFromCam
	grayImageFromCam = cv2.cvtColor(imageFromCam, cv2.COLOR_BGR2GRAY)
	# ret,threshImage = cv2.threshold(grayImageFromCam,75,125,0)
	blurred = cv2.GaussianBlur(grayImageFromCam, (35,35), 0)
	_, thresh1 = cv2.threshold(blurred, 70, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	im2, contours, hierarchy = cv2.findContours(thresh1,2,1)

	max_area = -1
	for i in range(len(contours)):
		cnt=contours[i]
		area = cv2.contourArea(cnt)
		if(area>max_area):
			max_area=area
			ci=i
	cnt=contours[ci]
	hull = cv2.convexHull(cnt,returnPoints = False)
	defects = cv2.convexityDefects(cnt,hull)

	for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple(cnt[s][0])
		end = tuple(cnt[e][0])
		far = tuple(cnt[f][0])
		cv2.line(imageFromCam,start,end,[0,255,0],2)
		cv2.line(thresh1,start,end,[0,255,0],2)
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(imageFromCam, (x,y), (x+w,y+h),[0,255,0], 2)
		cv2.rectangle(thresh1, (x,y), (x+w,y+h),[0,255,0], 2)
		# cv2.circle(imageFromCam,far,5,[0,0,255],-1)

	cv2.imshow("Test Capture Picture", thresh1) # displays captured imageFromCam

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite("test.png",imageFromCam) # writes image test.bmp to disk
		break

cam.release()
cv2.destroyAllWindows()

# import cv2                             
# import numpy as np                           #importing libraries
                      
# img = cv2.imread('test.png')  

# im = cv2.imread('test.jpg')
# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray,127,255,0)
# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # blur = cv2.GaussianBlur(gray,(1,1),0)
# # ret,thresh1 = cv2.threshold(blur,10,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# im2, contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for i in range(len(contours)):
# 	cnt=contours[i]
# 	area = cv2.contourArea(cnt)
# 	if(area>200):
# 		area=200
#                 ci=i
# cnt=contours[ci]
# hull = cv2.convexHull(cnt)
# drawing = np.zeros(img.shape,np.uint8)
# cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
# cv2.drawContours(drawing,[hull],0,(0,0,255),2)

# cv2.imshow('img_drawing',drawing)
# cv2.imshow('img_thresh',im2)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

