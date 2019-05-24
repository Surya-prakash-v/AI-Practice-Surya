# Architectural Basics</br>
### 1.  How many layers</br>
* The number of layers in a CNN depends on the size of the input image and the content that we want to detect
* we need to add as many convolution layers needed, until we read the complete image
### 2.  MaxPooling</br>
* Max pooling is taking the maximum number/pixel value to the next layer. For a 2x2 Maxpool size, it results the maximum pixel value of the 4 pixels
* Max Pooling there by reduces the image size by half, but retains the Loudest information from the pixels
* This helps by reducing the number of convolution layers required to read the entire image
### 3.  1x1 Convolutions</br>
* 1x1 Convolution is where the Kernal size of just one pixel convolves on each pixel and extracts the significant features of all the channels.
* 1x1 convolution is used to reduce the number of channels.
* This is very advantageous because, it reduces the number of channels and there by number of parameters are reduced & most significant features are retained, while the in significant ones are discarded.
### 4.  3x3 Convolutions</br>
* 3x3 is the most common kind of convolution, used to extract the features to the next layer.
* When 3x3 convolution is used, the input size/channel size, reduces by 2. i.e 100X100 becomes 98x98. (n-2)
* Each pixel of the output is derived from convolution operation on 9 pixels in the input.
### 5.  Receptive Field</br>
* Receptive feild is the number of neurons of previous layer, that can be visible from one pixel of the current layer
* As described above, during 3x3 convolution, the output nueuron will be able to visualized by 9 input pixels. So the Receptive feild is 3
* The concept of Global Receptive feild is the total number of input pixels that can be viewed till the input layer.
* For the accuracy to be good, we need to have the Global receptive feild approximately equal to image size.
### 6.  SoftMax</br>
* Soft max is the function, which calulates the probability like output describing the likelyness of the pridicted class.
* This is calculated exponentially as e^a/(e^a+e^b+e^c).
* Due to this calculation the output is more softened when compared to the classification/pridiction of logits from the penultimate layer 
### 7.  Learning Rate></br>
* Learning rate is the rate at which the parameters are adjusting such that the error is reduced.
* It can also be visualized as the steps that a gradient descent or any similar loss minimization algorithm adjusts its weights, step by step.
### 8.  Kernels and how do we decide the number of kernels</br>
**Kernals are the filters or feature extractors, that are used to extract the significant features.*
* The Number of kernals is decided based on the number of channels that we are expecting to extract or the number of classes that are required to be clasified.
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
