---
layout: default
title: Column
permalink: /column/
body_class: column-page
---

# The column

Weekly write-ups, published after the games are cold. Superlatives included.
{:.column-intro}

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">
      <div class="date">{{ post.date | date: "%Y-%m-%d" }}</div>
      <h2>{{ post.title }}</h2>
      <p>{{ post.excerpt | strip_html | strip }}</p>
    </a>
  </li>
{% endfor %}
</ul>
