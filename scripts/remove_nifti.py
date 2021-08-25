'''Script to remove extra nifti files and keep only one per patient'''
''' Need to do it manually. String names are not consistent..'''

import os
import glob

path = 'E:/skia_projects/ct_segmentation_3d/temp'
for folder in os.listdir(path):
	path_patient = os.path.join(path, folder)
	for nifti in glob.glob(path_patient + '/*'):
		if ("3_") not in nifti:
			os.remove(nifti)
			


