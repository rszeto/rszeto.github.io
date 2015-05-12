---
layout: page
title: Projects
---

Below is a list of my projects.

{% for project in site.projects %}
## [{{ project.title }}]({{ project.url }})
{{ project.short_desc }}

{% endfor %}