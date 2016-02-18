import cv2

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

def grayImage(img):
	num_rows = img.shape[0]
	num_cols = img.shape[1]

	for i in range(num_rows):
		for j in range(num_cols):
			r = img.item(i, j, 0)
			g = img.item(i, j, 1)
			b = img.item(i, j, 2)
			setPixel(img, i, j, grayPixel(r, g, b)) 
	return img

def blurImage(img):
	num_rows = img.shape[0] - 2
	num_cols = img.shape[1] - 2

	for i in range(1, num_rows):
		for j in range(1, num_cols):
			setPixel(img, i, j, blurPixel(img, i, j))
	return img 

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

location = raw_input("Image location: ")
#if I want to read from URL, do that here. Until them, I treat it as a local url 
image = cv2.imread(location)
cv2.imshow('color_image',image)

gray_image = grayImage(image)
cv2.imshow('gray_image',gray_image)

blur_image = blurImage(gray_image)
cv2.imshow('blur_image',blur_image)

#Escape key to exit
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

