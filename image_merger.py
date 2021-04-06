import os
import glob
import subprocess

import numpy as np
from matplotlib import pyplot as plt


class ImageMerger():
    """Este módulo é responsável pela solução do primeiro problema de
    imageamento.

    Aleḿ disso, possui alguns modulos adicionais que deixei para serem
    utilizados em experimentos. A função "merge_image_set" representa a
    solução de primero. Com as imagens em mãos, basta jogar uma lista
    ordenada para esta função e ela resolve o problema.
    """

    def __init__(self):
        pass

    def slice_image(self, img, lsz, overlap):
        """Essa função peag uma imagem e corta ela em várias imagens
        sobrepostas em cadeia.

        Recebe a imagem, o parâmetro lsz que indica o tamanho das
        imagens finais e o overlap, que define quantos pixels cada
        imagem vai compartilhar.
        """
        if lsz <= overlap:
            raise Exception('LSZ must never be >= overlap')
        i = 0
        indx = 0
        imgs = []
        while i+lsz < img.shape[1]:
            imgs.append(img[:, i:i + lsz])
            i = i + lsz - overlap
            indx = indx + 1
        print('Sliced img into', len(imgs), 'pieces')
        print('Lost', round((img.shape[1] - i) / img.shape[1], 2),
              '% of original img')
        plt.figure()
        f, axarr = plt.subplots(1, len(imgs))
        indx = 0
        for img in imgs:
            axarr[indx].imshow(imgs[indx])
            indx = indx + 1
        return imgs

    def merge_images(self, img1, img2):
        """Essa função recebe duas imagens para serem juntadas, a primeira
        imagem deve estar numa posição igual ou mais à esquerda que a segunda.

        Demora pra rodar!
        """
        width = img2.shape[1]
        height = img1.shape[0]
        width_img_1 = img1.shape[1]
        best_d = 0
        best_d_diff = 1000000
        index_d = None
        pics = []

        for i in range(0, width):
            diff_sum = 0
            print_img = []

            for y in range(0, height):
                print_img_row = list(img1[y][:-(width_img_1-i)])

                for x in range(0, width - i):
                    pixel_1 = img1[y][width_img_1 - (width - i) + x]
                    pixel_2 = img2[y][x]
                    pix_diff = pixel_1 - pixel_2
                    val = int(sum(pix_diff) / 3)
                    pix_diff = list(map(lambda x: x**2, pix_diff))
                    diff_sum = sum(pix_diff)**0.5
                    
                    if np.all(pix_diff) <= 1:
                        print_img_row.append(pixel_1)
                    else:
                        print_img_row.append([val, val, val])

                for pix in img2[y][(width - i):]:
                    print_img_row.append(pix)
                print_img.append(print_img_row)

            diff = float(diff_sum) / (float(height)
                                      * (float(width) - float(i)))

            print('d:', i, '\tdiff_sum:', diff_sum, '\tarea: ',
                  float(height) * (float(width) - float(i)), '\tdiff:', diff)

            print_img = np.array(print_img)
            pics.append(print_img)

            if diff < best_d_diff:
                best_d = i
                best_d_diff = diff
                index_d = len(pics) - 1

        return best_d, pics[index_d]
    

    def generate_video(self, imgs, framerate=30, name='video'):
        """Recebe uma lista de imagens e gera um vídeo com as imagens em
        sucessão.

        Nota: você deve ter o ffmpeg instalado numa máquina linux
        """
        for i in range(len(imgs)):
            fig, ax = plt.subplots(figsize=(20, 10))
            ax.imshow(imgs[i])
            plt.savefig("file%02d.png" % i)

        subprocess.call([
            'ffmpeg', '-framerate', str(framerate), '-i', 'file%02d.png',
            '-r', '100', "{}.mp4".format(name)])

        for file_name in glob.glob("*.png"):
            os.remove(file_name)

    def merge_image_set(self, imageset):
        """Recebe uma lista de imagens (ordenada pelas tiradas da esquerda para
        a direita) e retorna a união de todas elas.

        Demora muito pra rodar!
        """
        endimage = None
        for image in imageset:
            if endimage is None:
                endimage = image
            else:
                _, endimage = self.merge_images(endimage, image)
        return endimage
