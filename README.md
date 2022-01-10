# Image_pre-processing
Pre-processing EM images for alignment and machine learning

Extract_tile.py will re-write a stack of tif files as individual images. Stack files are normally collected during a montage acquistion. A CLAHE filter is also applied to images before saving. 

file_renaming.py will allow to re-name all the files in the image folder to match train and mask labels

saveAllTiles.py will extract all tiles from a montage collection and save them as individual tif file. 

