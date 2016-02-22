import cv2
import numpy as np
from math import atan2
import sys


def setPixel(img, row, col, newPixel):
	'''
		img is cv2 image
		row, col are obvious
		newPixel is a tuple with (r, g, b) values that you want to set
		does not return anything, but changes img value
	'''
	img.itemset((row, col, 0), newPixel[0])
	img.itemset((row, col, 1), newPixel[1])
	img.itemset((row, col, 2), newPixel[2])


def grayPixel(r, g, b):
	pxVal = .3 * r + .59 * g +  .11 * b
	return (pxVal, pxVal, pxVal)

def blurPixel(img, row, col):
	vals = []
	vals.append(img.item(row-1, col-1, 0))
	vals.append(2 * img.item(row-1, col, 0))
	vals.append(img.item(row-1, col+1, 0))

	vals.append(2 * img.item(row, col-1, 0))
	vals.append(4 * img.item(row, col, 0))
	vals.append(2 * img.item(row, col+1, 0))

	vals.append(img.item(row+1, col-1, 0))
	vals.append(2 * img.item(row+1, col, 0))
	vals.append(img.item(row+1, col+1, 0))

	val = sum(vals) / 16

	return (val, val, val)

def grayImage(image):
	'''returns grayed image'''
	img = image.copy()
	num_rows = img.shape[0]
	num_cols = img.shape[1]

	for i in range(num_rows):
		for j in range(num_cols):
			r = img.item(i, j, 0)
			g = img.item(i, j, 1)
			b = img.item(i, j, 2)
			setPixel(img, i, j, grayPixel(r, g, b)) 
	return img

def blurImage(image):
	'''returns blurred image'''
	img = image.copy()
	num_rows = img.shape[0] - 2
	num_cols = img.shape[1] - 2

	for i in range(1, num_rows):
		for j in range(1, num_cols):
			setPixel(img, i, j, blurPixel(img, i, j))
	return img 

def getDerivatives(img, i, j):
	gx = 0
	gy = 0 
	# gx = [
	# [-1, 0, 1],
	# [-2, 0, 2],
	# [-1, 0, 1]]
	gx += (-1) * img.item(i-1, j-1, 0) #top left
	gx += img.item(i+1, j-1, 0) # top right
	gx += (-2) * img.item(i-1, j, 0) # middle left
	gx += 2 * img.item(i+1, j, 0) # middle right
	gx += (-1) * img.item(i-1, j+1, 0) # bottom left
	gx += img.item(i+1, j+1, 0) # bottom right

	# gy = [
	# [-1, -2, -1],
	# [0, 0, 0],
	# [1, 2, 1]]
	gy += (-1) * img.item(i-1, j-1, 0) #top left
	gy += (-2) * img.item(i-1, j, 0) # top middle
	gy += (-1) * img.item(i+1, j-1, 0) # top right
	gy += img.item(i-1, j+1, 0) # bottom right
	gy += (2) * img.item(i, j+1, 0) # bottom middle
	gy += img.item(i+1, j+1, 0) # bottom right

	return (gx, gy)

def getGvalue(img, i, j):
	derivs = getDerivatives(img, j, j)
	gx = derivs[0]
	gy = derivs[1]

	return gx * gx + gy * gy


def sobelPixel(img, i, j, threshold):
	# gx = 0
	# gy = 0 
	# # gx = [
	# # [-1, 0, 1],
	# # [-2, 0, 2],
	# # [-1, 0, 1]]
	# gx += (-1) * img.item(i-1, j-1, 0) #top left
	# gx += img.item(i+1, j-1, 0) # top right
	# gx += (-2) * img.item(i-1, j, 0) # middle left
	# gx += 2 * img.item(i+1, j, 0) # middle right
	# gx += (-1) * img.item(i-1, j+1, 0) # bottom left
	# gx += img.item(i+1, j+1, 0) # bottom right

	# # gy = [
	# # [-1, -2, -1],
	# # [0, 0, 0],
	# # [1, 2, 1]]
	# gy += (-1) * img.item(i-1, j-1, 0) #top left
	# gy += (-2) * img.item(i-1, j, 0) # top middle
	# gy += (-1) * img.item(i+1, j-1, 0) # top right
	# gy += img.item(i-1, j+1, 0) # bottom right
	# gy += (2) * img.item(i, j+1, 0) # bottom middle
	# gy += img.item(i+1, j+1, 0) # bottom right

	# gSquared = gx * gx + gy * gy
	# # print(gx, gy)

	derivs = getDerivatives(img, i, j)
	gx = derivs[0]
	gy = derivs[1]

	if(((gx * gx) + (gy * gy)) > (threshold * threshold)):
		return (255, 255, 255) # black pixel
	else:
		return (0, 0, 0) # white pixel

def sobelImage(image):
	img = image.copy()
	num_rows = img.shape[0] - 2
	num_cols = img.shape[1] - 2
	for i in range(1, num_rows):
		for j in range(1, num_cols):
			setPixel(img, i, j, sobelPixel(image, i, j, MID_THRESHOLD)) #image is not changed, img is changed
	return img

def cannyPixel(image, i, j, lower_t, upper_t):
	derivs = getDerivatives(img, j, j)
	gx = derivs[0]
	gy = derivs[1]

	theta = atan2(gy, gx)
	
	getGvalue(img, i+1, j+1)

def cannyImage(image):
	img = image.copy()
	num_rows = img.shape[0] - 4
	num_cols = img.shape[1] - 4
	for i in range(2, num_rows):
		for j in range(2, num_cols):
			setPixel(img, i, j, cannyPixel(image, i, j, MID_THRESHOLD-50, MID_THRESHOLD+50)) #image is not changed, img is changed
	return img

def keystroke():
	#Escape key to exit
	k = cv2.waitKey(0)
	if k == 27:         # wait for ESC key to exit
	    cv2.destroyAllWindows()
	    exit()
	elif k == ord('n'):
		cv2.destroyAllWindows()
		cv2.imshow('color_image',image)
		print('showing normal image')
	elif k == ord('g'):
		cv2.destroyAllWindows()
		cv2.imshow('gray_image',gray_image)
		print('showing gray image')
	elif k == ord('b'):
		cv2.destroyAllWindows()
		cv2.imshow('blur_image',blur_image)
		print('showing blur image')
	elif k == ord('s'):
		cv2.destroyAllWindows()
		cv2.imshow('sobel_image',sobel_image)
		print('showing sobel image')
	# elif k == ord('c'):
	# 	cv2.destroyAllWindows()
	# 	cv2.imshow('canny_image',canny_image)
	# 	print('showing canny image')

	print("recursing")
	keystroke()

location = sys.argv[1]

MID_THRESHOLD = int(sys.argv[2])

#if I want to read from URL, do that here. Until them, I treat it as a local url 
image = cv2.imread(location)
cv2.imshow('color_image',image)

gray_image = grayImage(image)
cv2.imshow('gray_image',gray_image)

blur_image = blurImage(gray_image)
cv2.imshow('blur_image',blur_image)

sobel_image = sobelImage(gray_image)
cv2.imshow('sobel_image',sobel_image)

# canny_image = cannyImage(gray_image)
# cv2.imshow('canny_image', canny_image)

keystroke()

