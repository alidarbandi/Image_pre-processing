# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:46:50 2022

@author: sem
"""

import os
from skimage import io, exposure, util
import numpy as np

in_dir='X:/Images/Andrew/20220207/SESI/'
out_dir='X:/Images/Andrew/20220207/cropped/'


for files in os.listdir(in_dir):
    path= in_dir + files
    print(path)
    if path.endswith('tif'):       
      image=io.imread(path)
      cr_image=image[3402:4815,1547:7022]
      saveName=out_dir+files
      io.imsave(saveName, cr_image)
 
#io.imshow(image)
#io.show()
#print(image.shape)

