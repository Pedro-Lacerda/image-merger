# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import imutils
import cv2

# load the two input images
imageA = cv2.imread("disaster_dataset/landslide_oso_2013_far.jpg")
imageB = cv2.imread("disaster_dataset/landslide_oso_2014_far.jpg")

# imageB = cv2.resize(imageB,(imageA.shape[1],imageA.shape[0]))

imageA = cv2.resize(imageA,(0,0),None,0.5,0.5)
imageB = cv2.resize(imageB,(0,0),None,0.5,0.5)

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

#apply gaussian blurr
blurr = 17
blurredA = cv2.GaussianBlur(grayA, (blurr, blurr), 0)
blurredB = cv2.GaussianBlur(grayB, (blurr, blurr), 0)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = ssim(blurredA, blurredB, full=True)
diff = (diff * 255).astype("uint8")

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
 	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# thresh = cv2.adaptiveThreshold(diff, 255,
#  	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)[1]
# thresh = cv2.adaptiveThreshold(diff, 255,
# 	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)[1]

#apply an opening in the threshhold mask
opening = 6
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opening,opening))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)