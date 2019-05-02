

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np


from scipy import misc
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


df = pd.read_csv('./data/train_responses.csv')

feat = []


for f in df.id:
    img=mpimg.imread('./data/train_imgs/'+f+'.png')
    #gray = rgb2gray(img)
    reszimg = misc.imresize(img, 0.5)
    feat.append(np.asarray(reszimg, dtype=np.float16))


df['feat'] = feat

df.to_pickle('./data/feat_gray.csv')


