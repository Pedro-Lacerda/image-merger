from image_merger import ImageMerger
from matplotlib import pyplot
from matplotlib import image
import numpy as np

#im0 = image.imread("lake0.jpeg")
#im1 = image.imread("lake1.jpeg")
im2 = image.imread("lake2.jpeg")
im3 = image.imread("lake3.jpeg")

#result1 = ImageMerger().merge_images(im0, im1)
#im01 = result1[1]
result2 = ImageMerger().merge_images(im2, im3)
im23 = result2[1]
#result3 = ImageMerger().merge_images(im01, im23)
#im0123 = result3[1]

pyplot.clf()
pyplot.imshow(im23)