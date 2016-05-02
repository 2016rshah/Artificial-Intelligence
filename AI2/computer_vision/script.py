import cv2
import numpy as np
import sys
from math import atan2, pi, cos, sin
from math import degrees #converts to degrees
from math import radians #converts to radians
from math import sqrt

LOCATION = sys.argv[1]
THRESHOLD = int(sys.argv[2])
BLACK_PIXEL = (0, 0, 0)
WHITE_PIXEL = (255,255,255)
RED_PIXEL = (0, 0, 255)

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
	elif k == ord('1'):
		cv2.destroyAllWindows()
		cv2.imshow('canny1_image', canny1_image)
		print('showing canny1 image')
	elif k == ord('2'):
		cv2.destroyAllWindows()
		cv2.imshow('canny2_image', canny2_image)
		print('showing canny2 image')

	print("recursing")
	keystroke()

def setPixel(img, row, col, newPixel):
	'''
		img is cv2 image
		row, col are obvious
		newPixel is a tuple with (b, g, r) values that you want to set
		does not return anything, but changes img value
	'''
	img.itemset(row, col, 0, newPixel[0])
	img.itemset(row, col, 1, newPixel[1])
	img.itemset(row, col, 2, newPixel[2])

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

	#print("get derivatives", gx, gy)
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
	# print(theta)
	if((theta > (pi) and theta < (3 * pi)) or (theta > (-7 * pi) and theta < (-5 * pi))): # diagonal up
		return ((1, -1), (-1, 1))
	elif((theta > (3 * pi) and theta < (5 * pi)) or (theta > (-5 * pi) and theta < (-3 * pi))): # vertical
		return ((0, 1), (0, -1))
	elif((theta > (5 * pi) and theta < (7 * pi)) or (theta > (-3 * pi) and theta < (-1 * pi))): # diagonal down
		return ((-1, -1), (1, 1))
	elif((theta > (-pi) or theta < (pi)) or (theta > (7 * pi) or theta < (-7 * pi))): # or because can never be greater or less
		return ((-1, 0), (1, 0))
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

	if((g1 > lt * lt) and (g1 < ht * ht)): #within boundary
		#check if neighbours are edges. If so, say its an edge, otherwise not
		ds = neighbours(gx1, gy1)
		dx2, dy2 = ds[0]
		dx3, dy3 = ds[1]

		if(img.item(row+dx2, col+dy2, 0) is 0 or img.item(row+dx3, col+dy3, 0) is 0):
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

def getLine(image, row, col):
	'''takes a grayscale image
	returns a list of (x,y) values'''
	img = image.copy()
	num_rows = img.shape[0]
	num_cols = img.shape[1]
	gs = getDerivatives(img, row, col)
	gx = float(gs[0])
	gy = float(gs[1])
	res = []
	if(gy == 0 or gx == 0):
		return res
	slope = gy / gx
	if(abs(slope) >= 1):
		slope = slope
		for i in range(0, num_rows):
			j = slope * (i-row) + col
			if(j > 0 and j < (num_cols-1)):
				res.append((i, int(j)))
	else:
		slope = 1 / slope
		for j in range(0, num_cols):
			i = slope * (j-col) + row
			if(i > 0 and i<(num_rows-1)):
				res.append((int(i), j))
	return res

def maximums(votes):
	'''returns tuple
	first value is maximum value
	second value is maximum value's location'''
	maxValue = 0
	maxLocation = (0,0)
	for i in range(0, len(votes)):
		for j in range(0, len(votes[i])):
			if(votes[i][j] > maxValue):
				maxValue = votes[i][j]
				maxLocation = (i,j)
	return (maxValue, maxLocation)

def drawLines(canny, gray):
	'''returns tuple containing
	the resulting image with lines drawn based on votes and center
	the number of votes for each pixel based on how many lines pass through'''
	num_rows = gray.shape[0]
	num_cols = gray.shape[1]

	#initialize voting array
	votes = []
	for i in range(0, num_rows):
		row = []
		for j in range(0, num_cols):
			row.append(0)
		votes.append(row)

	#poll the image
	for i in range(1, num_rows - 1):
		for j in range(1, num_cols-1):
			if(canny.item(i, j, 0) == 0):
				linePoints = getLine(gray, i, j)
				for pt in linePoints:
					votes[pt[0]][pt[1]] += 1
	# print(votes)
	#scale resulting image based on votes
	maxValue, maxLocation = maximums(votes)
	res = gray.copy()
	

	# print(votes)
	# print(m)
	for i in range(0, num_rows):
		for j in range(0, num_cols):
			v = votes[i][j]
			if(v < maxValue):
				p = votes[i][j] * 255 / maxValue 
				setPixel(res, i, j, (p,p,p))
			else:
				for di in range(-2, 3):
					for dj in range(-2, 3):
						setPixel(res, i+di, j+dj, RED_PIXEL)

	return (res, votes)

def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

def circle(image, center, radius):
	img = image.copy()
	num_rows = img.shape[0]
	num_cols = img.shape[1]
	for i in range(2, num_rows-2):
		for j in range(2, num_cols-2):
			if(abs(distance(center, (i,j)) - radius) < 500):
				setPixel(img, i, j, RED_PIXEL)
			else:
				setPixel(img, i, j, WHITE_PIXEL)
	return img

def drawCircle(gray, maxValue, maxLocation):
	img = gray.copy()
	num_rows = img.shape[0]
	num_cols = img.shape[1]
	radii = {}
	for i in range(2, num_rows-2):
		for j in range(2, num_cols-2):
			line = getLine(gray, i, j)
			if(maxLocation in line):
				d = abs(distance(maxLocation, (i,j)))
				if(d in radii):
					radii[d] += 1
				else:
					radii[d] = 1
	print(radii)

	radiusGuess = max(radii.iterkeys(), key=(lambda key: radii[key]))

	return circle(img, maxLocation, radiusGuess)

def calcD(x, y, theta):
	return (y * cos(theta) - x * sin(theta))

def pointsFromDTheta(d, theta):
	x = cos(radians(theta))
	y = sin(radians(theta))
	if y == 0:
		return ((float(x) * d, float(y) * d), (float(x+1000) * d, float(y) * d))
	# print("not just doing a flat slope")
	slope = float(x)/float(y)
	# print(x, y, slope)
	return (((float(x) * d),(float(y) * d)), (float(x+1000) * d, float((x + 1000) * slope * d)))
	#(x-1000, slope * (x - 1000))

def scale(num_votes, max_votes):
	return 255 * num_votes / max_votes

def lineDetection(image):
	img = image.copy() #both are canny2 images
	num_rows = img.shape[0]
	num_cols = img.shape[1]
	poll = {}
	for x in range(0, num_rows):
		for y in range(0, num_cols):
			for theta in range(0, 180, 10):
				d = calcD(x, y, theta)
				dt = (d, theta)
				if poll.has_key(dt):
					poll[dt] += 1
					#print("upserted")
				else:
					poll[dt] = 1
					#print("inserted")

				# poll[(d, theta)] = poll.get((d, theta), 0) + 1
	print(poll)
	maxDTheta = max(poll.iterkeys(), key=(lambda key: poll[key]))
	print(maxDTheta, poll[maxDTheta])
	width = sqrt(num_rows * num_rows + num_cols * num_cols)
	huffTransform = np.zeros((180, width, 3), np.uint8)
	for key, value in poll.iteritems():
		d, theta = key
		num_votes = value
		c = (scale(num_votes, poll[maxDTheta]))
		p1, p2 = pointsFromDTheta(d, theta)
		p3 = (int(p1[0]), int(p1[1]))
		p4 = (int(p2[0]), int(p2[1]))
		print(p1, p2, p3, p4, c)
		#p3 and c are no good
		# cv2.line(huffTransform, p3, p4, (c,(c),(c)))
		cv2.line(huffTransform, (0, 0), (100, 100), (0, 0, 0))
	# for theta in (0, 180, 30):
	# 	for d in (0, width):
	# 		dt = (d, theta)
	# 		if poll.has_key(dt):
	# 			num_votes = poll[dt]
				
	# 			imageGraph = np.zeros()
	#huff transform
	# maxVotes = max(poll.iterkeys(), key=(lambda key: poll[key]))
	# for theta in (0, 180):
	# 	for d in (0, sqrt(num_rows * num_rows + num_cols * num_cols)):
	# 		num_votes = poll[(d, theta)]
	# 		c = scale(num_votes, maxVotes)
	# 		p1, p2 = pointsFromDTheta(d, theta)
	# 		cv2.line(img, p1, p2, (c,c,c))
	# 		#img = drawDTheta(img, d, theta, (c, c, c))
	return huffTransform

	# dthetas = sorted(poll, key=poll.get)
	# for dtheta in dthetas:
	# 	d = dtheta[0]
	# 	theta = dtheta[1]
	# 	draw(img)

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

linedetection_image = lineDetection(canny2_image)
cv2.imshow('linedetection_image', linedetection_image)
# cv2.imshow('cannydiff_image', (canny1_image ^ canny2_image))

#circle stuff:
# lined_image, polls = drawLines(canny2_image, gray_image)

# cv2.imshow('line_image', lined_image)
# cv2.imwrite("lined_image.jpg", lined_image)

# maxValue, maxLocation = maximums(polls)
# circle_image = drawCircle(gray_image, maxValue, maxLocation) #should you only calculate on edges or calculate everywhere?
# cv2.imshow('circle_image', circle_image)
# cv2.imwrite("circle_image.jpg", circle_image)

keystroke()