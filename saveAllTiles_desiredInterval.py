# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:53:29 2021

@author: Ali Darbandi
"""

import os
from skimage import io, exposure, util

in_dir = 'Z:/Images/Ali/Sept302021/' 
outdir = 'Z:/Images/Ali/Sept302021/sequence/'

# loop through stacks in directory
for stack in os.listdir(in_dir):
    if stack.endswith('0.tif'): # select only .tif
        path = in_dir + stack
        im = io.imread(path) # opens image with skimage into 3d array
        tile_index = 0
        
        # loop through tiles in stack
        for tile in im:
            tile_clahe = exposure.equalize_adapthist(tile, clip_limit=0.03) # perform clahe
            tile_int = util.img_as_uint(tile_clahe) # have to convert from float64 array to int array
            tilename = stack[:-4] # crop '.tif' from the end
            
            saveName = outdir + tilename + '_' + str(tile_index).zfill(2) + '.tif'
            io.imsave(saveName, tile_int)
            tile_index += 1