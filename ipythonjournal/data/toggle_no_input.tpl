<!-- adapted from http://stackoverflow.com/a/24067557 -->

{%- extends 'full.tpl' -%}

{% block output_group %}
<div class="output_hidden">
{{ super() }}
</div>
{% endblock output_group %}

{% block input_group -%}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}

{%- block header -%}
{{ super() }}

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<style type="text/css">
div.cell {
  padding: 0px;
  border-style: none;
}

div.output_wrapper {
  margin-top: 0px;
}
.output_hidden {
  display: block;
  margin-top: 5px;
}

div.input_wrapper {
  margin-top: 0px;
}
.input_hidden {
  display: none;
  margin-top: 5px;
}
</style>

<script>
$(document).ready(function(){
  $(".output_hidden").click(function(){
      $(this).prev('.input_hidden').slideToggle();
  });
  $(".input_hidden").click(function(){
      $(this).next('.output_hidden').slideToggle();
  });

})
</script>
{%- endblock header -%}
