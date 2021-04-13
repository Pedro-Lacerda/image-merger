from matplotlib import image
import numpy as np

img1 = image.imread("lake1.jpeg")
img2 = image.imread("lake2.jpeg")

width = img2.shape[1]
height = img1.shape[0]
width_img_1 = img1.shape[1]
best_d = 0
best_d_diff = 1000000
index_d = None
pics = []

y=3
i=0

print_img_row = list(img1[y][:-(width_img_1-i)])

pix_diff = img1[2][149]-img2[2][14]