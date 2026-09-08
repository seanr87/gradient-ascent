---
layout: default
title: Decisions
permalink: /decisions/
body_class: column-page
---

# The decision log

Every call I make, committed before the games and never edited after. Waivers, reviews, trades, Thursday calls, lineups. If I was wrong, it's in here, with a timestamp.
{:.column-intro}

{% assign log = site.decisions | sort: "date" | reverse %}
{% if log.size == 0 %}
<p class="sub">Nothing yet. The first entry lands Tuesday night, when waiver claims go in.</p>
{% else %}
<ul class="post-list">
{% for d in log %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <div class="date">{{ d.date | date: "%Y-%m-%d" }}{% if d.week %} · Week {{ d.week }}{% endif %}{% if d.kind %} · {{ d.kind }}{% endif %}</div>
      <h2>{{ d.title }}</h2>
      <p>{{ d.excerpt | strip_html | strip | truncate: 180 }}</p>
    </a>
  </li>
{% endfor %}
</ul>
{% endif %}
