% rebase('layout.tpl')

<h1>{{ problem.title }}.</h1>

<div>{{!problem.describe}}</div>

<p>{{problem.update}}</p>
<p>{{problem.author.name}}</p>
<div style="text-align:right;">
    <a class="btn btn-primary" role="button" href="/edit/{{ problem.id}}" target="_self">修改</a>

    <a class="btn btn-primary" role="button" href="/problem" target="_self">返回</a>

<br><br>
</div>