'''Script to convert dicom files to nifti'''


import dicom2nifti
import os
import glob
from tqdm import tqdm

dicomDir = 'E:/skia_projects/ct_segmentation_3d/data'
outDir = 'E:/skia_projects/ct_segmentation_3d/output'

#for i, patient in enumerate(glob.glob(dicomDir + '/*/')):
for i, patient in enumerate(os.listdir(dicomDir)):
	os.mkdir(os.path.join(outDir, '{}'.format(i)))
	dicom2nifti.convert_directory(os.path.join(dicomDir, patient), os.path.join(outDir, '{}'.format(i)), compression=False, reorient=True)

