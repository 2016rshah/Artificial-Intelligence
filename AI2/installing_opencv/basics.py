import cv2

def main():
    filename = input("What is the filename for the image")
    if filename.length == 0:
        filename = "prof-pic2.jpg"
    img = cv2.imread(filename, 0)
    cv2.imshow('image', img)
    #k = cv2.waitKey(0)
    #if k == 27:
    #    cv2.destroyAllWindows()
    
