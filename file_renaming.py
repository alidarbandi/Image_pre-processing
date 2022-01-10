# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:24:57 2022

@author: sem
"""



import os
from skimage import io, exposure, util
#from matplotlib import pyplot as plt
import numpy as np

in_dir = 'Z:/Images/Ali/Human Liver/Nov 17/Unet/training_mask/' 
outdir = 'Z:/Images/Ali/Human Liver/Nov 17/Unet/training_mask_r/'



# loop through stacks in directory
for files in os.listdir(in_dir):
     
              
         path = in_dir + files
      
         im=io.imread(path)
         tilename='Hela_cropped'+files[9:]
         print(tilename)
         saveName=outdir+tilename
         io.imsave(saveName,im)
 
