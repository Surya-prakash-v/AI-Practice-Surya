># Assignment 1B
>### What are Channels and Kernels (according to EVA)?
> #### Channels:
>  Channels are similar features which can be grouped together. In deep learning, the neural networks determine what these similar features are and then groups them together.</br>
**Examples:** Eyes, facial features could get grouped together into a channel.
> #### Kernals:
>  Kernals are the filters which are used to perform convolution operations.</br>
They are also called feature extractors. </br>
When a kernal of size 'n' convoles on an image of size 'I', then the resultant image will be of size 'I-(n-1)'.</br></br>
>### Why should we only (well mostly) use 3x3 Kernels?
> We should use 3x3 kernals only because, the number of parameters that needs to be figured out by the network will be significantly less, comared to any other higher order filters.</br>
**Example:** Instead of using 5x5 filter over a 5x5 image which consumes 25 parameters, we can use 3x3 filter 2 times, to get the same result with 18 parameters only.</br></br>
We cannot use even filters like 2x2 or 4x4, as we cannot arrive at a singular midpoint for these filters, so deciding the accurate output is not possible.</br></br>
>### How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations)
>We need to perform convolution 99 times...</br></br>
199 ->  197 ->  195 ->  193 ->  191 ->  189 ->  187 ->  185 ->  183 ->  181 ->  179</br>
179 ->  177 ->  175 ->  173 ->  171 ->  169 ->  167 ->  165 ->  163 ->  161 ->  159</br>
159 ->  157 ->  155 ->  153 ->  151 ->  149 ->  147 ->  145 ->  143 ->  141 ->  139</br>
139 ->  137 ->  135 ->  133 ->  131 ->  129 ->  127 ->  125 ->  123 ->  121 ->  119</br>
119 ->  117 ->  115 ->  113 ->  111 ->  109 ->  107 ->  105 ->  103 ->  101 ->  99</br>
99 ->  97 ->  95 ->  93 ->  91 ->  89 ->  87 ->  85 ->  83 ->  81 ->  79</br>
79 ->  77 ->  75 ->  73 ->  71 ->  69 ->  67 ->  65 ->  63 ->  61 ->  59</br>
59 ->  57 ->  55 ->  53 ->  51 ->  49 ->  47 ->  45 ->  43 ->  41 ->  39</br>
39 ->  37 ->  35 ->  33 ->  31 ->  29 ->  27 ->  25 ->  23 ->  21 ->  19</br>
19 ->  17 ->  15 ->  13 ->  11 ->  09 ->  07 ->  05 ->  03 ->  01 </br>
