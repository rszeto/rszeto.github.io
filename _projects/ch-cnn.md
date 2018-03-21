---
title: Click Here&#58; Human-Localized Keypoints as Guidance for Viewpoint Estimation
short_desc: Improving viewpoint estimation by integrating information about a single keypoint.
date: 2017-03-17
authors: [szetor, jjcorso]
thumbnail: /images/project_thumbs/ch-cnn.png
---

<center><img src="{{ site.baseurl }}/images/ch-cnn_motivation.png" width="70%" /></center>

### Abstract

We motivate and address a human-in-the-loop variant of the monocular viewpoint estimation task in which the location and class of one semantic object keypoint is available at test time. In order to leverage the keypoint information, we devise a Convolutional Neural Network called Click-Here CNN (CH-CNN) that integrates the keypoint information with activations from the layers that process the image. It transforms the keypoint information into a 2D map that can be used to weigh features from certain parts of the image more heavily. The weighted sum of these spatial features is combined with global image features to provide relevant information to the prediction layers. To train our network, we collect a novel dataset of 3D keypoint annotations on thousands of CAD models, and synthetically render millions of images with 2D keypoint information. On test instances from PASCAL 3D+, our model achieves a mean class accuracy of 90.7%, whereas the state-of-the-art baseline only obtains 85.7% accuracy, justifying our argument for human-in-the-loop inference.

[ [arXiv][arXiv] \| [code][code] \| [keypoint dataset][keypoint-dataset] ]

[arXiv]: https://arxiv.org/abs/1703.09859
[code]: https://github.com/rszeto/click-here-cnn
[keypoint-dataset]: http://web.eecs.umich.edu/~jjcorso/extdelivery/shapenet-keypoints-1.0.zip

### Publications

{% include pubs/szeto2017click.html %}
