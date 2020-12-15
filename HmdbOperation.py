import pymysql


def add_user(userid, userlogin, username, iden):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.user(id,login,name,identify) VALUES (%i,'%s','%s','%s')""" % (
    userid, userlogin, username, iden)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def add_commit_author(id):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.commit_author(id) VALUES (%i)""" % (id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def add_url(url,id):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.url(url, id) VALUES ('%s','%s')""" % (url,id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def add_request(id, number, state, title, body, locked):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.request(id,number,state,title,body,locked) VALUES (%i,%i,'%s','%s','%s',%i)""" % (
        id, number, state, title, body, locked)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def add_commit(id, adddtion, deletion, total, author_id, year, month, day):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.commit(id,addition,deletion,total,author_id,year,month,day) VALUES ('%s',%i,%i,%i,%i,
    %i,%i,%i)""" % (
        id, adddtion, deletion, total, author_id, int(year), int(month), int(day))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def add_tester_rela(user, request):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.tester_rela(user,request) VALUES (%i,%i)""" % (user, request)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def add_assignees_rela(user, request):
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    cursor = db.cursor()
    sql = """INSERT INTO HMinfo.assignees_rela(user,request) VALUES (%i,%i)""" % (user, request)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
