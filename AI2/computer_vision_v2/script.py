import cv2
import numpy as np
import sys
from math import atan2
from math import pi

LOCATION = sys.argv[1]
THRESHOLD = int(sys.argv[2])
BLACK_PIXEL = (0, 0, 0)
WHITE_PIXEL = (255,255,255)

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
		cv2.imshow('gray_image', gray_image)
		print('showing gray image')
	elif k == ord('b'):
		cv2.destroyAllWindows()
		cv2.imshow('blur_image', blur_image)
		print('showing blur image')
	elif k == ord('s'):
		cv2.destroyAllWindows()
		cv2.imshow('sobel_image', sobel_image)
		print('showing sobel image')

	print("recursing")
	keystroke()

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

def grayImage(image):
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
	'''Returns a tuple with gx and gy'''
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

def sobelPixel(img, row, col):
	derivs = getDerivatives(img, row, col)
	gx = derivs[0]
	gy = derivs[1]
	g = gx * gx + gy * gy
	if(g > THRESHOLD * THRESHOLD):
		return BLACK_PIXEL #edge
	else:
		return WHITE_PIXEL

def sobelImage(image):
	img = image.copy()
	num_rows = img.shape[0] - 2
	num_cols = img.shape[1] - 2
	for i in range(1, num_rows):
		for j in range(1, num_cols):
			setPixel(img, i, j, sobelPixel(image, i, j)) 
			#image is not changed, img is changed
	return img

def neighbours(gx, gy):
	'''returns ((dx1, dy1), (dx2, dy2))'''
	theta = atan2(gy, gx) * 8 # Multiply by eight because unit circle split into eights to get lines to check along
	if((theta > (-pi) or theta < (pi)) or (theta > (7 * pi) or theta < (-7 * pi))): # or because can never be greater or less
		return ((-1, 0), (1, 0))
	elif((theta > (pi) and theta < (3 * pi)) or (theta > (-7 * pi) and theta < (-5 * pi))): # diagonal up
		return ((1, -1), (-1, 1))
	elif((theta > (3 * pi) and theta < (5 * pi)) or (theta > (-5 * pi) and theta < (-3 * pi))): # vertical
		return ((0, 1), (0, -1))
	elif((theta > (5 * pi) and theta < (7 * pi)) or (theta > (-3 * pi) and theta < (-1 * pi))): # diagonal down
		return ((-1, -1), (1, 1))
	else:
		print("Something went wrong #1")
		return ((0, 0), (0, 0))

def canny1Pixel(img, row, col):
	gx1, gy1 = getDerivatives(img, row, col)
	g1 = gx1 * gx1 + gy1 * gy1

	if(g1 < THRESHOLD * THRESHOLD):
		return WHITE_PIXEL #Not even an edge

	ds = neighbours(gx1, gy1)
	dx2, dy2 = ds[0]
	dx3, dy3 = ds[1]

	gx2, gy2 = getDerivatives(img, row+dx2, col+dy2)
	g2 = gx2 * gx2 + gy2 * gy2

	gx3, gy3 = getDerivatives(img, row+dx3, col+dy3)
	g3 = gx3 * gx3 + gy3 * gy3

	if(g1 > g2 and g1 > g3):
		return BLACK_PIXEL #stronger than neighbours
	else:
		return WHITE_PIXEL

def canny1Image(image):
	img = image.copy()
	num_rows = img.shape[0] - 4
	num_cols = img.shape[1] - 4
	for i in range(2, num_rows):
		for j in range(2, num_cols):
			setPixel(img, i, j, canny1Pixel(image, i, j))
	return img

def canny2Pixel(img, row, col):
	gx1, gy1 = getDerivatives(img, row, col)
	g1 = gx1 * gx1 + gy1 * gy1

	lt = THRESHOLD
	ht = THRESHOLD * 2

	print(lt * lt, ht * ht, g1)

	if((g1 > lt * lt) and (g1 < ht * ht)): #within boundary
		#check if neighbours are edges. If so, say its an edge, otherwise not
		ds = neighbours(gx1, gy1)
		dx2, dy2 = ds[0]
		dx3, dy3 = ds[1]
		gx2, gy2 = getDerivatives(img, row+dx2, col+dy2)
		g2 = gx2 * gx2 + gy2 * gy2
		gx3, gy3 = getDerivatives(img, row+dx3, col+dy3)
		g3 = gx3 * gx3 + gy3 * gy3

		if((g2 > lt * lt) or (g3 > lt * lt)): #neighbours are black
			return BLACK_PIXEL
		else:
			#return (0, 255, 0)
			return False
	else:
		return False

def canny2Image(image):
	img = image.copy()
	num_rows = img.shape[0] - 4
	num_cols = img.shape[1] - 4
	for i in range(2, num_rows):
		for j in range(2, num_cols):
			r = canny2Pixel(image, i, j)
			if(r):
				setPixel(img, i, j, r)
	return img


image = cv2.imread(LOCATION)
cv2.imshow('color_image',image)

gray_image = grayImage(image)
cv2.imshow('gray_image', gray_image)
if(LOCATION == "dog.jpg"):
	cv2.imwrite("gray_dog.jpg", gray_image)

blur_image = blurImage(gray_image)
cv2.imshow('blur_image', blur_image)
if(LOCATION == "dog.jpg"):
	cv2.imwrite("blur_dog.jpg", blur_image)

sobel_image = sobelImage(gray_image)
cv2.imshow('sobel_image', sobel_image)
if(LOCATION == "dog.jpg"):
	cv2.imwrite("sobel_dog.jpg", sobel_image)

canny1_image = canny1Image(gray_image)
cv2.imshow('canny1_image', canny1_image)
if(LOCATION == "dog.jpg"):
	cv2.imwrite("canny1_dog.jpg", canny1_image)

canny2_image = canny2Image(canny1_image)
cv2.imshow('canny2_image', canny2_image)
if(LOCATION == "dog.jpg"):
	cv2.imwrite("canny2_dog.jpg", canny2_image)


keystroke()