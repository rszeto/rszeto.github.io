---
layout: page
title: Projects
---

{% assign projects_sorted = site.projects | sort: "date" | reverse %}
{% for project in projects_sorted %}
---
## [{{ project.title }}]({{ project.url }})
{{ project.short_desc }}

{% endfor %}