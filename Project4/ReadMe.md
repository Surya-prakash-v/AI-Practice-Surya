# Architectural Basics</br>
### 1.  How many layers</br>
* The number of layers in a CNN depends on the size of the input image and the content that we want to detect
* we need to add as many convolution layers needed, until we read the complete image
### 2.  MaxPooling</br>
* Max pooling is taking the maximum number/pixel value to the next layer. For a 2x2 Maxpool size, it results the maximum pixel value of the 4 pixels
* Max Pooling there by reduces the image size by half, but retains the Loudest information from the pixels
* This helps by reducing the number of convolution layers required to read the entire image
### 3.  1x1 Convolutions</br>
### 4.  3x3 Convolutions</br>
### 5.  Receptive Field</br>
### 6.  SoftMax</br>
### 7.  Learning Rate></br>
### 8.  Kernels and how do we decide the number of kernels</br>
### 9.  Batch Normalization</br>
### 10.  Image Normalization</br>
### 11.  Position of MaxPooling</br>
### 12.  Concept of Transition Layers</br>
### 13.  Position of Transition Layer</br>
### 14.  Number of Epochs and when to increase them</br>
### 15.  DropOut</br>
### 16.  When do we introduce DropOut, or when do we know we have some overfitting</br>
### 17.  The distance of MaxPooling from Prediction</br>
### 18.  The distance of Batch Normalization from Prediction</br>
### 19.  When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)</br>
### 20.  How do we know our network is not going well, comparatively, very early</br>
### 21.  Batch Size, and effects of batch size</br>
### 22.  When to add validation checks</br>
### 23.  LR schedule and concept behind it</br>
### 24.  Adam vs SGD</br>
