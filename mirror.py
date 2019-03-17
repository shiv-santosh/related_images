import os
import cv2

path = "/Users/shiv/related_images/resized_data/reverse_images/"

for i in os.listdir(path):
	cv2.imwrite(path+i+".jpg",cv2.flip(cv2.imread(path+i),1))