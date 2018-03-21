---
title: A Temporally-Aware Interpolation Network for Video Frame Inpainting
short_desc: Filling in missing frames by blending bidirectional predictions with a temporally-aware interpolation network.
date: 2018-03-15
authors: [sunxm, szetor, jjcorso]
thumbnail: /images/project_thumbs/tai.gif
---

<div class="row" style="margin: 20px 0px">
	<div class="col-xs-12 col-sm-10 col-sm-offset-1">
		<div class="embed-responsive embed-responsive-4by3">
		  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/I27HHr3VWjg"></iframe>
		</div>
	</div>
</div>

### Abstract

We propose the first deep learning solution to video frame inpainting, a challenging instance of the general video inpainting problem with applications in video editing, manipulation, and forensics. Our task is less ambiguous than frame interpolation and video prediction because we have access to both the temporal context and a partial glimpse of the future, allowing us to better evaluate the quality of a model's predictions objectively. We devise a pipeline composed of two modules: a bidirectional video prediction module, and a temporally-aware frame interpolation module. The prediction module makes two intermediate predictions of the missing frames, one conditioned on the preceding frames and the other conditioned on the following frames, using a shared convolutional LSTM-based encoder-decoder. The interpolation module blends the intermediate predictions to form the final result. Specifically, it utilizes time information and hidden activations from the video prediction module to resolve disagreements between the predictions. Our experiments demonstrate that our approach produces more accurate and qualitatively satisfying results than a state-of-the-art video prediction method and many strong frame inpainting baselines.

<center><img src="{{ site.baseurl }}/images/tai.png" width="80%" /></center>

[ [arXiv][arXiv] ]

[arXiv]: https://arxiv.org/abs/1803.07218

### Preprints

{% include pubs/sun2018temporally.html %}
