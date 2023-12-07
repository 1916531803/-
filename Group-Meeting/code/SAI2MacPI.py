import imageio
from PIL import Image
import numpy as np
import os

def SAI2MacPI(SAI_PNG_PATH, MacPI_PNG_PATH, u, v, h, w):
    lf = np.zeros(shape=(u, v, h, w, 3), dtype=int)
    for i in range(u*v):
        temp = imageio.imread(SAI_PNG_PATH + '/f_b_0%.2d.png' % (i+1))
        lf[i // u, i - v * (i // u), :, :, :] = temp
    u, v, h, w, c = lf.shape

    MacPI = np.zeros(shape=(u*h, v*w, 3), dtype=int)
    for i in range(u*h):
        for j in range(v*w):
            MacPI[i, j, :] = lf[i%u, j%v, i//u, j//v, :]
    MacPI = Image.fromarray(MacPI.astype('uint8'))
    if not os.path.exists(MacPI_PNG_PATH):
        os.makedirs(MacPI_PNG_PATH)
    Image_name = SAI_PNG_PATH.split("/")[-1]
    MacPI.save(MacPI_PNG_PATH + '/' + Image_name + '.png')


if __name__ == '__main__':
    SAI_PNG_PATH = "C:/Users/Harrison/Desktop/GEO/data/decode/occlusions_1_eslf/RA37"
    MacPI_PNG_PATH = "C:/Users/Harrison/Desktop/GEO/data/decode/occlusions_1_eslf/RA37"
    Input_Anger_U = 7
    Input_Anger_V = 7
    Input_Spati_H = 368
    Input_Spati_W = 536

    SAI2MacPI(SAI_PNG_PATH, MacPI_PNG_PATH, Input_Anger_U, Input_Anger_V, Input_Spati_H, Input_Spati_W)