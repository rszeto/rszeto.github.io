---
title: HyperCon&#58; Image-To-Video Model Transfer for Video-To-Video Translation Tasks
short_desc: Enabling temporally-consistent style transfer and inpainting via interpolation and aggregation.
date: 2020-11-21
authors: [szetor, mostafa, jungwon, jjcorso]
thumbnail: /images/project_thumbs/hypercon.gif
---

<div class="row" style="margin: 20px 0px">
	<div class="col-xs-12 col-sm-10 col-sm-offset-1">
		<div class="embed-responsive embed-responsive-16by9">
		  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/FvHAPShgtNI" allowfullscreen></iframe>
		</div>
	</div>
</div>

### Abstract

Video-to-video translation is more difficult than image-to-image translation due to the temporal consistency problem that, if unaddressed, leads to distracting flickering effects. Although video models designed from scratch produce temporally consistent results, training them to match the vast visual knowledge captured by image models requires an intractable number of videos. To combine the benefits of image and video models, we propose an image-to-video model transfer method called Hyperconsistency (HyperCon) that transforms any well-trained image model into a temporally consistent video model without fine-tuning. HyperCon works by translating a temporally interpolated video frame-wise and then aggregating over temporally localized windows on the interpolated video. It handles both masked and unmasked inputs, enabling support for even more video-to-video translation tasks than prior image-to-video model transfer techniques. We demonstrate HyperCon on video style transfer and inpainting, where it performs favorably compared to prior state-of-the-art methods without training on a single stylized or incomplete video.

[ [arXiv][arXiv] ]

[arXiv]: https://arxiv.org/abs/1912.04950

### Acknowledgements

This project was completed as part of an internship at Samsung Semiconductor, Inc.

### Publications

{% include pubs/szeto2021hypercon.html %}
