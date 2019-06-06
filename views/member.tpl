% rebase('layout.tpl', title=title)

<h2>{{ title }}</h2>
<hr>
<ul>
    %for m in names:
    <li>
        <h3> {{m}}</h3>
    </li>
    %end
</ul>

