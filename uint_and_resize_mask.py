# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:49:52 2022

@author: sem
"""


import os
from skimage import io, exposure, util
from PIL import Image,ImageEnhance
from torch.utils.data import Dataset
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import cv2
import numpy as np

in_dir = 'Z:/Images/Maynes/April 4/DS2_clean/' 
outdir = 'Z:/Images/Maynes/April 4/DS2_resize/' 



# loop through stacks in directory
for files in os.listdir(in_dir):
           
   path = in_dir + files
   cimage = cv2.imread(path)
   cimage = cv2.cvtColor(cimage, cv2.COLOR_BGR2GRAY)
 #  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#   oimg = clahe.apply(cimage)
   nci=np.array(cimage)
   nci[nci==2]=1
   print (np.unique(nci))
   print(np.shape(nci))
   print(nci.dtype)
#   img8 = cv2.normalize(nci, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  
   small = cv2.resize(nci, (2000,2000), fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
   
   tilename=files
   print(tilename)
   saveName=outdir+tilename
   cv2.imwrite(saveName, small)
   

   
 