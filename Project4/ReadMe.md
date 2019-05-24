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
### 7.  Learning Rate</br>
* Learning rate is the rate at which the parameters are adjusting such that the error is reduced.
* It can also be visualized as the steps that a gradient descent or any similar loss minimization algorithm adjusts its weights, step by step.
### 8.  Kernels and how do we decide the number of kernels</br>
* Kernals are the filters or feature extractors, that are used to extract the significant features.*
* The Number of kernals is decided based on the number of channels that we are expecting to extract or the number of classes that are required to be clasified.
### 9.  Batch Normalization</br>
* Batch Normalization is used to normalize the values of the kernals such that all of them fall into a similar range/scale.
* This useful because if the activation in the hidden layers are of different magnitudes, then the learning will be uneven for few features.
* Batch normalization is can be on the channels or on the kernals.
### 10.  Image Normalization</br>
* Image normalization is the concept of computer vision domain, which is used to enhance the images which have bad contrast etc..
* The image is enhanced as the all the values are normailised based on difference between the highest and least contrast values.
* This is also the techinque similar to histogram normalization
### 11.  Position of MaxPooling</br>
* MaxPooling is used to reduce the size of the image to 25% considering the 2x2 filter which gives the maximum value of the 4 pixels.
* It helps in reducing the number of convolutions required, without compromizing much on the image information.
* But if the Maxpooling is done in the initial layers of the convolution, then there is possibility of loosing of whatever the kernals have learnt till that level.
* so Postion of maxpooling is suggested to be at a place where at least the edges & gradients have been extracted. (normally at receptive feild of 9 or 11)
* This inturn depends on the image size as well.

### 12.  Concept of Transition Layers</br>
* Transition layers or Transition blocks are nothing but the different other type of operations that are performed on images between convolution layers or convolution blocks.
* For example, Batch Normalization, Maxpooling, dropouts, 1x1 convolution, average pooling etc..
### 13.  Position of Transition Layer</br>
* Transition layers are placed between convolution blocks or convolution layers.
* They should not be used before the last prediction layer.
### 14.  Number of Epochs and when to increase them</br>
* Epochs are the iterations of the training of the model, one epoch / iteration is the model scanning through all the training data one time.
* Number of epochs determine how much the model is learning.
* we can increase the number of epochs as long as the loss is reducing and the train accuracy is improving.
* once the model has reached a state of over-fitting/ underfitting & the train accuracy is not improving anymore, the loss is not reducing, then there is no use of increasing the epochs.
### 15.  DropOut</br>
* Dropout is the concept where few of the neurons are neglected when extracting features to the next layer.
* As few neurons are ignored, there is a forced need on the other neurons to do the prediction on their own, to try not to reduce the accuracy.
* This makes the neurons learn better.
* Also, this prevents the model to overfit, as the training accuracy is reduced a little & provides scope for learning.
### 16.  When do we introduce DropOut, or when do we know we have some overfitting</br>
* When the loss is not reducing any further & the accurcy is not improving any further, it means model is not learning.
* In this case dropout can be used.
* We know that the model is overfitting when the training accuracy is more & the test accuracy is lagging.
### 17.  The distance of MaxPooling from Prediction</br>
* MaxPooling should not be very close to the prediction layers, because as we know maxpooling is reducing the information to 25% of existing information.
* So when we are close to prediction, if we loose that much information, the prediction can go wrong.
### 18.  The distance of Batch Normalization from Prediction</br>
* Batch Normalization also should be avoided atleast at the last layer or prediction layer & a layer before it as well.
* The reason for this is also the same, like , Batch normalization is also a way considered as introducing noise, inorder to maintain values at one scale.
* so it is better not to do this at the last two layers, as we may taamper the important information, which is needed for prediction.
### 19.  When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)</br>
* When the object that we need to predict with in a image, cannot be shrinked to very less size like 5x5 or 3x3, i.e only very few number of pixels do not carry much useful data, after so many convolutions.
* So it is best to stop convolutions when you reached a very small size like 5x5 or 3x3, and use a bigger kernal like 5x5x or 7x7.
* The other alternatives are using a pooling layers like Global average pooling.
* One more alternative is using padding = same
### 20.  How do we know our network is not going well, comparatively, very early</br>
* we can analyse the model, by looking at the loss reduction & the differences in accruacy of prediction between epochs
### 21.  Batch Size, and effects of batch size</br>
* Batch size is the number of images that are scanned by the model, before doing a back propagation step.
* Ideally the batch size should be more than the number of distinct classes for prediction.
* depending on GPU capacity, if the batch size is increased, the time taken per epoch reduces.
### 22.  When to add validation checks</br>
* Validation checks can be added, when have reached the best accuracies.
* we can save the best validation accuracy of the model.
### 23.  LR schedule and concept behind it</br>
* Learning rate schedule is used to change the learning rate between the epochs.
* it can be gradually reduced, so that as we approch the minimum loss point, if we reduce the step size or learning rate, we have a better chance to reach global minima, and acheive Good accuracy.

### 24.  Adam vs SGD</br>
* SGD or stochastic gradient descent optimizer is a varient of Gradient descent where the learning rate is constant through the training process. The weights are updated based on the calculations on few random samplefrom the dataset.
* Adam is a Optimizer which is a combination of RMS PROP i.e calculating the Root Mean square averages and in effect adjusts the learning rate automatically.
It consists of parameters beta1 and beta2 which control the Decay in the learing rate. 
