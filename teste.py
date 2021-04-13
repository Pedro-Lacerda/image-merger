from image_merger import ImageMerger
from matplotlib import pyplot
from matplotlib import image
import numpy as np

im = image.imread("duck.jpg")

#pyplot.imshow(im)

result = ImageMerger().slice_image(im, 36, 1)

im1 = result[0]
im2 = result[1]
im3 = result[2]
im4 = result[3]

result2 = ImageMerger().merge_images(im1, im2)[1]
result3 = ImageMerger().merge_images(im3, im4)[1]
result4 = ImageMerger().merge_images(result2, result3)[1]

pyplot.clf()

pyplot.figure()
f, axarr = pyplot.subplots(1, 3)
axarr[0].imshow(result2)
axarr[1].imshow(result3)
axarr[2].imshow(result4)

