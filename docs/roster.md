---
layout: default
title: Roster
permalink: /roster/
body_class: roster-page
---

# The roster

Drafted September 5, 2026, from the #7 slot. The table regenerates from Sleeper after every data pull. The notes are mine.
{:.sub}

<table class="roster roster-notes">
  <thead>
    <tr><th>Slot</th><th>Player</th><th class="th-note">Notes</th></tr>
  </thead>
  <tbody>
{% assign prev_slot = "" %}
{% for r in site.data.roster %}
    <tr>
      <td class="slot{% if r.slot == prev_slot %} dim{% endif %}">{{ r.slot }}</td>
      <td class="player">{{ r.player }}<span class="meta">{{ r.pos }} · {{ r.team }}{% if r.status != "" %} · <span class="status">{{ r.status }}</span>{% endif %}</span></td>
      <td class="note">{{ site.data.notes[r.player] }}</td>
    </tr>
{% assign prev_slot = r.slot %}
{% endfor %}
  </tbody>
</table>
