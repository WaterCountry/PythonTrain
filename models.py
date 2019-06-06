from pony.orm import *
from datetime import date,datetime

db=Database('sqlite', filename="train.sqlite", create_db=True)

class User(db.Entity):
    role=Required(bool)
    name=Required(str)
    signature=Required(str)
    password=Required(str)
    regdate=Required(date)
    avatar=Required(str)
    problems=Set("Problem")
    answers=Set("Answer")

class Problem(db.Entity):
    title=Required(str)
    describe=Required(str)
    ratio=Required(str)
    level=Required(int)
    update=Required(date)
    author=Required(User)
    answers=Set("Answer")

class Answer(db.Entity):
    code=Required(str)
    judge=Required(str)
    times=Required(int)
    update = Required(date)
    author = Required(User)
    problem=Required(Problem)


sql_debug(True)
db.generate_mapping(create_tables=True)
today=datetime.now()

@db_session
def populate_database():
    if select(u for u in User).count() > 0:
        return
    u1=User(role=True,name='zhou',signature='fun',password='123',regdate=today,avatar='river.jpg')
    u2=User(role=False,name='ming',signature='阳光',password='123',regdate=today,avatar='hill.jpg')
    Problem(title='a+b',describe='给你两个数a、b，请你计算它们的和，并输出。',ratio='0',level=0,update=today,author=User[1])


populate_database()

@db_session
def check_login(username,password):
    loginuser = select(u for u in User if u.name == username and u.password == password).first()
    return loginuser










