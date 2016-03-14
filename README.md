# time-series-classification
Short and long time series classification via convolutional neural networks

In this project, we present a novel framework for time series classification, which is based on 
Gramian Angular Summation/Difference Fields and Markov Transition Fields (GAF-MTF), a recently published 
image feature extraction method. A convolutional neural network (CNN) was employed as the classifier. 
This framework enables the use of CNN to learn high-level features and classify time series. 
Its performance was evaluated on 16 standard datasets. Experiment results show that our framework outperforms 
or achieves the same level at least with the GAF-MTF+Tiled CNN framework on 14 of the 16 datasets. 
And it obtained competitive performance compared with other 8 representive approaches. 
Furthermore, we compared the performance of GAF-MTF feature with other 5 image features on a large-scale cough dataset. 
Results indicates that the GAF-MTF feature is not suitable for large-scale cough datasets 
while its competitive performance on the standard datasets.

## Image features extraction
### Short time series
Image features for short time series:

- GASF

 <img src="images-source/gaf-mtf/gasf.png"/>
- GADF

 <img src="images-source/gaf-mtf/gadf.png"/>
- MTF

 <img src="images-source/gaf-mtf/mtf_64.png"/>

### Large-scale cough dataset
Image features for cough dataset:

- Comparision of the six image features:

  <img src="images-final/six-features.png"/>

## CNN
- Framework for short time series classification:

 <img src="images-final/cnn.png"/>
- AlexNet/CaffeNet

 <img src="images-final/caffenet.jpg"/>

## Results
- short time series classification:

 <img src="images-final/results.png"/>
- long time series classificaiton:

 <img src="images-final/result2.png"/>

## Appendix
Dataset information:
- Short: [UCR Time Series Classification Archive](http://www.cs.ucr.edu/~eamonn/time_series_data/)
- Long: [Cough dataset from Tongji Hospital](http://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/1472-6947-15-S4-S2)
 
Software Links:
- [Caffe: deep learning framework](http://caffe.berkeleyvision.org/)
- [RASTAMAT](http://labrosa.ee.columbia.edu/matlab/rastamat/)

This project is partly motivated by @Zhiguang Wang, who is the author of "Imaging Time-Series to Improve Classification 
and Imputation". He provided me the source code to extract GASF-GADF-MTF features and pointed out that "The tiled CNN is 
not the best one and the TICA pre-training stage seems unnecessary". His advice helped us save a great deal of time. 
Thanks for his kindness and if you use this repository for GAF/MTF feature extraction, please cite the work in your publication:
```
@inproceedings{Wang:2015:ITI:2832747.2832798,
 author = {Wang, Zhiguang and Oates, Tim},
 title = {Imaging Time-series to Improve Classification and Imputation},
 booktitle = {Proceedings of the 24th International Conference on Artificial Intelligence},
 series = {IJCAI'15},
 year = {2015},
 isbn = {978-1-57735-738-4},
 location = {Buenos Aires, Argentina},
 pages = {3939--3945},
 numpages = {7},
 url = {http://dl.acm.org/citation.cfm?id=2832747.2832798},
 acmid = {2832798},
 publisher = {AAAI Press},
}
```
