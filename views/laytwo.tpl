<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - {{ info.name }} </title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/darkstrap.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">{{ info.name }}</a>
            </div>
            <div class="navbar-collapse collapse">

                %if info.auth:
                    <ul class="nav navbar-nav navbar-right ">
                        <li>
                         <span class="navbar-brand">
                        <img src='{{ info.avatar }}' class="face-img" alt=" ">
                         {{ info.user }}
                         <a href="/logout ">注销</a>
                         </span>
                        </li>
                    </ul>
                %else:
                <ul class="nav navbar-nav navbar-right ">
                    <li><span class="navbar-brand">
                        <a href="/login ">登录</a>
                    </span>
                    </li>
                </ul>
                %end

            </div>
        </div>
    </div>
    <div class="body-content">
        {{!base}}
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
