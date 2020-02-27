---
title: HyperCon&#58; Image-To-Video Model Transfer for Video-To-Video Translation Tasks
short_desc: Enabling temporally-consistent style transfer and inpainting via interpolation and aggregation.
date: 2019-12-10
authors: [szetor, mostafa, jungwon, jjcorso]
thumbnail: /images/project_thumbs/umich-placeholder.png
---

<center><img src="{{ site.baseurl }}/images/hypercon.png" /></center>

### Abstract

Video-to-video translation for super-resolution, inpainting, style transfer, etc. is more difficult than corresponding image-to-image translation tasks due to the temporal consistency problem that, if left unaddressed, results in distracting flickering effects. Although video models designed from scratch produce temporally consistent results, training them to match the vast visual knowledge captured by image models requires an intractable number of videos. To combine the benefits of image and video models, we propose an image-to-video model transfer method called Hyperconsistency (HyperCon) that transforms any well-trained image model into a temporally consistent video model without fine-tuning. HyperCon works by translating a synthetic temporally interpolated video frame-wise and then aggregating over temporally localized windows on the interpolated video. It handles both masked and unmasked inputs, enabling support for even more video-to-video tasks than prior image-to-video model transfer techniques. We demonstrate HyperCon on video style transfer and inpainting, where it performs favorably compared to prior state-of-the-art video consistency and video inpainting methods, all without training on a single stylized or incomplete video.

[ [arXiv][arXiv] ]

[arXiv]: https://arxiv.org/abs/1912.04950

### Acknowledgements

This project was completed as part of an internship at Samsung Semiconductor, Inc.

### Preprints

{% include pubs/szeto2019hypercon.html %}
