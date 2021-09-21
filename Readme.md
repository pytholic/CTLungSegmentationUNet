# Project description

In this project, we will per form lung segmentation on 3D CT volumes using 2D UNet architecture. 

## Dataset
We use 150 CT volumes (75 patients) for training, 20 volumes (10 patients) for validation and 12 volumes for testing predictions. Note that dataset is separated on subject-level and not volume-level to keep the evaluation unbiased.

## Mask Generation
To generate the segmentation label mask, we used 3D slicer software along with NVidia AI Assisted Annotation tool (can be installed as an extension in 3D slicer) to speed up the process. Manual segmentation on each slice for 170 volumes can take forever. Thanks to NVidia researchers for developing this tool which helped me to generate these masks in 2 days instead of months.

## Data preprocessing
First of all convert 3D data into 2D slices and store them. The code is provided in 'Data preprocessing' notebook. Set your data paths accordingly. The resulting dataset consisted of 176,884 slices for  training and 23,298 slices for validation purpose.

## Training
Before starting training, make sure your data structure looks like this.

```
|-- data_slices
    |-- train
        |-- masks
            |-- img
        |-- slices
            |-- img
            
    |-- valid
        |-- masks
            |-- img
        |-- slices
            |-- img
```

After that we can prepare our UNet mdoel and train it on our dataset. We can also visualize our models predictions on the validation dataset. The code is provided in the 'Model training' notebook.

## Prediction
We can use also make and visualize predicitons on the test data. The notebooks are provided.
