from image_merger import ImageMerger
from matplotlib import pyplot
from matplotlib import image
import numpy as np

im = image.imread("duck.jpg")

result = ImageMerger().slice_image(im, 72, 1)

im1 = result[0]
im2 = result[1]

#im1 = image.imread("duck5.jpg")
#im2 = image.imread("duck61.jpg")

result2 = ImageMerger().merge_images(im1, im2)
im3 = result2[1]

pyplot.clf()
pyplot.imshow(im3)