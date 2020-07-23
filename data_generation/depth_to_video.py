import os
import numpy as np
import cv2

if __name__=='__main__':
	
	# dirs
	seq_name = '0517_take_02'
	seq_path = 'datasets/depth/' + seq_name + '/'
	imgs = os.listdir(seq_path)
	
	# get img properties
	frame = cv2.imread(seq_path+'00000000.png')
	height, width, layers = frame.shape
	
	# video
	fps = 30
	video_name = seq_name + '.avi'
	cap = cv2.VideoCapture(0)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	video = cv2.VideoWriter(video_name, fourcc, fps, (width,height))
	
	# stack frames
	for img in imgs:
		img_frame = cv2.imread(seq_path+img)
		video.write(img_frame)
	
	cv2.destroyAllWindows()
	video.release()