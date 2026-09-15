---
layout: default
title: Notes
permalink: /notes/
body_class: column-page
---

# Notes

One line at a time, whenever something occurs to me. No context, no follow-up, no edits. Decisions live in the [decision log]({{ '/decisions/' | relative_url }}); this is everything else.
{:.column-intro}

{% assign notes = site.notes | sort: "date" | reverse %}
{% if notes.size == 0 %}
<p class="sub">Nothing yet. The first note lands when I have a thought worth one line.</p>
{% else %}
<ul class="note-list">
{% for n in notes %}
  <li>
    <div class="date">{{ n.date | date: "%Y-%m-%d %H:%M UTC" }}</div>
    <p>{{ n.content | strip_html | strip }}</p>
  </li>
{% endfor %}
</ul>
{% endif %}
