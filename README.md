# Image_pre-processing
Pre-processing EM images for alignment and machine learning

Extract_tile.py will re-write a stack of tif files as individual images. Stack files are normally collected during a montage acquistion. A CLAHE filter is also applied to images before saving. 

file_renaming.py will allow to re-name all the files in the image folder to match train and mask labels

saveAllTiles.py will extract all tiles from a montage collection and save them as individual tif file. 

crop_file.py will crop a stack of images stored in the input directory and will save them with the same name in another directoy. You have to edit the pixel locations for cropping. 

uint_and_resize.py converts images to unint 8bit and resize. 
uint_and_resize_mask.py resizes the mask images for machine learning. For U-net segmentation make sure that the mask pixel values for one-class segmentation is set to 1. for multi class segmentation each mask pixel value should correspond to the proper class (i.e. 2, 3, 4.)   
