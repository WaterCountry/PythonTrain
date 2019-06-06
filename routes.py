"""
Routes and views for the bottle application.
"""

from bottle import route, view,redirect,request,template,static_onefile
from models import *
from config import baseinfo,getfilepath
from pony.orm import db_session
import html
from os.path import abspath,dirname,join,splitext
from urllib.parse import unquote,urlencode



@route('/home')
@view('home')
def home():
    """Renders the home page."""
    bf=baseinfo()
    dd= dict(
        title='Home',
        info=bf
    )
    return dd

@route('/member')
@db_session
def contact():
    """Renders the contact page."""
    names=select(u.name for u in User )
    bf=baseinfo()

    dd= dict(title='member',info=bf,names=names)

    return template('member',dd)


@route('/logout')
@view('home')
def logout():
    s=request.environ.get('beaker.session')
    s.delete()

    bf=baseinfo()
    dd= dict(
        title='Home',
        info=bf
    )
    return dd

@route('/login')
@view('login')
def login():
    bf=baseinfo()
    dd= dict(
        title='login',
        info=bf
    )
    return dd

@route('/login',method='POST')
@view('login')
def login():
    username = request.forms.username
    password = request.forms.password

    if username.strip() and password.strip():
        u = check_login(username, password)
        if u:
            s = request.environ.get('beaker.session')
            s['user'] = u.name
            s['id'] = u.id
            s['auth']=True
            s.save()
            return redirect('/')

    bf=baseinfo()
    dd= dict(
        title='Home',
        info=bf
    )
    return dd


faviconico='/static/images/book.gif'

@route('/favicon.ico')
def favicon():
    return faviconico

@route('/problem')
@db_session
def blog():
    page=request.query.page or '1'
    plimit=5
    problems=select(b for b in Problem )
    problemscount=problems.count()
    pnum= int( problemscount/plimit)
    if problemscount>pnum*plimit:
        pnum=pnum+1

    problems=problems.page(int(page),plimit)

    bf = baseinfo()
    dd = dict( title='Problem',info=bf, problems=problems,pagecount=pnum,cpage=int(page))

    return template('problem',dd)

@route('/problem/:id')
@db_session
def detail(id):
    b=Problem[id]
    bf=baseinfo()
    dd= dict(title='Detail',info=bf,problem=b)

    return template('detail',dd)



@route('/add',method='POST')
@db_session
def add():
    bf = baseinfo()
    if bf.auth:
        title = request.forms.title
        describe = request.forms.content
        if title.strip() and describe.strip():
            describe=html.unescape(describe)
            b = Problem(title=title, describe=describe,ratio='',level=0, update=today, author=bf.id)
            commit()
            # must commit,otherwise not add anything
            #必须要提交，否则添加不了内容

            return redirect("/problem/%d" % b.id)
    else:
        return redirect('/problem')



@route('/add')
@view('add')
def add():
    bf = baseinfo()
    if bf.auth:
        dd = dict(
            title='Add news',
            info=bf
        )
        return dd
    else:
        return redirect('/problem')


@route('/edit/:id')
@db_session
def edit(id):
    bf=baseinfo()
    if bf.auth:
        b=Problem[id]
        dd= dict(title='Edit',info=bf,blog=b)
        return template('edit',dd)
    else:
        return redirect("/problem/%s" % id)  # id is string , must be %s ,not be %d


@route('/edit/:id',method='POST')
@db_session
def add(id):
    title = request.forms.title
    describe = request.forms.content
    if title.strip() and describe.strip():
        describe=html.unescape(describe)
        b = Problem[id]
        b.title=title
        b.describe=describe
        b.update=today
        commit()
        # We must put the commit() command here, but it is very necessary
        # because PonyPlugin will take no care of this!!!
        return redirect("/problem/%d" % b.id)


@route('/register')
@view('register')
def register():
    bf=baseinfo()
    dd= dict(
        title='register',
        info=bf
    )
    return dd


@route('/register',method='POST')
@view('register')
@db_session
def register():
    username = request.forms.username
    password = request.forms.password
    signature = request.forms.signature

    if username.strip() and password.strip():
        u = User( name=username, signature=signature, password=password, regdate=today,avatar='')
        commit()
        s = request.environ.get('beaker.session')
        s['name'] = u.name
        s['id'] = u.id
        s['auth'] = True
        s.save()
        return redirect('/')
    else:
        return "need username and password! "


@route('/python')
@db_session
def program():
    page = request.query.page or '1'
    plimit = 5
    problems = select(p for p in Problem)
    problemscount = problems.count()
    pnum = int(problemscount / plimit)
    if problemscount > pnum * plimit:
        pnum = pnum + 1

    problems = problems.page(int(page), plimit)

    bf = baseinfo()
    dd = dict(title='Problems', info=bf, problems=problems, pagecount=pnum, cpage=int(page))

    return template('source', dd)


@route('/')
@route('/python/:id')
@db_session
def code(id=1):
    p=Problem[id]
    problems=select(m for m in Problem)
    bf=baseinfo()
    dd= dict(title='Code Detail',info=bf,problems=problems,program=p)

    return template('source',dd)


@route('/write',method='POST')
@db_session
def write():
    bf = baseinfo()
    if bf.auth:
        title = request.forms.title
        pcode = request.forms.code
        if title.strip() and pcode.strip():
            pcode=html.unescape(pcode)
            p=Problem(title=title,code=pcode,update=today,level='0')
            commit()
            # must commit,otherwise not add anything
            #必须要提交，否则添加不了内容

            return redirect("/program/%d" % p.id)
    else:
        return redirect('/program')


@route('/judge',method='POST')
def judge():
    progradcode=request.forms.code

    return  progradcode


