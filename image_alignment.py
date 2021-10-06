import numpy as np
import imutils
import cv2

def align_images(image, template, maxFeatures=500, keepPercent=0.2,
	debug=False):
    # Converte as imagens pra escala de cinza
	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Extracao de features nas duas imagens por meio do metodo ORB
	orb = cv2.ORB_create(maxFeatures)
	(kpsA, descsA) = orb.detectAndCompute(imageGray, None)
	(kpsB, descsB) = orb.detectAndCompute(templateGray, None)
    
	# Faz o pareamento das features entre as duas imagens
	method = cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
	matcher = cv2.DescriptorMatcher_create(method)
	matches = matcher.match(descsA, descsB, None)
    
    # Ordena os pares pela distancia (menor distância = maior semelhanca)
	matches = sorted(matches, key=lambda x:x.distance)
    
	# Mantem os melhores pares e descarta o resto
	keep = int(len(matches) * keepPercent)
	matches = matches[:keep]
    
	# Checar a condicao de debug
	if debug:
		matchedVis = cv2.drawMatches(image, kpsA, template, kpsB,
			matches, None)
		matchedVis = imutils.resize(matchedVis, width=1000)
		cv2.imshow("Matched Keypoints", matchedVis)
		cv2.waitKey(0)
        
    # Aloca memória para as coordenadas dos keypoints para gerar a matriz
    # de homografia
	ptsA = np.zeros((len(matches), 2), dtype="float")
	ptsB = np.zeros((len(matches), 2), dtype="float")
    
	# Faz um loop pelos pares
	for (i, m) in enumerate(matches):
        # Indica que as coordenadas nas duas imagens representam o mesmo ponto
		ptsA[i] = kpsA[m.queryIdx].pt
		ptsB[i] = kpsB[m.trainIdx].pt
        
    # Computa a matriz de homografia
	(H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)
    
	# Usa a matriz para alinhar os pontos
	(h, w) = template.shape[:2]
	aligned = cv2.warpPerspective(image, H, (w, h))
    
	# Retorna a imagem final
	return aligned

#-------------- codigo para testar a função --------------

img = cv2.imread("disaster_dataset/earthquake_petobo_2018.jpg")
temp = cv2.imread("disaster_dataset/earthquake_petobo_2017.jpg")

img = cv2.resize(img,(0,0),None,0.2,0.2)
temp = cv2.resize(temp,(0,0),None,0.2,0.2)

align = align_images(img,temp)

cv2.imshow("align", align)
cv2.waitKey(0)