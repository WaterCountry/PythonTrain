from bottle import request
from datetime import datetime
from beaker.middleware import SessionMiddleware
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
STORE_ROOT = os.path.join(PROJECT_ROOT, 'store').replace('\\', '/')


def getfilepath(dirname,filename):
    ## return abspath
    FPATH_ROOT=os.path.join(PROJECT_ROOT,dirname).replace('\\','/')
    filepath=FPATH_ROOT+'/'+filename
    return filepath

def baseinfo():
    # base infomation name,year,auth,nick,avatar
    bf=info()
    session=request.environ.get('beaker.session')

    if session:
        bf.user=session.get('name')
        bf.auth=session.get('auth')
        bf.id=session.get('id')
    else:
        bf.auth=False

    return bf


class info:
    def __init__(self):
        self.name="Python Train"
        self.year=datetime.now().year
        self.auth=False
        self.id=""
        self.user="Guest"
        self.avatar='/static/avatar/river.jpg'
        self.title=""
        self.writer="温州水乡"
