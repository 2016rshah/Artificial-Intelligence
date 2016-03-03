import cv2
import numpy as np
from math import atan2
from math import pi
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
	derivs = getDerivatives(img, i, j)
	gx = derivs[0]
	gy = derivs[1]

	if(((gx * gx) + (gy * gy)) > (threshold * threshold)):
		return (0,0,0) # black pixel
	else:
		return (255, 255, 255) # white pixel

def sobelImage(image):
	img = image.copy()
	num_rows = img.shape[0] - 2
	num_cols = img.shape[1] - 2
	for i in range(1, num_rows):
		for j in range(1, num_cols):
			setPixel(img, i, j, sobelPixel(image, i, j, MID_THRESHOLD)) 
			#image is not changed, img is changed
	return img

# def neighbors(img, i, j, di, dj):
# 	low = getGvalue(img, i-di, j-di)
# 	high = getGvalue(img, i+di, j+dj)
# 	# if(low > )

def isEdge(img, i, j, lower_t, upper_t):
	if(i<1 or j<1 or i>=img.shape[0] or j>=img.shape[1]):
		return False

	derivs = getDerivatives(img, i, j)
	gx = derivs[0]
	gy = derivs[1]
	g = gx * gx + gy * gy
	#print(g, lower_t * lower_t, upper_t * upper_t)
	#print(g)

	if(g > upper_t * upper_t):
		return False
	elif(g < lower_t * lower_t):
		return True
	else:
		return True

def isGreatest(img, p1, p2, p3):
	derivs1 = getDerivatives(img, p1[0], p1[0])
	g1 = derivs1[0] * derivs1[0] + derivs1[1] * derivs1[1]

	derivs2 = getDerivatives(img, p2[0], p2[0])
	g2 = derivs2[0] * derivs2[0] + derivs2[1] * derivs2[1]

	derivs3 = getDerivatives(img, p3[0], p3[0])
	g3 = derivs3[0] * derivs3[0] + derivs3[1] * derivs3[1]
	return (g1>g2 and g1>g3)

def isStrong(img, i, j):
	if(i<1 or j<1 or i>=img.shape[0] or j>=img.shape[1]):
		return False

	derivs = getDerivatives(img, i, j)
	gx = derivs[0]
	gy = derivs[1]
	g = gx * gx + gy * gy

	theta = atan2(gy, gx) * 8 # Multiply by eight because unit circle split into eights to get lines to check along
	if((theta > (-pi) or theta < (pi)) or (theta > (7 * pi) or theta < (-7 * pi))): # or because can never be greater or less
		# print("horizontal")
		if(isGreatest(img, (i, j), (i-1, j), (i+1, j))):
			return False
		else:
			return True
	elif((theta > (pi) and theta < (3 * pi)) or (theta > (-7 * pi) and theta < (-5 * pi))): # diagonal up
		# print("diagonal up")
		if(isGreatest(img, (i, j), (i-1, j+1), (i+1, j-1))):
			return False
		else:
			return True
	elif((theta > (3 * pi) and theta < (5 * pi)) or (theta > (-5 * pi) and theta < (-3 * pi))): # vertical
		# print("vertical")
		if(isGreatest(img, (i, j), (i, j-1), (i, j+1))):
			return False
		else:
			return True
	elif((theta > (5 * pi) and theta < (7 * pi)) or (theta > (-3 * pi) and theta < (-1 * pi))): # diagonal down
		# print("diagonal down")
		if(isGreatest(img, (i, j), (i-1, j-1), (i+1, j+1))):
			return False
		else:
			return True
	else:
		# print("something must have been close?")
		return False

def neighbors(img, i, j, gx, gy):
	for ii in range(-1, 2):
		for jj in range(-1, 2):
			if(img.item(i+ii, j+jj, 0) == 0):
				print("found neighbor")
				return True
			else:
				print(img.item(i+ii, j+jj, 0))
				return False
	# theta = atan2(gy, gx) * 8 # Multiply by eight because unit circle split into eights to get lines to check along
	# if((theta > (-pi) or theta < (pi)) or (theta > (7 * pi) or theta < (-7 * pi))): # horizontal
	# 	# print("horizontal")
	# 	if(img.item(i-1, j, 0) == 0 or img.item(i+1, j, 0) == 0): #neighbors are black
	# 		return True
	# 	else:
	# 		return False
	# elif((theta > (pi) and theta < (3 * pi)) or (theta > (-7 * pi) and theta < (-5 * pi))): # diagonal up
	# 	# print("diagonal up")
	# 	if(img.item(i, j, 0) == 0 or img.item(i-1, j+1, 0) == 0):
	# 		#neighbors are black
	# 		return True
	# 	else:
	# 		return False
	# elif((theta > (3 * pi) and theta < (5 * pi)) or (theta > (-5 * pi) and theta < (-3 * pi))): # vertical
	# 	# print("vertical")
	# 	if(img.item(i, j-1, 0) == 0 or img.item(i, j+1, 0) == 0): 
	# 		#neighbors are black
	# 		return True
	# 	else:
	# 		return False
	# elif((theta > (5 * pi) and theta < (7 * pi)) or (theta > (-3 * pi) and theta < (-1 * pi))): # diagonal down
	# 	# print("diagonal down")
	# 	if(img.item(i-1, j-1, 0) == 0 or img.item(i+1, j+1, 0) == 0):
	# 		#neighbors are black
	# 		return True
	# 	else:
	# 		return False
	# else:
	# 	# print("something must have been close?")
	# 	return True


def isEdge2(img, i, j, lower_t, upper_t):
	if(i<1 or j<1 or i>=img.shape[0] or j>=img.shape[1]):
		return False

	derivs = getDerivatives(img, i, j)
	gx = derivs[0]
	gy = derivs[1]
	g = gx * gx + gy * gy
	print(g, lower_t * lower_t, upper_t * upper_t)

	if(g > upper_t * upper_t):
		return False
	elif(g < lower_t * lower_t):
		return True
	else:
		print("mid threshold")
		#contested edge
		if(neighbors(img, i, j, gx, gy)):
			print("Filled in a pixel during canny2")
			return True
		else:
			print("Apparently not neighboring anything")
			return False


def canny1(image):
	img = image.copy()
	num_rows = img.shape[0] - 4
	num_cols = img.shape[1] - 4
	#Pass 1 of canny
	for i in range(2, num_rows):
		for j in range(2, num_cols):
			if(isEdge(image, i, j, MID_THRESHOLD-(MID_THRESHOLD/2), MID_THRESHOLD+DT)): #image is not changed, img is changed
				setPixel(img, i, j, (255, 255, 255)) 
	return img
def canny2(image):
	img = image.copy()
	num_rows = img.shape[0] - 4
	num_cols = img.shape[1] - 4
	for i in range(2, num_rows):
		for j in range(2, num_cols):
			if(img.item(i, j, 0) == 0): # black, and therefore edge
				if(isEdge2(image, i, j, MID_THRESHOLD-(MID_THRESHOLD/2), MID_THRESHOLD)): 
					setPixel(img, i, j, (0, 0, 0)) # strong edges, fill with black
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
	elif k == ord('c'):
		cv2.destroyAllWindows()
		cv2.imshow('canny_image',canny_image)
		print('showing canny image')

	print("recursing")
	keystroke()

location = sys.argv[1]

MID_THRESHOLD = int(sys.argv[2])
DT = 25

#if I want to read from URL, do that here. Until them, I treat it as a local url 
image = cv2.imread(location)
cv2.imshow('color_image',image)

gray_image = grayImage(image)
cv2.imshow('gray_image',gray_image)
if(location == "dog.jpg"):
	cv2.imwrite("gray_dog.jpg", gray_image)

blur_image = blurImage(gray_image)
cv2.imshow('blur_image',blur_image)
if(location == "dog.jpg"):
	cv2.imwrite("blur_dog.jpg", blur_image)

sobel_image = sobelImage(gray_image)
cv2.imshow('sobel_image',sobel_image)
if(location == "dog.jpg"):
	cv2.imwrite("sobel_dog.jpg", sobel_image)

canny_image1 = canny1(sobel_image)
cv2.imshow('canny_image1', canny_image1)
if(location == "dog.jpg"):
	cv2.imwrite("canny1_dog.jpg", canny_image1)

canny_image2 = canny2(canny_image1)
cv2.imshow('canny_image2', canny_image2)
if(location == "dog.jpg"):
	cv2.imwrite("canny2_dog.jpg", canny_image2)

keystroke()

# Print out with
# ORIGINAL IMAGE
# SOBEL EDGES ONLY
# EDGES AFTER CANNY IS APPLIED
# A. AFTER EDGE THINNING
# B. AFTER WEEK EDGES ARE INCORPORATED
