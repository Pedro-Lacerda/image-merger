import cv2
import os

# Determina o caminho da pasta principal que contem as subpastas 
# com cada conjunto de imagens
mainFolder = 'Images'
myFolders = os.listdir(mainFolder)

# Le cada imagem dentro das pastas e guarda em uma lista
for folder in myFolders:
    path = mainFolder +'/'+folder
    images =[]
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        
        # Se descomentada, redimensiona as imagens para acelerar 
        # o processamento
        
        # curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
        images.append(curImg)

    # Define a classe 'stitcher' e faz a mesclagem das imagens
    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        # Salva e a mostra na tela a imagem resultante
        cv2.imwrite("output_"+folder+".jpg", result)
        print('Panorama Generated')
        cv2.imshow(folder,result)
        cv2.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')

cv2.waitKey(0)