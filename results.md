---
title: "Results"
---
{% assign sortedPages = site.pages | sort: 'title' %}
<ul>
{% for p in sortedPages %}
{% if p.dir == "/results/" %}
<li><a href="{{p.url}}">{{ p.title }}</a></li>
{% endif %}
{% endfor %}
</ul>