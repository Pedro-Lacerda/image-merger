import matplotlib.pyplot as plt
import cv2

im1 = plt.imread("teste_alinhamento/template.jpg")
im2 = plt.imread("teste_alinhamento/resultado.jpg")

# im1 = cv2.resize(im1,(0,0),None,0.2,0.2)
# im2 = cv2.resize(im2,(0,0),None,0.2,0.2)
# im3 = cv2.resize(im3,(0,0),None,0.2,0.2)

# im1 = cv2.rotate(im1, cv2.ROTATE_90_COUNTERCLOCKWISE)
# im2 = cv2.rotate(im2, cv2.ROTATE_90_COUNTERCLOCKWISE)
# im3 = cv2.rotate(im3, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.figure()
f, axarr = plt.subplots(1, 2)
indx = 0

axarr[indx].imshow(im1)
indx = 1
axarr[indx].imshow(im2)