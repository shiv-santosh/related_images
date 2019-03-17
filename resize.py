import os
import cv2

# a = cv2.imread("/Users/shiv/Desktop/Abarth_124_Spider_Convertible_2017_1.jpg")
# b = cv2.resize(a,(152,96))
# cv2.imwrite()
l = []
path = "/Users/shiv/related_images/data/"
for i in os.listdir(path):
	a = cv2.imread(path+i)
	b = cv2.resize(a,(152,96))
	cv2.imwrite("/Users/shiv/related_images/resized_data/"+i+".jpg",b)
