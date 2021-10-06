import cv2

def nothing(x):
    pass

img = cv2.imread("disaster_dataset/landslide_oso_2014_far.jpg")
res = cv2.resize(img,(0,0),None,0.7,0.7)
cv2.namedWindow('canny')
switch = '0: OFF \n1 : ON'
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)
cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)
cv2.createTrackbar("blur_size", 'canny', 0, 255, nothing)
cv2.createTrackbar("blur_amp", 'canny', 0, 255, nothing)

while(1):
    lower = cv2.getTrackbarPos('lower','canny')
    upper = cv2.getTrackbarPos('upper','canny')
    s = cv2.getTrackbarPos(switch,'canny')
    blur_size = cv2.getTrackbarPos("blur_size",'canny')
    blur_amp = cv2.getTrackbarPos("blur_amp",'canny')
    
    img_blurred = cv2.GaussianBlur(res.copy(), (blur_size * 2 + 1,
                                                    blur_size * 2 + 1), blur_amp)
    if s == 0:
        edges = res
    else:
        edges = cv2.Canny(img_blurred,lower,upper)
    cv2.imshow('canny',edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 
cv2.destroyAllWindows()