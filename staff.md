---
title: "Staff"
hidden: true
---
<div class="row">
{% for s in site.data.staff %}
  <div class="col-xl-3 col-md-4 p-5">
    <div class="card m-0 px-10 py-5" style="height: 100%;">
      <h2 class="card-title font-size-16 font-weight-bold">{{ s['Tag'] }}</h2>
      {% if s['Pic URL'] %}
      <img src="{{ s['Pic URL'] }}" class="img-fluid rounded" style="width: 100%; height: auto;">
      {% else %}
      {% assign min = 1 %}
      {% assign max = 85 %}
      {% assign diff = max | minus: min %}
      {% assign randomNumber = "now" | date: "%N" | modulo: diff | plus: min %}
      <img src='/img/staff/staff_{{ randomNumber }}.jpg' class="img-fluid rounded" style="width: 100%; height: auto;">
      {% endif %}
      {% if s['Twitter'] %}
        <i class="fab fa-twitter"></i>
        <a href="https://twitter.com/{{ s['Twitter'] }}">{{ s['Twitter'] }}</a>
      <hr/>
      {% endif %}
      {% if s['Pronouns'] %}
      <p class="text-muted mx-0 my-5"><i>{{ s['Pronouns'] }}</i></p>
      {% endif %}
      {% if s['Staff Page Blurb'] %}
      <p class="content m-0">
          {{ s['Staff Page Blurb'] }}
      </p>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
